from datetime import datetime, timedelta
from typing import Optional


class SpacedRepetition:
    """Manages spaced repetition scheduling for problem revisits"""

    # Spaced repetition intervals in days
    INTERVALS = [1, 3, 7, 14, 30, 60, 90]

    @classmethod
    def get_next_revisit_date(cls, count: int) -> str:
        """
        Calculate the next revisit date based on completion count.

        Args:
            count: Number of times the problem has been completed

        Returns:
            ISO format date string for the next revisit
        """
        if count < len(cls.INTERVALS):
            days = cls.INTERVALS[count]
        else:
            days = cls.INTERVALS[-1]  # Cap at max interval

        return (datetime.now().date() + timedelta(days=days)).isoformat()

    @classmethod
    def is_due_for_review(cls, revisit_date: Optional[str]) -> bool:
        """
        Check if a problem is due for review.

        Args:
            revisit_date: ISO format date string or None

        Returns:
            True if the problem should be reviewed today
        """
        if not revisit_date:
            return False

        return datetime.strptime(revisit_date, "%Y-%m-%d").date() <= datetime.now().date()
