import type { Alert } from "../../types"

type Props = {
  alerts: Alert[]
}

function getAlertContainerStyle(severity: string) {
  if (severity === "critical") {
    return "alert-glow border-red-500/30 bg-red-500/10"
  }

  if (severity === "warning") {
    return "alert-glow border-yellow-500/30 bg-yellow-500/10"
  }

  return "border-gray-700 bg-gray-800/80"
}

function AlertBadge({ severity }: { severity: string }) {
  const normalizedSeverity = severity.toLowerCase()

  const badgeStyles =
    normalizedSeverity === "critical"
      ? "border-red-500/30 bg-red-500/15 text-red-300"
      : normalizedSeverity === "warning"
        ? "border-yellow-500/30 bg-yellow-500/15 text-yellow-300"
        : "border-gray-600 bg-gray-700/80 text-gray-300"

  return (
    <span
      className={`inline-flex items-center rounded-full border px-2.5 py-1 text-xs font-medium uppercase tracking-[0.2em] ${badgeStyles}`}
    >
      {severity}
    </span>
  )
}

export default function AlertList({ alerts }: Props) {
  return (
    <div className="rounded-2xl border border-gray-800 bg-gray-900 p-6 transition hover:border-gray-700">
      <h2 className="text-lg font-semibold mb-4">
        Alerts
      </h2>

      <div>
        {alerts.length === 0 && (
          <p className="text-gray-500 mt-4">No active alerts</p>
        )}

        {alerts.map((a) => (
          <div
            key={`${a.severity}-${a.message}`}
            className={`mb-3 rounded-xl border px-4 py-4 ${getAlertContainerStyle(a.severity)}`}
          >
            <div className="flex items-start justify-between gap-3">
              <p className="text-sm leading-6 text-gray-100">
                {a.message}
              </p>
              <AlertBadge severity={a.severity} />
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
