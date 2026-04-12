class AlertRepository:

    def __init__(self, alert_engine):
        self.alert_engine = alert_engine

    def get_active_alerts(self):
        return [
            alert.model_dump()
            for alert in self.alert_engine.active_alerts.values()
        ]
