from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Problem:
    """Represents a LeetCode problem with tracking metadata"""

    name: str
    url: str
    tag: str
    count: int = 0
    updated_datetime: Optional[str] = None
    revisit_date: Optional[str] = None

    @classmethod
    def from_dict(cls, name: str, data: dict) -> 'Problem':
        """Create a Problem instance from dictionary data"""
        return cls(
            name=name,
            url=data['url'],
            tag=data['tag'],
            count=data['count'],
            updated_datetime=data.get('updated_datetime'),
            revisit_date=data.get('revisit_date')
        )

    def to_dict(self) -> dict:
        """Convert Problem to dictionary format for JSON storage"""
        return {
            'url': self.url,
            'tag': self.tag,
            'count': self.count,
            'updated_datetime': self.updated_datetime or datetime.now().isoformat(),
            'revisit_date': self.revisit_date
        }
