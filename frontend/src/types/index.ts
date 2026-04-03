export interface Summary {
  monthly_total: number
  weekly_total: number
  daily_total: number
}

export interface ServiceCost {
  service: string
  monthly_cost: number
}

export interface Alert {
  severity: string
  message: string
}

export interface CostHistoryPoint {
  period_start: string
  period_label: string
  cost: number
}

export interface BudgetConfig {
  daily_limit: number
  monthly_limit: number
}
