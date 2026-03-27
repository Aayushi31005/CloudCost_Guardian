import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from "recharts"

import type { DailyCost } from "../../types"

type Props = {
  data: DailyCost[]
}

export default function TrendChart({ data }: Props) {
  return (
    <div className="bg-gray-900 border border-gray-800 p-6 rounded-2xl">
      <h2 className="text-lg font-semibold mb-4">
        Cost Trend (Daily)
      </h2>

      <div className="h-[250px]">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
            <CartesianGrid stroke="#374151" strokeDasharray="3 3" />

            <XAxis dataKey="date" stroke="#9CA3AF" />
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
