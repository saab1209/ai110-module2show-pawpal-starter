from dataclasses import dataclass, field
from typing import List, Optional, Tuple


@dataclass
class Task:
    """Represents a single pet care task such as feeding, walking, or medication."""
    title: str
    category: str
    time: str
    duration_minutes: int = 30
    priority: str = "Medium"
    frequency: str = "Once"
    completed: bool = False
    pet_name: str = ""

    def mark_complete(self) -> Optional["Task"]:
        """Mark task complete and return next recurring Task instance if applicable."""
        pass


@dataclass
class Pet:
    """Represents a pet owned by an Owner and its assigned care tasks."""
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Attach a task to this pet."""
        pass

    def remove_task(self, task_title: str) -> bool:
        """Remove a task by title."""
        pass

    def get_pending_tasks(self) -> List[Task]:
        """Return all incomplete tasks for this pet."""
        pass


@dataclass
class Owner:
    """Represents a pet owner who manages one or more pets."""
    name: str
    email: str = ""
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Register a pet under this owner."""
        pass

    def get_all_tasks(self) -> List[Task]:
        """Collect all tasks across every pet owned by this owner."""
        pass


class Scheduler:
    """Handles sorting, filtering, conflict detection, and task completion across an Owner's pets."""

    def __init__(self, owner: Owner):
        self.owner = owner

    def get_daily_schedule(self, sort_by: str = "time") -> List[Task]:
        """Return all tasks sorted by time or priority."""
        pass

    def filter_tasks(self, pet_name: Optional[str] = None, status: str = "all") -> List[Task]:
        """Filter tasks by pet name and completion status."""
        pass

    def detect_conflicts(self) -> List[Tuple[Task, Task]]:
        """Identify pairs of incomplete tasks whose scheduled times overlap."""
        pass

    def complete_task(self, pet_name: str, task_title: str) -> Optional[Task]:
        """Mark a task complete and auto-schedule the next occurrence if recurring."""
        pass

