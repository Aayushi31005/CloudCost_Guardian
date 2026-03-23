class AlertRepository:

    def __init__(self, alert_engine):
        self.alert_engine = alert_engine

    def get_active_alerts(self):

        return [
            {
                "severity": "unknown",
                "message": key
            }
            for key in self.alert_engine.sent_alerts
        ]