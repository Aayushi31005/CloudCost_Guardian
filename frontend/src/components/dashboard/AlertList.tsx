import type { Alert } from "../../types"

type Props = {
  alerts: Alert[]
}

function getAlertStyle(severity: string) {
  if (severity === "critical") {
    return "bg-red-500/20 border-red-500/40 text-red-400"
  }

  if (severity === "warning") {
    return "bg-yellow-500/20 border-yellow-500/40 text-yellow-400"
  }

  return "bg-gray-700 text-gray-300"
}

export default function AlertList({ alerts }: Props) {
  return (
    <div className="bg-gray-900 border border-gray-800 p-6 rounded-2xl">
      <h2 className="text-lg font-semibold mb-4">
        Alerts
      </h2>

      <div>
        {alerts.length === 0 && (
          <p className="text-gray-500 mt-4">No active alerts</p>
        )}

        {alerts.map((a, i) => (
          <div
            key={i}
            className={`px-4 py-3 rounded-lg mb-3 border ${getAlertStyle(a.severity)}`}
          >
            {a.message}
          </div>
        ))}
      </div>
    </div>
  )
}
