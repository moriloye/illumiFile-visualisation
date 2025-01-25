from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Helper function to parse meta-alerts from a file
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

                # Apply filters if specified
                if phase_filter and meta_alert["phase"] != phase_filter:
                    continue
                if similarity_threshold and meta_alert["sim"] < similarity_threshold:
                    continue

                meta_alerts.append(meta_alert)
    return meta_alerts

# API endpoint to fetch filtered meta-alerts
@app.route("/api/meta_alerts", methods=["GET"])
def get_meta_alerts():
    # Extract query parameters
    delta = request.args.get("delta", "0.5")
    phase_filter = request.args.get("phase")  # Optional phase filter
    similarity_threshold = request.args.get("similarity")
    similarity_threshold = float(similarity_threshold) if similarity_threshold else None

    # Parse and filter meta-alerts
    meta_alerts = parse_meta_alerts(
        f"data/out/aggregate/meta_alerts_{delta}.txt",
        phase_filter=phase_filter,
        similarity_threshold=similarity_threshold,
    )
    return jsonify(meta_alerts)

# Real-time aggregation (mock function for demonstration)
@app.route("/api/realtime_aggregation", methods=["POST"])
def realtime_aggregation():
    # Simulate processing new alerts (replace with real logic for AECID updates)
    new_alerts = request.json.get("alerts", [])
    delta = request.json.get("delta", 0.5)

    # For demonstration, return the number of new alerts processed
    return jsonify({
        "status": "success",
        "delta": delta,
        "processed_alerts": len(new_alerts)
    })

if __name__ == "__main__":
    app.run(debug=True)
