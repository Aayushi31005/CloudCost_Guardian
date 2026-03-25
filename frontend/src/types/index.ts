export interface Summary {
  monthly_total: number
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