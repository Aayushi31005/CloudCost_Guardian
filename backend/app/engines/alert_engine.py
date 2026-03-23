import logging
from typing import Optional

from app.models.policy import PolicyViolation
from app.models.alert import Alert

logger = logging.getLogger(__name__)

class AlertEngine:
    def __init__(self):
        self.sent_alerts = set()

    def emit(self, violation: PolicyViolation) -> Optional[Alert]:
        key = f"{violation.policy_name}:{violation.window}:{violation.service}"

        if key in self.sent_alerts:
            logger.info("alert_deduplicated", extra={"key": key})
            return None

        alert = Alert(
            key=key,
            severity=violation.severity,
            alert_message=(
                f"{violation.policy_name} exceeded: "
                f"{violation.current_cost} > {violation.threshold}"
            ),
        )

        self.sent_alerts.add(key)

        logger.error(
            "alert_emitted",
            extra=alert.model_dump(),
        )

        return alert
