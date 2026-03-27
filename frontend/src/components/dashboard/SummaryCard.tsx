type Props = {
  title: string
  value: number
  variant?: "primary" | "success"
}

export default function SummaryCard({ title, value, variant = "primary" }: Props) {

  const color =
    variant === "primary"
      ? "text-blue-400"
      : "text-green-400"

  return (
    <div className="bg-gray-900 border border-gray-800 p-6 rounded-2xl">
      <p className="text-gray-400 text-sm">{title}</p>

      <h2 className={`text-3xl font-semibold mt-2 ${color}`}>
        ${value}
      </h2>
    </div>
  )
}