# MongoDB

## MongoDB install

```bash
sudo apt update && sudo apt install gnupg curl -y
curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg --dearmor
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/8.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list
sudo apt update
sudo apt install -y mongodb-org
sudo systemctl start mongod
sudo systemctl enable mongod
sudo systemctl status mongod
```

## Community-CE GUI (Optional)

https://www.mongodb.com/try/download/compass

```bash
sudo dpkg -i mongodb-compass_ver_amd64.deb
```

## PIP

```bash
pip install pymongo
```

## Write DB

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["my_new_database"]

collection = db["my_collection"]

record = {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 28,
    "status": "active"
}

result = collection.insert_one(record)

print(f"Record inserted successfully with ID: {result.inserted_id}")

```

## Read DB

```python
import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["my_new_database"]
collection = db["my_collection"]

query = {"email": "alice@example.com"}
record = collection.find_one(query)

print("--- Found by Email ---")
print(record)

try:
    target_id = "PASTE_ID_HERE" 
    record_by_id = collection.find_one({"_id": ObjectId(target_id)})
    
    print("\n--- Found by ObjectId ---")
    print(record_by_id)
except Exception as e:
    print(f"\nCould not search by ObjectId: {e}")

```
