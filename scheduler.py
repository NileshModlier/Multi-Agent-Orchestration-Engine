"""
Task Scheduler
--------------
Coordinates execution order of agents.
"""

class Scheduler:
    def schedule(self, tasks):
        return sorted(tasks, key=lambda t: t.get("priority", 0), reverse=True)
