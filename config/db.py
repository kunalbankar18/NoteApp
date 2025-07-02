from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

conn=MongoClient(MONGO_URI)
