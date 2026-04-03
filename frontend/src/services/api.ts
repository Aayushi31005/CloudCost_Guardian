import type { BudgetConfig, CostHistoryPoint } from "../types"

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

export async function getCostHistory(granularity: "daily" | "weekly" | "monthly"): Promise<CostHistoryPoint[]> {
  const res = await fetch(`${API_BASE}/analytics/cost-history?granularity=${granularity}`, {
    headers: {
      "X-Timezone": USER_TIMEZONE,
    },
  })

  if (!res.ok) {
    throw new Error("Failed to load cost history")
  }

  return res.json()
}

export async function getBudget(): Promise<BudgetConfig> {
  const res = await fetch(`${API_BASE}/budget`)

  if (!res.ok) {
    throw new Error("Failed to load budget")
  }

  return res.json()
}

export async function saveBudget(config: BudgetConfig): Promise<BudgetConfig> {
  const res = await fetch(`${API_BASE}/budget`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(config),
  })

  if (!res.ok) {
    throw new Error("Failed to save budget")
  }

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
