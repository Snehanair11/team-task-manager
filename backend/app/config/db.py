from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("❌ MONGO_URI not found in .env file")

# Create MongoDB client
client = AsyncIOMotorClient(MONGO_URI)

# Database reference
db = client["task_manager"]