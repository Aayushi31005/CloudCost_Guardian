import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from "recharts"

import type { CostHistoryPoint } from "../../types"

type Props = {
  data: CostHistoryPoint[]
  granularity: "daily" | "weekly" | "monthly"
  onGranularityChange: (granularity: "daily" | "weekly" | "monthly") => void
}

const options: Array<"daily" | "weekly" | "monthly"> = ["daily", "weekly", "monthly"]

export default function TrendChart({ data, granularity, onGranularityChange }: Props) {
  return (
    <div className="rounded-xl border border-gray-800 bg-gray-900 p-5 transition hover:border-gray-700">
      <div className="mb-4 flex items-center justify-between">
        <h2 className="text-sm uppercase tracking-[0.2em] text-gray-400">
          Cost Trend
        </h2>
        <div className="flex items-center gap-2">
          {options.map((option) => (
            <button
              key={option}
              type="button"
              onClick={() => onGranularityChange(option)}
              className={`rounded-full px-3 py-1 text-xs uppercase tracking-[0.18em] transition ${
                granularity === option
                  ? "bg-blue-500/20 text-blue-300"
                  : "bg-gray-800 text-gray-400 hover:bg-gray-700 hover:text-gray-200"
              }`}
            >
              {option}
            </button>
          ))}
        </div>
      </div>

      <div className="h-[240px]">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
            <CartesianGrid stroke="#374151" strokeDasharray="3 3" />

            <XAxis dataKey="period_label" stroke="#9CA3AF" />
            <YAxis stroke="#9CA3AF" />

            <Tooltip
              contentStyle={{
                backgroundColor: "#111827",
                border: "1px solid #374151",
                borderRadius: "8px",
                color: "#E5E7EB"
              }}
            />

            <Line
              type="monotone"
              dataKey="cost"
              stroke="#10B981"
              strokeWidth={2}
              dot={{ r: 3 }}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}
