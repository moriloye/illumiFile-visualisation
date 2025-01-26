const RealtimeAggregation = () => {
  const [alerts, setAlerts] = useState(""); // Simulated alert data
  const [delta, setDelta] = useState("0.5");
  const [response, setResponse] = useState(null);

  const submitAlerts = () => {
    fetch("/api/realtime_aggregation", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ alerts: alerts.split("\n"), delta }),
    })
      .then((res) => res.json())
      .then((data) => setResponse(data));
  };

  return (
    <div>
      <h2>Real-Time Aggregation</h2>
      <textarea
        rows="5"
        cols="50"
        placeholder="Paste alert data here..."
        value={alerts}
        onChange={(e) => setAlerts(e.target.value)}
      />
      <br />
      <label>
        Delta:
        <select value={delta} onChange={(e) => setDelta(e.target.value)}>
          <option value="0.5">0.5</option>
          <option value="5">5</option>
        </select>
      </label>
      <button onClick={submitAlerts}>Submit Alerts</button>
      {response && (
        <div>
          <h3>Response</h3>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default RealtimeAggregation;
