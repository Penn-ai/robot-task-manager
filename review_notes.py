"""
Review Robot Program
机器人复习程序

This program reviews basic Python concepts through a simple robot task example.

本程序通过一个简单的机器人任务案例，复习 Python 基础知识。

Concepts reviewed:
- Variables
- Strings
- Numbers
- Lists
- If / else
- For loops
- Functions
- Return values
- f-string output
"""


# ==============================
# 1. Basic Robot Information
# 1. 机器人基础信息
# ==============================

robot_name = "TurtleBot3"

# Initial battery level
# 初始电量
battery = 60

# Battery consumed by each task
# 每个任务消耗的电量
battery_cost_per_task = 15

# Minimum battery level required to start a task
# 执行任务所需的最低电量
low_battery_threshold = 15

# Target points that the robot needs to visit
# 机器人需要前往的目标点
target_points = ["A", "B", "C", "D"]


# ==============================
# 2. Function Definitions
# 2. 函数定义
# ==============================

def print_program_header():
    """
    Print basic program information.
    输出程序基础信息。
    """
    print("Review Robot Program Started")
    print(f"Robot name: {robot_name}")
    print(f"Initial battery: {battery}%")
    print(f"Target points: {target_points}")
    print(f"Battery cost per task: {battery_cost_per_task}%")
    print(f"Low battery threshold: {low_battery_threshold}%")
    print("------------------------------")


def check_battery(battery_level, required_battery):
    """
    Check whether the robot has enough battery to complete the next task.

    检查机器人是否有足够电量完成下一个任务。

    Parameters:
    battery_level: current battery level
    required_battery: battery required for the next task

    参数：
    battery_level：当前电量
    required_battery：下一个任务所需电量

    Return:
    True if battery is enough.
    False if battery is not enough.

    返回：
    如果电量足够，返回 True。
    如果电量不足，返回 False。
    """
    if battery_level >= required_battery:
        return True
    else:
        return False


def move_to_point(point):
    """
    Simulate the robot moving to a target point.

    模拟机器人移动到目标点。
    """
    print(f"{robot_name} is moving to point {point}.")


def complete_task(point):
    """
    Print task completion information.

    输出任务完成信息。
    """
    print(f"Task at point {point} completed.")


def print_task_summary(total_tasks, completed_tasks, final_battery):
    """
    Print the final task summary.

    输出最终任务总结。
    """
    unfinished_tasks = total_tasks - completed_tasks

    print("------------------------------")
    print("Task Summary")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Unfinished tasks: {unfinished_tasks}")
    print(f"Final battery: {final_battery}%")
    print("Robot status: Task process finished.")


# ==============================
# 3. Main Program
# 3. 主程序
# ==============================

print_program_header()

# Count completed tasks
# 记录已完成任务数量
completed_tasks = 0

# Count total tasks
# 统计总任务数量
total_tasks = len(target_points)
-
# Execute tasks one by one
# 依次执行任务
for point in target_points:
    print(f"Next target point: {point}")

    # Check whether battery is enough before each task
    # 每次执行任务前先检查电量是否足够
    if check_battery(battery, battery_cost_per_task):
        print("Battery check passed.")

        move_to_point(point)

        # Update battery level after completing the task
        # 完成任务后更新电量
        battery = battery - battery_cost_per_task

        # Update completed task count
        # 更新已完成任务数量
        completed_tasks = completed_tasks + 1

        complete_task(point)

        print(f"Battery left: {battery}%")
    else:
        print("Battery check failed.")
        print(f"Battery left: {battery}%")
        print(f"Battery required: {battery_cost_per_task}%")
        print("Battery is not enough. Robot stops the task.")
        break

    print("------------------------------")


# ==============================
# 4. Final Summary
# 4. 最终总结
# ==============================

print_task_summary(total_tasks, completed_tasks, battery)