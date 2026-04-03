import { Component, type ReactNode, useState } from "react"
import BootScreen from "./components/BootScreen"
import Dashboard from "./pages/Dashboard"

type AppErrorBoundaryProps = {
  children: ReactNode
}

type AppErrorBoundaryState = {
  hasError: boolean
}

class AppErrorBoundary extends Component<AppErrorBoundaryProps, AppErrorBoundaryState> {
  state: AppErrorBoundaryState = {
    hasError: false,
  }

  static getDerivedStateFromError() {
    return { hasError: true }
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="flex min-h-screen items-center justify-center bg-gray-950 px-6 text-white">
          <div className="w-full max-w-xl rounded-2xl border border-red-500/30 bg-gray-900 p-6 text-center">
            <h1 className="text-2xl font-semibold">Dashboard failed to load</h1>
            <p className="mt-3 text-sm text-gray-400">
              A runtime error occurred while rendering the dashboard. Refresh the page to try again.
            </p>
          </div>
        </div>
      )
    }

    return this.props.children
  }
}

function App() {
  const [ready, setReady] = useState(false)

  if (!ready) {
    return <BootScreen onFinish={() => setReady(true)} />
  }

  return (
    <AppErrorBoundary>
      <Dashboard />
    </AppErrorBoundary>
  )
}

export default App
