import logging
from typing import Optional

from app.models.policy import PolicyViolation
from app.models.alert import Alert

logger = logging.getLogger(__name__)

class AlertEngine:
    def __init__(self):
        self.sent_alerts = set()
        self.active_alerts: dict[str, Alert] = {}

    def emit(self, violation: PolicyViolation) -> Optional[Alert]:
        key = (
            f"{violation.policy_name}:{violation.stage}:{violation.window}:"
            f"{violation.period_start}:{violation.service}"
        )

        if key in self.sent_alerts:
            logger.info("alert_deduplicated", extra={"key": key})
            return None

        policy_label = violation.policy_name.replace("_", " ").title()

        if violation.stage == "projected":
            message = (
                f"{policy_label}: your spend is close to the limit. "
                f"At the current pace, the next usage spike could push it from "
                f"{violation.current_cost:.2f} to {violation.projected_cost:.2f}, over the "
                f"{violation.threshold:.2f} limit."
            )
        elif violation.stage == "approaching":
            message = (
                f"{policy_label}: your spend has reached {violation.current_cost:.2f} out of "
                f"{violation.threshold:.2f}. Consider reducing usage now to avoid an unexpected bill."
            )
        else:
            message = (
                f"{policy_label}: your spend is already above the limit at "
                f"{violation.current_cost:.2f} against {violation.threshold:.2f}."
            )

        alert = Alert(
            key=key,
            severity=violation.severity,
            message=message,
        )

        self.sent_alerts.add(key)
        self.active_alerts[key] = alert

        logger.error(
            "alert_emitted",
            extra=alert.model_dump(),
        )

        return alert
