import React, { useState, useEffect } from "react";
import io from "socket.io-client";

const socket = io("http://localhost:5000"); // Backend WebSocket URL

const RealtimeDashboard = () => {
  const [metaAlerts, setMetaAlerts] = useState([]);
  const [newAlerts, setNewAlerts] = useState(null);

  // Fetch initial data and listen for WebSocket events
  useEffect(() => {
    // Fetch initial meta-alerts
    fetch("/api/meta_alerts?delta=0.5")
      .then((res) => res.json())
      .then((data) => setMetaAlerts(data));

    // Listen for real-time updates
    socket.on("new_alerts", (data) => {
      setNewAlerts(data);
    });

    return () => {
      socket.disconnect();
    };
  }, []);

  return (
    <div>
      <h1>Real-Time Meta-Alerts Dashboard</h1>
      <ul>
        {metaAlerts.map((alert) => (
          <li key={alert.id}>
            Phase: {alert.phase}, Alerts: {alert.alerts}, Similarity: {alert.sim}
          </li>
        ))}
      </ul>

      {newAlerts && (
        <div style={{ marginTop: "20px", padding: "10px", border: "1px solid green" }}>
          <h2>New Alerts Received</h2>
          <p>Delta: {newAlerts.delta}</p>
          <p>Processed Alerts: {newAlerts.alerts}</p>
        </div>
      )}
    </div>
  );
};

export default RealtimeDashboard;
