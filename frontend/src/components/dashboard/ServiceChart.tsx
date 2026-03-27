import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts"

import type { ServiceCost } from "../../types"

type Props = {
  services: ServiceCost[]
}

export default function ServiceChart({ services }: Props) {
  return (
    <div className="bg-gray-900 border border-gray-800 p-6 rounded-2xl">
      <h2 className="text-lg font-semibold mb-3">Service Cost Distribution</h2>

      <div className="h-[220px]">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={services}>
            <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
            <XAxis dataKey="service" stroke="#9CA3AF" />
            <YAxis stroke="#9CA3AF" />
            <Tooltip
              contentStyle={{
                backgroundColor: "#111827",
                border: "1px solid #374151",
                borderRadius: "8px",
                color: "#E5E7EB"
              }}
            />
            <Bar
              dataKey="monthly_cost"
              fill="#3B82F6"   // Tailwind blue-500
              radius={[6, 6, 0, 0]}
            />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}
