import { useEffect, useState } from "react"
import { getSummary, getServices, getAlerts } from "../services/api"
import type { Summary, ServiceCost, Alert } from "../types"

export default function Dashboard() {
  const [summary, setSummary] = useState<Summary | null>(null)
  const [services, setServices] = useState<ServiceCost[]>([])
  const [alerts, setAlerts] = useState<Alert[]>([])

  useEffect(() => {
    async function fetchData() {
      const s = await getSummary()
      const svc = await getServices()
      const al = await getAlerts()

      setSummary(s)
      setServices(svc)
      setAlerts(al)
    }

    fetchData()
  }, [])

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <h1 className="text-3xl font-bold mb-6">
        CloudCost Guardian
      </h1>

      {/* Summary */}
      {summary && (
        <div className="mb-6">
          <h2 className="text-xl mb-2">Summary</h2>
          <p>Monthly: ${summary.monthly_total}</p>
          <p>Daily: ${summary.daily_total}</p>
        </div>
      )}

      {/* Services */}
      <div className="mb-6">
        <h2 className="text-xl mb-2">Services</h2>
        {services.map((s) => (
          <div key={s.service}>
            {s.service}: ${s.monthly_cost}
          </div>
        ))}
      </div>

      {/* Alerts */}
      <div>
        <h2 className="text-xl mb-2">Alerts</h2>
        {alerts.map((a, i) => (
          <div key={i} className="text-red-400">
            {a.message}
          </div>
        ))}
      </div>
    </div>
  )
}
