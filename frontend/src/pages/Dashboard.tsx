import { useEffect, useState } from "react"
import { getSummary, getServices, getAlerts, getDailyCosts } from "../services/api"
import type { Summary, ServiceCost, Alert, DailyCost } from "../types"
import ServiceChart from "../components/dashboard/ServiceChart"
import PageHeader from "../components/layout/PageHeader"
import SummaryCard from "../components/dashboard/SummaryCard"
import ServiceList from "../components/dashboard/ServiceList"
import AlertList from "../components/dashboard/AlertList"
import TrendChart from "../components/dashboard/TrendChart"
import UsageForm from "../components/dashboard/UsageForm"
import SimulatorToggle from "../components/dashboard/SimulatorToggle"

export default function Dashboard() {
  const [summary, setSummary] = useState<Summary | null>(null)
  const [services, setServices] = useState<ServiceCost[]>([])
  const [alerts, setAlerts] = useState<Alert[]>([])
  const [trend, setTrend] = useState<DailyCost[]>([])

  useEffect(() => {
    async function fetchData() {
      const s = await getSummary()
      const svc = await getServices()
      const al = await getAlerts()
      const t = await getDailyCosts()

      setSummary(s)
      setServices(svc)
      setAlerts(al)
      setTrend(t)
    }

    fetchData()

    const interval = setInterval(fetchData, 5000)

    return () => clearInterval(interval)
  }, [])

  return (
    <div className="min-h-screen bg-gray-950 text-white px-10 py-8">
      <PageHeader />

      {summary && (
        <div className="grid grid-cols-2 gap-6 mb-10">
          <SummaryCard
            title="Monthly Spend"
            value={summary.monthly_total}
            variant="primary"
          />
          <SummaryCard
            title="Daily Spend"
            value={summary.daily_total}
            variant="success"
          />
          <div className="mb-10">
            <UsageForm />
          </div>
          <SimulatorToggle />
        </div>
      )}

      {trend.length > 0 && (
        <div className="mb-10">
          <TrendChart data={trend} />
        </div>
      )}

      <div className="grid grid-cols-2 gap-6 mb-6">
        <ServiceChart services={services} />
        <AlertList alerts={alerts} />
      </div>

      <div className="grid grid-cols-1 gap-6">
        <ServiceList services={services} />
      </div>
    </div>
  )
}
