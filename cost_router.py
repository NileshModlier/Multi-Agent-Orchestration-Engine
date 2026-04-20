"""
Cost-Aware Routing
-----------------
Routes tasks based on budget constraints.
"""

def route(tasks, max_cost):
    return [t for t in tasks if t.get("cost", 0) <= max_cost]
