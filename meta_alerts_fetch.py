@app.route("/api/meta_alerts", methods=["GET"])
def get_meta_alerts():
    delta = request.args.get("delta", "0.5")
    meta_alerts = parse_meta_alerts(f"data/out/aggregate/meta_alerts_{delta}.txt")
    return jsonify(meta_alerts)
