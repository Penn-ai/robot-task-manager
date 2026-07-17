# Robot Task Manager
# This program simulates a robot completing tasks and calculates task statistics.

robot_name = "TurtleBot3"

# Initial battery level
battery = 60

# Each target point has a different battery consumption
tasks = {
    "A": 10,
    "B": 15,
    "C": 20,
    "D": 25
}

# Task statistics
total_tasks = len(tasks)
completed_tasks = 0


def check_battery(battery_level, required_battery):
    """
    Check whether the robot has enough battery for the next task.
    """
    if battery_level >= required_battery:
        return True
    else:
        return False


def move_to_point(point, battery_cost):
    """
    Simulate the robot moving to a target point.
    """
    print(f"{robot_name} is moving to point {point}.")
    print(f"This task will consume {battery_cost}% battery.")


print("Robot Task Manager Started")
print(f"Robot name: {robot_name}")
print(f"Initial battery: {battery}%")
print(f"Total tasks: {total_tasks}")
print("------------------------------")

for point, battery_cost in tasks.items():
    print(f"Next target point: {point}")

    if check_battery(battery, battery_cost):
        move_to_point(point, battery_cost)

        battery = battery - battery_cost
        completed_tasks = completed_tasks + 1

        print(f"Task at point {point} completed.")
        print(f"Battery left: {battery}%")
    else:
        print(f"Battery is not enough for point {point}.")
        print("Robot stops the task.")
        break

    print("------------------------------")

# Calculate final statistics
unfinished_tasks = total_tasks - completed_tasks
completion_rate = completed_tasks / total_tasks * 100

print("------------------------------")
print("Task Summary")
print(f"Total tasks: {total_tasks}")
print(f"Completed tasks: {completed_tasks}")
print(f"Unfinished tasks: {unfinished_tasks}")
print(f"Final battery: {battery}%")
print(f"Task completion rate: {completion_rate:.1f}%")
print("Robot Task Manager Finished")