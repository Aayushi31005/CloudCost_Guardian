export default function PageHeader() {
  return (
    <div className="flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
      <div>
        <h1 className="text-4xl font-semibold tracking-tight text-white">
          CloudCost Guardian
        </h1>
        <p className="mt-2 text-gray-400">
          Real-time cloud cost monitoring and proactive spend alerts
        </p>
      </div>

      <span className="flex items-center text-sm text-green-400">
        <span className="mr-2 h-2 w-2 animate-pulse rounded-full bg-green-400" />
        Live Monitoring
      </span>
    </div>
  )
}
