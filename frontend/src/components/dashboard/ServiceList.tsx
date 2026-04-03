import type { ServiceCost } from "../../types"

type Props = {
  services: ServiceCost[]
}

export default function ServiceList({ services }: Props) {
  return (
    <div className="rounded-2xl border border-gray-800 bg-gray-900 p-6 transition hover:border-gray-700">
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
