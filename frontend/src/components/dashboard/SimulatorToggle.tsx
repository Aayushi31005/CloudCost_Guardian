import { useEffect, useState } from "react"
import {
  getSimulatorStatus,
  startSimulator,
  stopSimulator,
} from "../../services/api"

export default function SimulatorToggle() {
  const [running, setRunning] = useState(false)

  useEffect(() => {
    getSimulatorStatus().then((res) => setRunning(res.running))
  }, [])

  const toggle = async () => {
    if (running) {
      await stopSimulator()
      setRunning(false)
    } else {
      await startSimulator()
      setRunning(true)
    }
  }

  return (
    <div className="flex items-center justify-between rounded-xl border border-gray-800 bg-gray-900 p-5 transition hover:border-gray-700">
      <div>
        <p className="text-sm text-gray-400">Simulator Mode</p>
        <p className="text-white font-medium">
          {running ? "Running" : "Stopped"}
        </p>
      </div>

      <button
        onClick={toggle}
        className={`rounded-md px-4 py-2 text-sm font-medium transition ${
          running
            ? "bg-red-600 hover:bg-red-500"
            : "bg-green-600 hover:bg-green-500"
        }`}
      >
        {running ? "Stop" : "Start"}
      </button>
    </div>
  )
}
