import { useEffect, useState } from "react"
import { getSummary, getServices, getAlerts, getDailyCosts } from "../services/api"
import type { Summary, ServiceCost, Alert, DailyCost } from "../types"
import ServiceChart from "../components/dashboard/ServiceChart"
import BudgetPanel from "../components/BudgetPanel"
import PageHeader from "../components/layout/PageHeader"
import SummaryCard from "../components/dashboard/SummaryCard"
import ServiceList from "../components/dashboard/ServiceList"
import AlertList from "../components/dashboard/AlertList"
import TrendChart from "../components/dashboard/TrendChart"
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

    const interval = setInterval(fetchData, 3000)

    return () => clearInterval(interval)
  }, [])

  return (
    <div className="min-h-screen bg-gray-950 text-white">
      <div className="relative">
        <div className="absolute inset-0 bg-gradient-to-r from-blue-500/10 to-purple-500/10 blur-3xl" />

        <div className="relative mx-auto flex w-full max-w-6xl flex-col space-y-8 px-6 py-10 lg:px-8">
          <PageHeader />

          {summary && (
            <div className="grid gap-6 md:grid-cols-2">
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
              <SimulatorToggle />
            </div>
          )}

          {trend.length > 0 && <TrendChart data={trend} />}

          <div className="grid grid-cols-1 gap-6 md:grid-cols-2">
            <BudgetPanel />
            <AlertList alerts={alerts} />
          </div>

          <div className="grid grid-cols-1 gap-6">
            <ServiceChart services={services} />
          </div>

          <div className="grid grid-cols-1 gap-6">
            <ServiceList services={services} />
          </div>
        </div>
      </div>
    </div>
  )
}
