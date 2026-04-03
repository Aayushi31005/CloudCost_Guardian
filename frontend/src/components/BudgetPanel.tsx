import { useState, useEffect } from "react"
import axios from "axios"

export default function BudgetPanel() {

  const [daily, setDaily] = useState(0)
  const [monthly, setMonthly] = useState(0)

  useEffect(() => {
    axios.get("/budget").then(res => {
      setDaily(res.data.daily_limit)
      setMonthly(res.data.monthly_limit)
    })
  }, [])

  const saveBudget = async () => {
    await axios.post("/budget", {
      daily_limit: daily,
      monthly_limit: monthly
    })
  }

  return (
    <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">

      <h2 className="text-sm text-gray-400 uppercase tracking-wide mb-4">
        Budget Configuration
      </h2>

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
          onClick={saveBudget}
          className="w-full mt-3 bg-blue-600 hover:bg-blue-500 text-white py-2 rounded-md"
        >
          Save Budget
        </button>

      </div>

    </div>
  )
}
