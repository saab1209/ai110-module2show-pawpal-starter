from pawpal_system import Owner, Pet, Scheduler, Task


def test_task_completion_updates_status():
    task = Task(title="Morning Walk", category="Walk", time="08:00", frequency="Once")
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_add_task_increases_pet_task_count():
    pet = Pet(name="Bella", species="Dog", age=3)
    assert len(pet.tasks) == 0
    pet.add_task(Task(title="Dinner", category="Feeding", time="18:00"))
    assert len(pet.tasks) == 1
    assert pet.tasks[0].pet_name == "Bella"


def test_scheduler_sorts_across_multiple_pets_and_detects_conflict():
    owner = Owner(name="Salmaa")
    dog = Pet(name="Bella", species="Dog", age=3)
    cat = Pet(name="Milo", species="Cat", age=2)

    dog.add_task(Task(title="Walk", category="Walk", time="08:00", duration_minutes=30, priority="Medium"))
    cat.add_task(Task(title="Meds", category="Medication", time="08:15", duration_minutes=15, priority="High"))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler(owner)
    schedule = scheduler.get_daily_schedule(sort_by="time")
    assert [t.title for t in schedule] == ["Walk", "Meds"]
    assert len(scheduler.detect_conflicts()) == 1


def test_recurring_task_creates_next_occurrence():
    owner = Owner(name="Salmaa")
    dog = Pet(name="Bella", species="Dog", age=3)
    dog.add_task(Task(title="Daily Vitamin", category="Medication", time="09:00", frequency="Daily"))
    owner.add_pet(dog)

    scheduler = Scheduler(owner)
    next_task = scheduler.complete_task("Bella", "Daily Vitamin")
    assert next_task is not None
    assert next_task.completed is False
    assert len(dog.tasks) == 2
