const API_BASE = "http://127.0.0.1:8010"

export async function getSummary() {
  const res = await fetch(`${API_BASE}/dashboard/summary`)
  return res.json()
}

export async function getServices() {
  const res = await fetch(`${API_BASE}/dashboard/services`)
  return res.json()
}

export async function getAlerts() {
  const res = await fetch(`${API_BASE}/alerts/`)
  return res.json()
}