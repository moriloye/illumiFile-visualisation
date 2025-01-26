import { render, screen } from "@testing-library/react";
import RealtimeDashboard from "./RealtimeDashboard";

test("renders meta-alerts", async () => {
  render(<RealtimeDashboard />);
  const titleElement = await screen.findByText(/Real-Time Meta-Alerts Dashboard/i);
  expect(titleElement).toBeInTheDocument();
});
