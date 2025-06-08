from pymongo import MongoClient
from datetime import datetime


client = MongoClient("mongodb://localhost:27017/")
db = client["webhookDB"]
collection = db["events"]

def insert_event(event_type, author, from_branch=None, to_branch=None, timestamp=None):
    if timestamp is None:
        timestamp = datetime.utcnow()
    elif isinstance(timestamp, str):
        timestamp = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))

    event = {
        "event_type": event_type,
        "author": author,
        "from_branch": from_branch,
        "to_branch": to_branch,
        "timestamp": timestamp
    }

    event = {k: v for k, v in event.items() if v is not None}
    collection.insert_one(event)

def get_latest_events(limit=20):
    return list(collection.find({}, {"_id": 0}).sort("timestamp", -1).limit(limit))
