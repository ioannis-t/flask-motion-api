from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/api/motion", methods=["GET"])
def motion_command():
    command = {
        "base": random.randint(0, 180),
        "shoulder": random.randint(0, 90),
        "elbow": random.randint(0, 90),
        "wrist": random.randint(-45, 45),
        "duration_ms": random.randint(500, 1500)
    }
    return jsonify(command)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
