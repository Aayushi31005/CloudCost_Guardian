import { useState, useEffect } from "react"
import { getBudget, saveBudget } from "../services/api"

type Props = {
  service: "ec2" | "s3"
  onServiceChange: (service: "ec2" | "s3") => void
}

export default function BudgetPanel({ service, onServiceChange }: Props) {
  const [daily, setDaily] = useState("")
  const [monthly, setMonthly] = useState("")
  const [error, setError] = useState("")
  const [saving, setSaving] = useState(false)

  useEffect(() => {
    async function loadBudget() {
      try {
        const data = await getBudget(service)
        setDaily(String(data.daily_limit))
        setMonthly(String(data.monthly_limit))
        setError("")
      } catch {
        setError("Unable to load budget settings right now.")
      }
    }

    loadBudget()
  }, [service])

  const handleSaveBudget = async () => {
    try {
      setSaving(true)
      await saveBudget({
        service,
        daily_limit: Number(daily) || 0,
        monthly_limit: Number(monthly) || 0,
      })
      setError("")
    } catch {
      setError("Unable to save budget settings right now.")
    } finally {
      setSaving(false)
    }
  }

  return (
    <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">

      <h2 className="text-sm text-gray-400 uppercase tracking-wide mb-4">
        Budget Configuration
      </h2>

      {error && (
        <p className="mb-4 text-sm text-red-400">
          {error}
        </p>
      )}

      <div className="space-y-3">
        <div>
          <label className="text-xs text-gray-400">Service</label>

          <select
            value={service}
            onChange={(e) => onServiceChange(e.target.value as "ec2" | "s3")}
            className="w-full mt-1 bg-gray-800 border border-gray-700 rounded-md p-2 text-white"
          >
            <option value="ec2">EC2</option>
            <option value="s3">S3</option>
          </select>
        </div>

        <div>
          <label className="text-xs text-gray-400">Daily Budget</label>

          <input
            type="number"
            value={daily}
            onChange={(e) => setDaily(e.target.value)}
            className="w-full mt-1 bg-gray-800 border border-gray-700 rounded-md p-2 text-white"
          />
        </div>

        <div>
          <label className="text-xs text-gray-400">Monthly Budget</label>

          <input
            type="number"
            value={monthly}
            onChange={(e) => setMonthly(e.target.value)}
            className="w-full mt-1 bg-gray-800 border border-gray-700 rounded-md p-2 text-white"
          />
        </div>

        <button
          onClick={handleSaveBudget}
          className="w-full mt-3 bg-blue-600 hover:bg-blue-500 text-white py-2 rounded-md"
        >
          {saving ? "Saving..." : "Save Budget"}
        </button>

      </div>

    </div>
  )
}
