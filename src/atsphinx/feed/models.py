"""Data-models for feed.

This modue defines brige classes from doctree to feed.

Refs
----

* https://www.rfc-editor.org/rfc/rfc4287
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class Entry:
    """Data for entry in Atom feed."""

    title: str
    link: str
    updated: datetime
    summary: str


@dataclass
class Feed:
    """Data for Atom feed."""

    title: str
    link: str
    author: str
    entries: List[Entry]

    @property
    def updated(self) -> Optional[datetime]:
        """Value of updated time for feed itself."""
        if not self.entries:
            return None
        return max([e.updated for e in self.entries])
