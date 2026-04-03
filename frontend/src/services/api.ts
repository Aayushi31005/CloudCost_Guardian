const API_BASE = "http://127.0.0.1:8010"
const USER_TIMEZONE = Intl.DateTimeFormat().resolvedOptions().timeZone

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

export async function getDailyCosts() {
  const res = await fetch(`${API_BASE}/analytics/daily-costs`, {
    headers: {
      "X-Timezone": USER_TIMEZONE,
    },
  })
  return res.json()
}

export async function startSimulator() {
  await fetch(`${API_BASE}/simulator/start`, { method: "POST" })
}

export async function stopSimulator() {
  await fetch(`${API_BASE}/simulator/stop`, { method: "POST" })
}

export async function getSimulatorStatus() {
  const res = await fetch(`${API_BASE}/simulator/status`)
  return res.json()
}
