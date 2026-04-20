"""
Recovery Agent
--------------
Retries or rolls back failed tasks.
"""

def recover(task, error):
    task["retries"] = task.get("retries", 0) + 1
    if task["retries"] > 3:
        raise RuntimeError("Task permanently failed")
    return task
