import React, { useState, useEffect } from "react";
import Chart from "chart.js";

const MetaAlertsDashboard = () => {
  const [metaAlerts, setMetaAlerts] = useState([]);
  const [delta, setDelta] = useState("0.5");

  useEffect(() => {
    fetch(`/api/meta_alerts?delta=${delta}`)
      .then((res) => res.json())
      .then((data) => setMetaAlerts(data));
  }, [delta]);

  return (
    <div>
      <h1>Meta-Alerts Dashboard</h1>
      <label>
        Delta:
        <select value={delta} onChange={(e) => setDelta(e.target.value)}>
          <option value="0.5">0.5</option>
          <option value="5">5</option>
        </select>
      </label>
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
