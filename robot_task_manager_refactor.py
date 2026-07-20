"""
Robot Task Manager - Refactored Version

This program simulates a robot completing multiple target-point tasks.
It checks battery level before each task, updates task status, and prints a final task summary.

机器人任务管理器 - 结构优化版

这个程序模拟一个机器人完成多个目标点任务。
它会在每个任务前检查电量，更新任务状态，并输出最终任务总结。
"""


# ==============================
# 1. Robot Basic Information
# 1. 机器人基础信息
# ==============================

robot_name = "TurtleBot3"

# Initial battery level
# 初始电量
battery = 60

# Each target point has a different battery consumption
# 每个目标点有不同的电量消耗
tasks = {
    "A": 10,
    "B": 15,
    "C": 20,
    "D": 25
}


# ==============================
# 2. Function Definitions
# 2. 函数定义
# ==============================

def print_header(robot_name, battery, total_tasks):
    """
    Print the basic information of the program.

    输出程序的基础信息。
    """
    print("Robot Task Manager Started")
    print(f"Robot name: {robot_name}")
    print(f"Initial battery: {battery}%")
    print(f"Total tasks: {total_tasks}")
    print("------------------------------")


def check_battery(battery_level, required_battery):
    """
    Check whether the robot has enough battery for the next task.

    检查机器人是否有足够电量执行下一个任务。

    Parameters:
    battery_level: current battery level
    required_battery: battery required by the next task

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


def move_to_point(robot_name, point, battery_cost):
    """
    Simulate the robot moving to a target point.

    模拟机器人移动到目标点。
    """
    print(f"{robot_name} is moving to point {point}.")
    print(f"This task will consume {battery_cost}% battery.")


def complete_task(point, battery_level):
    """
    Print task completion information.

    输出任务完成信息。
    """
    print(f"Task at point {point} completed.")
    print(f"Battery left: {battery_level}%")


def stop_task(point, battery_level, required_battery):
    """
    Print task stop information when battery is not enough.

    当电量不足时，输出任务停止信息。
    """
    print(f"Battery is not enough for point {point}.")
    print(f"Battery left: {battery_level}%")
    print(f"Battery required: {required_battery}%")
    print("Robot stops the task.")


def print_summary(total_tasks, completed_tasks, final_battery):
    """
    Print the final task summary.

    输出最终任务总结。
    """
    unfinished_tasks = total_tasks - completed_tasks
    completion_rate = completed_tasks / total_tasks * 100

    print("------------------------------")
    print("Task Summary")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Unfinished tasks: {unfinished_tasks}")
    print(f"Final battery: {final_battery}%")
    print(f"Task completion rate: {completion_rate:.1f}%")
    print("Robot Task Manager Finished")


# ==============================
# 3. Main Program
# 3. 主程序
# ==============================

total_tasks = len(tasks)
completed_tasks = 0

print_header(robot_name, battery, total_tasks)

for point, battery_cost in tasks.items():
    print(f"Next target point: {point}")

    if check_battery(battery, battery_cost):
        move_to_point(robot_name, point, battery_cost)

        # Update battery after task completion
        # 任务完成后更新电量
        battery = battery - battery_cost

        # Update completed task count
        # 更新已完成任务数量
        completed_tasks = completed_tasks + 1

        complete_task(point, battery)
    else:
        stop_task(point, battery, battery_cost)
        break

    print("------------------------------")


# ==============================
# 4. Final Summary
# 4. 最终总结
# ==============================

print_summary(total_tasks, completed_tasks, battery)