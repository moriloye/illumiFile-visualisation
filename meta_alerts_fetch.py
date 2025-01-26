from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import json

# Initialize Flask and Flask-SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Enable CORS for WebSocket connections

# Function to parse meta-alerts
def parse_meta_alerts(meta_alerts_file, phase_filter=None, similarity_threshold=None):
    meta_alerts = []
    with open(meta_alerts_file, 'r') as f:
        for line in f:
            if "meta-alert" in line:
                parts = line.split()
                meta_alert = {
                    "id": int(parts[4]),
                    "phase": parts[-1],
                    "alerts": int(parts[8]),
                    "sim": float(parts[-2].split('=')[1])
                }
                # Apply filters
                if phase_filter and meta_alert["phase"] != phase_filter:
                    continue
                if similarity_threshold and meta_alert["sim"] < similarity_threshold:
                    continue
                meta_alerts.append(meta_alert)
    return meta_alerts

@app.route("/api/meta_alerts", methods=["GET"])
def get_meta_alerts():
    delta = request.args.get("delta", "0.5")
    phase_filter = request.args.get("phase")
    similarity_threshold = request.args.get("similarity")
    similarity_threshold = float(similarity_threshold) if similarity_threshold else None
    meta_alerts = parse_meta_alerts(f"data/out/aggregate/meta_alerts_{delta}.txt",
                                    phase_filter, similarity_threshold)
    return jsonify(meta_alerts)

@app.route("/api/realtime_aggregation", methods=["POST"])
def realtime_aggregation():
    # Simulate processing new alerts (replace with real logic for AECID updates)
    new_alerts = request.json.get("alerts", [])
    delta = request.json.get("delta", 0.5)

    # Notify clients of new alerts via WebSocket
    socketio.emit("new_alerts", {"delta": delta, "alerts": len(new_alerts)})

    return jsonify({"status": "success", "processed_alerts": len(new_alerts)})

# WebSocket event to handle client connections
@socketio.on("connect")
def handle_connect():
    print("Client connected")
    emit("connected", {"message": "Welcome to the Meta-Alerts Dashboard WebSocket!"})

if __name__ == "__main__":
    socketio.run(app, debug=True)
