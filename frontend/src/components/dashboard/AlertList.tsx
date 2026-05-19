import { useEffect, useRef } from "react"
import toast from "react-hot-toast"
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

function getToastStyle(severity: string) {
  if (severity === "critical") {
    return "border-red-500 bg-red-500/10"
  }

  if (severity === "warning") {
    return "border-yellow-500 bg-yellow-500/10"
  }

  return "border-gray-700 bg-gray-900"
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
  const prevAlertCount = useRef(0)

  useEffect(() => {
    if (alerts.length > prevAlertCount.current) {
      const newest = alerts[0]

      toast.custom(() => (
        <div className={`rounded-lg border p-4 text-white shadow-lg ${getToastStyle(newest.severity)}`}>
          <div className="font-semibold">Cloud Cost Alert</div>
          <div className="mt-1 text-sm">{newest.message}</div>
        </div>
      ))
    }

    prevAlertCount.current = alerts.length
  }, [alerts])

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
