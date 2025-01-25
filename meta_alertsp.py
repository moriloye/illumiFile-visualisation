import json

def parse_meta_alerts(meta_alerts_file):
    meta_alerts = []
    with open(meta_alerts_file, 'r') as f:
        for line in f:
            # Example line parsing: Extract meta-alert details
            if "meta-alert" in line:
                parts = line.split()
                meta_alerts.append({
                    "id": int(parts[4]),
                    "phase": parts[-1],
                    "alerts": int(parts[8]),
                    "sim": float(parts[-2].split('=')[1])
                })
    return meta_alerts

def parse_alerts(alerts_file):
    alerts = []
    with open(alerts_file, 'r') as f:
        for line in f:
            # Parse individual alerts (structure depends on file format)
            pass
    return alerts

# Example Usage
meta_alerts = parse_meta_alerts("data/out/aggregate/meta_alerts.txt")
print(json.dumps(meta_alerts, indent=2))
