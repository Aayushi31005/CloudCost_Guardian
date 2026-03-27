import type { ServiceCost } from "../../types"

type Props = {
  services: ServiceCost[]
}

export default function ServiceList({ services }: Props) {
  return (
    <div className="bg-gray-900 border border-gray-800 p-6 rounded-2xl">
      <h2 className="text-lg font-semibold mb-4">
        Service Breakdown
      </h2>

      {services.map((s) => (
        <div
          key={s.service}
          className="flex justify-between py-2 border-b border-gray-800 last:border-none"
        >
          <span className="text-gray-300">{s.service}</span>
          <span className="font-medium">${s.monthly_cost}</span>
        </div>
      ))}
    </div>
  )
}
