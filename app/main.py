# PinCodeFlow - GeoDistance Calculation Python API

# December 2025 Apex Standards Edition

# Imports
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from geopy.distance import geodesic
import pygeohash  # Assuming pygeohash is used for indexing
import redis  # Assuming Redis is used for caching

# --- Configuration ---
# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Redis Cache Configuration
# In a real-world scenario, this would be externalized (e.g., .env file)
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
CACHE_EXPIRY_SECONDS = 3600  # 1 hour

try:
    redis_client = redis.StrictRedis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        decode_responses=True  # Automatically decode responses from bytes to strings
    )
    redis_client.ping()  # Check connection
    logger.info(f"Connected to Redis at {REDIS_HOST}:{REDIS_PORT}")
except redis.exceptions.ConnectionError as e:
    logger.error(f"Could not connect to Redis: {e}. Cache functionality will be disabled.")
    redis_client = None

# --- Data Models -- (Adhering to Pydantic standards)

class PincodeInfo(BaseModel):
    pincode: str
    latitude: float
    longitude: float

class DistanceRequest(BaseModel):
    pincode1: str
    pincode2: str

class DistanceResponse(BaseModel):
    pincode1: str
    pincode2: str
    distance_km: float
    distance_miles: float
    geohash1: str | None = None # Optional: Include geohash for indexing context
    geohash2: str | None = None

# --- Mock Data Store ---
# In a production environment, this would interface with a proper database
# (e.g., PostgreSQL with PostGIS, specialized geospatial DBs).
# For demonstration, a dictionary will simulate data retrieval for pincodes.
# Format: { "pincode": {"latitude": float, "longitude": float} }
# This data should be pre-populated or fetched from a reliable source.

MOCK_PINCODE_DATA = {
    "110001": {"latitude": 28.6139, "longitude": 77.2090}, # New Delhi
    "400001": {"latitude": 19.0760, "longitude": 72.8777}, # Mumbai
    "600001": {"latitude": 13.0827, "longitude": 80.2707}, # Chennai
    "700001": {"latitude": 22.5726, "longitude": 88.3639}, # Kolkata
    "560001": {"latitude": 12.9716, "longitude": 77.5946}, # Bengaluru
    "110010": {"latitude": 28.6300, "longitude": 77.1800}, # Another Delhi Pincode
    "400002": {"latitude": 19.0800, "longitude": 72.8800}, # Another Mumbai Pincode
}

# --- Helper Functions ---

def get_pincode_coordinates(pincode: str) -> tuple[float, float] | None:
    """Retrieves latitude and longitude for a given pincode from the mock data.

    In a real system, this would query a database with geospatial capabilities.
    """
    if pincode in MOCK_PINCODE_DATA:
        coords = MOCK_PINCODE_DATA[pincode]
        return coords["latitude"], coords["longitude"]
    logger.warning(f"Pincode {pincode} not found in mock data.")
    return None

def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> tuple[float, float]:
    """Calculates distance in kilometers and miles using geopy.

    Returns: (distance_km, distance_miles)
    """
    coords1 = (lat1, lon1)
    coords2 = (lat2, lon2)
    distance_km = geodesic(coords1, coords2).km
    distance_miles = geodesic(coords1, coords2).miles
    return distance_km, distance_miles

def get_geohash(lat: float, lon: float, precision: int = 7) -> str:
    """Generates a geohash for given coordinates.

    Precision level can be adjusted based on desired spatial resolution.
    """
    return pygeohash.encode(lat, lon, precision=precision)

def get_from_cache(key: str) -> str | None:
    """Retrieves data from Redis cache.
    """
    if redis_client:
        try:
            return redis_client.get(key)
        except redis.exceptions.RedisError as e:
            logger.error(f"Redis GET error for key {key}: {e}")
    return None

def set_to_cache(key: str, value: str):
    """Sets data in Redis cache with expiry.
    """
    if redis_client:
        try:
            redis_client.setex(key, CACHE_EXPIRY_SECONDS, value)
        except redis.exceptions.RedisError as e:
            logger.error(f"Redis SETEX error for key {key}: {e}")

# --- FastAPI Application Setup ---

# Applying Hexagonal Architecture principles: API Layer (Adapter)
# The core logic is intended to be separated from this interface.

app = FastAPI(
    title="PinCodeFlow API",
    description="High-performance Python REST API for rapid, accurate distance calculation and route optimization between Indian Pincode locations.",
    version="1.0.0",
    contact={
        "name": "Chirag Sharma",
        "url": "https://github.com/chirag127/PinCodeFlow-GeoDistance-Calculation-Python-API",
        "email": "chirag.sharma@example.com", # Placeholder email
    },
    license_info={
        "name": "CC BY-NC 4.0 License",
        "url": "https://creativecommons.org/licenses/by-nc/4.0/",
    },
)

# --- API Endpoints ---

@app.get("/", summary="Health Check Endpoint", tags=["Utilities"])
async def health_check():
    """Basic health check endpoint to verify API is running.
    """
    return {"status": "ok", "message": "PinCodeFlow API is operational."}

@app.post("/distance/", response_model=DistanceResponse, summary="Calculate Distance Between Two Pincodes", tags=["GeoDistance"])
async def calculate_pincode_distance(request: DistanceRequest):
    """Calculates the geodesic distance between two Indian pincodes.

    - **Request Body:** `DistanceRequest` model containing `pincode1` and `pincode2`.
    - **Response Body:** `DistanceResponse` model with distances in KM and Miles, and optionally their geohashes.

    Uses caching for repeated requests.
    """
    # Create a cache key based on sorted pincodes to ensure uniqueness regardless of order
    cache_key = f"distance:{'_'.join(sorted([request.pincode1, request.pincode2]))}"

    # Check cache first
    cached_result = get_from_cache(cache_key)
    if cached_result:
        logger.info(f"Cache hit for key: {cache_key}")
        return DistanceResponse.parse_raw(cached_result)

    # Retrieve coordinates
    coords1 = get_pincode_coordinates(request.pincode1)
    coords2 = get_pincode_coordinates(request.pincode2)

    if not coords1:
        raise HTTPException(status_code=404, detail=f"Pincode {request.pincode1} not found.")
    if not coords2:
        raise HTTPException(status_code=404, detail=f"Pincode {request.pincode2} not found.")

    lat1, lon1 = coords1
    lat2, lon2 = coords2

    # Calculate distances
    distance_km, distance_miles = calculate_distance(lat1, lon1, lat2, lon2)

    # Generate geohashes (optional, for indexing/representation)
    geohash1 = get_geohash(lat1, lon1)
    geohash2 = get_geohash(lat2, lon2)

    # Prepare response
    response_data = DistanceResponse(
        pincode1=request.pincode1,
        pincode2=request.pincode2,
        distance_km=round(distance_km, 3), # Round for readability
        distance_miles=round(distance_miles, 3),
        geohash1=geohash1,
        geohash2=geohash2,
    )

    # Store in cache
    set_to_cache(cache_key, response_data.json())
    logger.info(f"Cache miss, calculated and stored result for key: {cache_key}")

    return response_data

# --- CLI Execution ---
# This part would typically be handled by a separate script (e.g., main.py or run.py)
# when using uvicorn for serving. For simplicity, we include a conditional block.
# In a production setup, you'd use `uvicorn app.main:app --reload` from the terminal.

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Uvicorn server for PinCodeFlow API...")
    # Note: --reload is for development. Remove for production.
    # Use host="0.0.0.0" to make it accessible externally.
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
