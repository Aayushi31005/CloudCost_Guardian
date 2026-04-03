import { useEffect, useState } from "react"

type BootScreenProps = {
  onFinish?: () => void
}

const steps = [
  "Loading pricing rules",
  "Starting usage ingestion simulator",
  "Initializing cost aggregation engine",
  "Starting alert pipeline",
]

export default function BootScreen({ onFinish }: BootScreenProps) {
  const [visibleSteps, setVisibleSteps] = useState<string[]>([])

  useEffect(() => {
    let index = 0

    const interval = setInterval(() => {
      if (index >= steps.length) {
        clearInterval(interval)
        window.setTimeout(() => onFinish?.(), 400)
        return
      }

      setVisibleSteps((prev) => [...prev, steps[index]])
      index += 1
    }, 350)

    return () => clearInterval(interval)
  }, [onFinish])

  return (
    <div className="h-screen bg-black text-green-400 font-mono flex flex-col justify-center items-center animate-pulse">
      <div className="w-full max-w-2xl rounded-2xl border border-gray-800 bg-gray-900/80 p-6 shadow-2xl shadow-blue-950/20 backdrop-blur">
        <h1 className="text-3xl font-semibold tracking-tight text-white">
          CloudCost Guardian
        </h1>
        <p className="mt-2 text-sm text-gray-400">
          Initializing monitoring services...
        </p>

        <div className="mt-6 space-y-3">
          {visibleSteps.map((step) => (
            <div
              key={step}
              className="animate-fade rounded-xl border border-gray-800 bg-gray-950/80 px-4 py-3 text-sm text-gray-200"
            >
              {step}
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
