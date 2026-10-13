import os
from flask import Flask, jsonify, request, send_file
from pymongo import MongoClient

app = Flask(__name__)

PORT = 3030
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MONGO_URL = "mongodb://khizer-db:password123@localhost:27017/?authSource=admin"
client = MongoClient(MONGO_URL)


@app.route("/")
def home():
    return send_file(os.path.join(BASE_DIR, "index.html"))


# GET all users
@app.route("/getUsers", methods=["GET"])
def get_users():
    db = client["my-sample-db"]
    data = list(db["users"].find({}))
    print("Connected successfully to server")

    for doc in data:
        doc["_id"] = str(doc["_id"])
    return jsonify(data)


# POST new user
@app.route("/addUser", methods=["POST"])
def add_user():
    user_obj = request.form.to_dict()
    print("Connected successfully to server")

    db = client["my-sample-db"]
    result = db["users"].insert_one(user_obj)
    print(result)
    print("data inserted in DB")

    return "data inserted in DB"


if __name__ == "__main__":
    print(f"server running on port {PORT}")
    app.run(host="0.0.0.0", port=PORT)
