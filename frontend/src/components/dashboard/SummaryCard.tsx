import { useEffect, useRef, useState } from "react"

type Props = {
  title: string
  value: number
  variant?: "primary" | "success"
}

export default function SummaryCard({ title, value, variant = "primary" }: Props) {
  const [displayValue, setDisplayValue] = useState(0)
  const previousValueRef = useRef(0)

  useEffect(() => {
    const duration = 600
    const startValue = previousValueRef.current
    const startTime = performance.now()

    let frameId = 0

    const animate = (currentTime: number) => {
      const progress = Math.min((currentTime - startTime) / duration, 1)
      const nextValue = startValue + (value - startValue) * progress

      setDisplayValue(nextValue)

      if (progress < 1) {
        frameId = window.requestAnimationFrame(animate)
      } else {
        previousValueRef.current = value
      }
    }

    frameId = window.requestAnimationFrame(animate)

    return () => window.cancelAnimationFrame(frameId)
  }, [value])

  const color =
    variant === "primary"
      ? "text-blue-400"
      : "text-green-400"

  const formattedValue = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 0,
  }).format(displayValue)

  return (
    <div className="rounded-2xl border border-gray-800 bg-gray-900 p-5 transition hover:border-gray-700 sm:p-6">
      <p className="text-xs font-medium uppercase tracking-[0.24em] text-gray-400">
        {title}
      </p>

      <h2 className={`mt-3 text-4xl font-semibold leading-none sm:text-5xl ${color}`}>
        {formattedValue}
      </h2>
    </div>
  )
}
