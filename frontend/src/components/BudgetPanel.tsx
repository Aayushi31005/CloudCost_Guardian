import { useState, useEffect } from "react"
import { getBudget, saveBudget } from "../services/api"

export default function BudgetPanel() {
  const [daily, setDaily] = useState(0)
  const [monthly, setMonthly] = useState(0)
  const [error, setError] = useState("")
  const [saving, setSaving] = useState(false)

  useEffect(() => {
    async function loadBudget() {
      try {
        const data = await getBudget()
        setDaily(data.daily_limit)
        setMonthly(data.monthly_limit)
        setError("")
      } catch {
        setError("Unable to load budget settings right now.")
      }
    }

    loadBudget()
  }, [])

  const handleSaveBudget = async () => {
    try {
      setSaving(true)
      await saveBudget({
        daily_limit: daily,
        monthly_limit: monthly,
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
          <label className="text-xs text-gray-400">Daily Budget</label>

          <input
            type="number"
            value={daily}
            onChange={(e) => setDaily(Number(e.target.value))}
            className="w-full mt-1 bg-gray-800 border border-gray-700 rounded-md p-2 text-white"
          />
        </div>

        <div>
          <label className="text-xs text-gray-400">Monthly Budget</label>

          <input
            type="number"
            value={monthly}
            onChange={(e) => setMonthly(Number(e.target.value))}
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
