from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    id: int
    title: str
    description: Optional[str]
    completed: bool