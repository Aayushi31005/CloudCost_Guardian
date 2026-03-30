import { useState } from "react"
import { createUsage } from "../../services/api"

export default function UsageForm() {
  const [loading, setLoading] = useState(false)
  const [service, setService] = useState("ec2")

  const handleSubmit = async (e: any) => {
    e.preventDefault()

    setLoading(true)
    const usageAmount = Number.parseFloat(e.target.usage.value)

    const payload = {
      id: `u_${Date.now()}`,
      service: e.target.service.value,
      resource_type: "t3.micro",
      usage_amount: Number.isNaN(usageAmount) ? 0 : usageAmount,
      unit: "hour",
      timestamp: new Date().toISOString()
    }

    await createUsage(payload)

    setLoading(false)
    e.target.reset()
  }

  return (
    <div className="bg-gray-900 border border-gray-800 p-6 rounded-2xl">
      <h2 className="text-lg font-semibold mb-4">
        Simulate Usage
      </h2>

      <form onSubmit={handleSubmit} className="space-y-4">

        <select
          name="service"
          value={service}
          onChange={(e) => setService(e.target.value)}
          className="w-full bg-gray-800 border border-gray-700 p-2 rounded"
        >
          <option value="ec2">EC2</option>
          <option value="s3">S3</option>
        </select>

        <input
          name="usage"
          type="number"
          placeholder={service === "ec2" ? "Try 751+ to generate cost" : "Try more than 5 to generate cost"}
          className="w-full bg-gray-800 border border-gray-700 p-2 rounded"
          required
        />

        <p className="text-xs text-gray-500">
          Enter usage units (free tier: 750 for EC2)
        </p>

        <p className="text-xs text-gray-500">
          Costs apply only after free tier usage is exceeded.
        </p>

        <p className="text-sm text-gray-400 leading-6">
          {service === "ec2"
            ? "EC2 has a free tier of 750 hours. Usage below that still creates a history record, but billable cost stays at 0.0."
            : "S3 has a free tier of 5 units. Usage below that is recorded in history, but it will not increase cost."}
        </p>

        <button
          type="submit"
          className="w-full bg-blue-600 hover:bg-blue-500 p-2 rounded transition"
        >
          {loading ? "Submitting..." : "Add Usage"}
        </button>

      </form>
    </div>
  )
}
