from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/alerts', methods=['GET'])
def get_alerts():
    # Read HIDS alerts (or aggregated-enhanced alerts)
    with open('/var/ossec/logs/alerts/alerts.log', 'r') as f:
        alerts = f.readlines()
    return jsonify(alerts)

@app.route('/stats', methods=['GET'])
def get_stats():
    # Example: Get HIDS stats
    stats = subprocess.check_output(['/var/ossec/bin/ossec-control', 'status'])
    return jsonify(stats.decode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True)
