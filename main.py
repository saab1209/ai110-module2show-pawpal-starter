from pawpal_system import Owner, Pet, Scheduler, Task


def main() -> None:
    owner = Owner(name="Salmaa", email="salmaa@example.com")

    bella = Pet(name="Bella", species="Dog", age=3)
    milo = Pet(name="Milo", species="Cat", age=2)

    bella.add_task(Task(title="Morning Walk", category="Walk", time="08:00", duration_minutes=30, priority="High", frequency="Daily"))
    milo.add_task(Task(title="Breakfast & Thyroid Pill", category="Medication", time="08:15", duration_minutes=15, priority="High", frequency="Daily"))
    bella.add_task(Task(title="Evening Kibble", category="Feeding", time="18:00", duration_minutes=15, priority="Medium", frequency="Daily"))
    milo.add_task(Task(title="Play & Brush Session", category="Enrichment", time="19:30", duration_minutes=20, priority="Low", frequency="Once"))

    owner.add_pet(bella)
    owner.add_pet(milo)

    scheduler = Scheduler(owner)

    print(f"=== Today's Schedule for {owner.name} ===")
    for idx, task in enumerate(scheduler.get_daily_schedule(sort_by="time"), start=1):
        status = "Done" if task.completed else "Pending"
        print(f"{idx}. [{task.time}] {task.pet_name} - {task.title} ({task.category} | {task.priority} | {task.frequency}) [{status}]")

    conflicts = scheduler.detect_conflicts()
    print(f"\nDetected Time Conflicts: {len(conflicts)}")
    for task_a, task_b in conflicts:
        print(f"  - Overlap: '{task_a.title}' ({task_a.time}) overlaps with '{task_b.title}' ({task_b.time})")


if __name__ == "__main__":
    main()
