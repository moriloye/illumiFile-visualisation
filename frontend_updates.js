import React, { useState, useEffect } from "react";

const MetaAlertsDashboard = () => {
  const [metaAlerts, setMetaAlerts] = useState([]);
  const [delta, setDelta] = useState("0.5");
  const [phase, setPhase] = useState("");
  const [similarity, setSimilarity] = useState(0);

  // Fetch meta-alerts with filters
  useEffect(() => {
    const queryParams = new URLSearchParams({
      delta,
      ...(phase && { phase }), // Include phase only if selected
      ...(similarity > 0 && { similarity }), // Include similarity if > 0
    });
    fetch(`/api/meta_alerts?${queryParams.toString()}`)
      .then((res) => res.json())
      .then((data) => setMetaAlerts(data));
  }, [delta, phase, similarity]);

  return (
    <div>
      <h1>Meta-Alerts Dashboard</h1>

      {/* Filters */}
      <div>
        <label>
          Delta:
          <select value={delta} onChange={(e) => setDelta(e.target.value)}>
            <option value="0.5">0.5</option>
            <option value="5">5</option>
          </select>
        </label>
        <label>
          Phase:
          <select value={phase} onChange={(e) => setPhase(e.target.value)}>
            <option value="">All Phases</option>
            <option value="nmap">nmap</option>
            <option value="nikto">nikto</option>
            <option value="vrfy">vrfy</option>
            <option value="hydra">hydra</option>
            <option value="upload">upload</option>
            <option value="exploit">exploit</option>
          </select>
        </label>
        <label>
          Similarity Threshold:
          <input
            type="range"
            min="0"
            max="1"
            step="0.01"
            value={similarity}
            onChange={(e) => setSimilarity(e.target.value)}
          />
          {similarity}
        </label>
      </div>

      {/* Meta-Alerts Display */}
      <ul>
        {metaAlerts.map((alert) => (
          <li key={alert.id}>
            Phase: {alert.phase}, Alerts: {alert.alerts}, Similarity: {alert.sim}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MetaAlertsDashboard;
