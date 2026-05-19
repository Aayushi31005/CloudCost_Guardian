export interface Summary {
  daily_total: number
  daily_ec2_total: number
  daily_s3_total: number
  weekly_total: number
  weekly_ec2_total: number
  weekly_s3_total: number
  monthly_total: number
  monthly_ec2_total: number
  monthly_s3_total: number
}

export interface ServiceCost {
  service: string
  monthly_cost: number
}

export interface Alert {
  key?: string
  severity: string
  message: string
}

export interface CostHistoryPoint {
  period_start: string
  period_label: string
  cost: number
}

export interface BudgetConfig {
  service: "ec2" | "s3"
  daily_limit: number
  monthly_limit: number
}
