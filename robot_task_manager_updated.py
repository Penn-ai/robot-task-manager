# """
# Robot Task Manager - Refactored Version

# This program simulates a robot completing multiple target-point tasks.
# It checks battery level before each task, updates task status, and prints a final task summary.

# 机器人任务管理器 - 结构优化版

# 这个程序模拟一个机器人完成多个目标点任务。
# 它会在每个任务前检查电量，更新任务状态，并输出最终任务总结。
# """


# # ==============================
# # 1. Robot Basic Information
# # 1. 机器人基础信息
# # ==============================

# robot_name = "TurtleBot3"

# # Initial battery level
# # 初始电量
# battery = 60

# # Each target point has a different battery consumption
# # 每个目标点有不同的电量消耗
# tasks = {
#     "A": 10,
#     "B": 15,
#     "C": 20,
#     "D": 25
# }


# # ==============================
# # 2. Function Definitions
# # 2. 函数定义
# # ==============================

# def print_header(robot_name, battery, total_tasks):
#     """
#     Print the basic information of the program.

#     输出程序的基础信息。
#     """
#     print("Robot Task Manager Started")
#     print(f"Robot name: {robot_name}")
#     print(f"Initial battery: {battery}%")
#     print(f"Total tasks: {total_tasks}")
#     print("------------------------------")


# def check_battery(battery_level, required_battery):
#     """
#     Check whether the robot has enough battery for the next task.

#     检查机器人是否有足够电量执行下一个任务。

#     Parameters:
#     battery_level: current battery level
#     required_battery: battery required by the next task

#     参数：
#     battery_level：当前电量
#     required_battery：下一个任务所需电量

#     Return:
#     True if battery is enough.
#     False if battery is not enough.

#     返回：
#     如果电量足够，返回 True。
#     如果电量不足，返回 False。
#     """
#     if battery_level >= required_battery:
#         return True
#     else:
#         return False


# def move_to_point(robot_name, point, battery_cost):
#     """
#     Simulate the robot moving to a target point.

#     模拟机器人移动到目标点。
#     """
#     print(f"{robot_name} is moving to point {point}.")
#     print(f"This task will consume {battery_cost}% battery.")


# def complete_task(point, battery_level):
#     """
#     Print task completion information.

#     输出任务完成信息。
#     """
#     print(f"Task at point {point} completed.")
#     print(f"Battery left: {battery_level}%")


# def stop_task(point, battery_level, required_battery):
#     """
#     Print task stop information when battery is not enough.

#     当电量不足时，输出任务停止信息。
#     """
#     print(f"Battery is not enough for point {point}.")
#     print(f"Battery left: {battery_level}%")
#     print(f"Battery required: {required_battery}%")
#     print("Robot stops the task.")


# def print_summary(total_tasks, completed_tasks, final_battery):
#     """
#     Print the final task summary.

#     输出最终任务总结。
#     """
#     unfinished_tasks = total_tasks - completed_tasks
#     completion_rate = completed_tasks / total_tasks * 100

#     print("------------------------------")
#     print("Task Summary")
#     print(f"Total tasks: {total_tasks}")
#     print(f"Completed tasks: {completed_tasks}")
#     print(f"Unfinished tasks: {unfinished_tasks}")
#     print(f"Final battery: {final_battery}%")
#     print(f"Task completion rate: {completion_rate:.1f}%")
#     print("Robot Task Manager Finished")


# # ==============================
# # 3. Main Program
# # 3. 主程序
# # ==============================

# total_tasks = len(tasks)
# completed_tasks = 0

# print_header(robot_name, battery, total_tasks)

# for point, battery_cost in tasks.items():
#     print(f"Next target point: {point}")

#     if check_battery(battery, battery_cost):
#         move_to_point(robot_name, point, battery_cost)

#         # Update battery after task completion
#         # 任务完成后更新电量
#         battery = battery - battery_cost

#         # Update completed task count
#         # 更新已完成任务数量
#         completed_tasks = completed_tasks + 1

#         complete_task(point, battery)
#     else:
#         stop_task(point, battery, battery_cost)
#         break

#     print("------------------------------")


# # ==============================
# # 4. Final Summary
# # 4. 最终总结
# # ==============================

# print_summary(total_tasks, completed_tasks, battery)

# """
# Robot Task Manager - Priority Version

# This program simulates a robot completing multiple target-point tasks.
# It supports task priority, checks battery level before each task,
# updates task status, and prints a final task summary.

# 机器人任务管理器 - 任务优先级版本

# 这个程序模拟一个机器人完成多个目标点任务。
# 它支持任务优先级，会在每个任务前检查电量，
# 更新任务状态，并输出最终任务总结。
# """


# # ==============================
# # 1. Robot Basic Information
# # 1. 机器人基础信息
# # ==============================

# robot_name = "TurtleBot3"

# # Initial battery level
# # 初始电量
# battery = 60

# # Task list
# # 任务列表
# #
# # Each task contains:
# # point: target point
# # battery_cost: battery required by this task
# # priority: task priority
# #
# # 每个任务包括：
# # point：目标点
# # battery_cost：任务消耗电量
# # priority：任务优先级
# #
# # Rule:
# # Higher priority number means higher priority.
# #
# # 规则：
# # priority 数字越大，任务优先级越高。
# tasks = [
#     {"point": "A", "battery_cost": 10, "priority": 2},
#     {"point": "B", "battery_cost": 15, "priority": 4},
#     {"point": "C", "battery_cost": 20, "priority": 1},
#     {"point": "D", "battery_cost": 25, "priority": 3}
# ]


# # ==============================
# # 2. Function Definitions
# # 2. 函数定义
# # ==============================

# def print_header(robot_name, battery, total_tasks):
#     """
#     Print the basic information of the program.

#     输出程序的基础信息。
#     """
#     print("Robot Task Manager Started")
#     print(f"Robot name: {robot_name}")
#     print(f"Initial battery: {battery}%")
#     print(f"Total tasks: {total_tasks}")
#     print("Priority rule: higher number means higher priority")
#     print("------------------------------")


# def sort_tasks_by_priority(task_list):
#     """
#     Sort tasks by priority from high to low.

#     按照任务优先级从高到低排序。

#     Parameters:
#     task_list: original task list

#     参数：
#     task_list：原始任务列表

#     Return:
#     A new task list sorted by priority.

#     返回：
#     一个按照优先级排序后的新任务列表。
#     """
#     sorted_tasks = sorted(
#         task_list,
#         key=lambda task: task["priority"],
#         reverse=True
#     )

#     return sorted_tasks

 
# def check_battery(battery_level, required_battery):
#     """
#     Check whether the robot has enough battery for the next task.

#     检查机器人是否有足够电量执行下一个任务。
#     """
#     if battery_level >= required_battery:
#         return True
#     else:
#         return False


# def print_task_info(task):
#     """
#     Print current task information.

#     输出当前任务信息。
#     """
#     print(f"Next target point: {task['point']}")
#     print(f"Task priority: {task['priority']}")
#     print(f"Battery required: {task['battery_cost']}%")


# def move_to_point(robot_name, point, battery_cost):
#     """
#     Simulate the robot moving to a target point.

#     模拟机器人移动到目标点。
#     """
#     print(f"{robot_name} is moving to point {point}.")
#     print(f"This task will consume {battery_cost}% battery.")


# def complete_task(point, battery_level):
#     """
#     Print task completion information.

#     输出任务完成信息。
#     """
#     print(f"Task at point {point} completed.")
#     print(f"Battery left: {battery_level}%")


# def stop_task(point, battery_level, required_battery):
#     """
#     Print task stop information when battery is not enough.

#     当电量不足时，输出任务停止信息。
#     """
#     print(f"Battery is not enough for point {point}.")
#     print(f"Battery left: {battery_level}%")
#     print(f"Battery required: {required_battery}%")
#     print("Robot stops the task.")


# def print_summary(total_tasks, completed_tasks, final_battery):
#     """
#     Print the final task summary.

#     输出最终任务总结。
#     """
#     unfinished_tasks = total_tasks - completed_tasks
#     completion_rate = completed_tasks / total_tasks * 100

#     print("------------------------------")
#     print("Task Summary")
#     print(f"Total tasks: {total_tasks}")
#     print(f"Completed tasks: {completed_tasks}")
#     print(f"Unfinished tasks: {unfinished_tasks}")
#     print(f"Final battery: {final_battery}%")
#     print(f"Task completion rate: {completion_rate:.1f}%")
#     print("Robot Task Manager Finished")


# # ==============================
# # 3. Main Program
# # 3. 主程序
# # ==============================

# total_tasks = len(tasks)
# completed_tasks = 0

# print_header(robot_name, battery, total_tasks)

# # Sort tasks by priority before execution
# # 执行任务前，先按照优先级排序
# sorted_tasks = sort_tasks_by_priority(tasks)

# print("Task execution order after priority sorting:")
# print("按优先级排序后的任务执行顺序：")

# for task in sorted_tasks:
#     print(f"Point {task['point']} - Priority {task['priority']}")

# print("------------------------------")

# # Execute tasks one by one according to priority
# # 按照优先级依次执行任务
# for task in sorted_tasks:
#     point = task["point"]
#     battery_cost = task["battery_cost"]
#     priority = task["priority"]

#     print_task_info(task)

#     if check_battery(battery, battery_cost):
#         move_to_point(robot_name, point, battery_cost)

#         # Update battery after task completion
#         # 任务完成后更新电量
#         battery = battery - battery_cost

#         # Update completed task count
#         # 更新已完成任务数量
#         completed_tasks = completed_tasks + 1

#         complete_task(point, battery)
#     else:
#         stop_task(point, battery, battery_cost)
#         break

#     print("------------------------------")


# # ==============================
# # 4. Final Summary
# # 4. 最终总结
# # ==============================

# print_summary(total_tasks, completed_tasks, battery)

"""
Robot Task Manager - Task Status Version

This program simulates a robot completing multiple target-point tasks.
It supports task priority and task status statistics.

机器人任务管理器 - 任务状态统计版本

这个程序模拟一个机器人完成多个目标点任务。
它支持任务优先级，并统计任务完成状态。
"""


# ==============================
# 1. Robot Basic Information
# 1. 机器人基础信息
# ==============================

robot_name = "TurtleBot3"

# Initial battery level
# 初始电量
battery = 60

# Task list
# 任务列表
#
# Each task contains:
# point: target point
# battery_cost: battery required by this task
# priority: task priority
# status: task completion status
#
# 每个任务包括：
# point：目标点
# battery_cost：任务消耗电量
# priority：任务优先级
# status：任务完成状态
#
# Rule:
# Higher priority number means higher priority.
#
# 规则：
# priority 数字越大，任务优先级越高。
#
# Initial status:
# All tasks are unfinished at the beginning.
#
# 初始状态：
# 所有任务一开始都是 unfinished，表示未完成。
tasks = [
    {"point": "A", "battery_cost": 10, "priority": 2, "status": "unfinished"},
    {"point": "B", "battery_cost": 15, "priority": 4, "status": "unfinished"},
    {"point": "C", "battery_cost": 20, "priority": 1, "status": "unfinished"},
    {"point": "D", "battery_cost": 25, "priority": 3, "status": "unfinished"}
]


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
    print("Priority rule: higher number means higher priority")
    print("Task status: completed / unfinished")
    print("------------------------------")


def sort_tasks_by_priority(task_list):
    """
    Sort tasks by priority from high to low.

    按照任务优先级从高到低排序。
    """
    sorted_tasks = sorted(
        task_list,
        key=lambda task: task["priority"],
        reverse=True
    )

    return sorted_tasks


def check_battery(battery_level, required_battery):
    """
    Check whether the robot has enough battery for the next task.

    检查机器人是否有足够电量执行下一个任务。
    """
    if battery_level >= required_battery:
        return True
    else:
        return False


def print_task_info(task):
    """
    Print current task information.

    输出当前任务信息。
    """
    print(f"Next target point: {task['point']}")
    print(f"Task priority: {task['priority']}")
    print(f"Battery required: {task['battery_cost']}%")
    print(f"Current task status: {task['status']}")


def move_to_point(robot_name, point, battery_cost):
    """
    Simulate the robot moving to a target point.

    模拟机器人移动到目标点。
    """
    print(f"{robot_name} is moving to point {point}.")
    print(f"This task will consume {battery_cost}% battery.")


def complete_task(task, battery_level):
    """
    Mark the task as completed and print completion information.

    将任务标记为 completed，并输出任务完成信息。
    """
    task["status"] = "completed"

    print(f"Task at point {task['point']} completed.")
    print(f"Updated task status: {task['status']}")
    print(f"Battery left: {battery_level}%")


def stop_task(task, battery_level):
    """
    Keep the task as unfinished and print stop information.

    保持任务状态为 unfinished，并输出任务停止信息。
    """
    task["status"] = "unfinished"

    print(f"Battery is not enough for point {task['point']}.")
    print(f"Battery left: {battery_level}%")
    print(f"Battery required: {task['battery_cost']}%")
    print(f"Updated task status: {task['status']}")
    print("Robot stops the task.")


def calculate_completed_tasks(task_list):
    """
    Count completed tasks.

    统计已完成任务数量。
    """
    completed_tasks = 0

    for task in task_list:
        if task["status"] == "completed":
            completed_tasks = completed_tasks + 1

    return completed_tasks


def print_task_status_table(task_list):
    """
    Print the final status of each task.

    输出每个任务的最终状态。
    """
    print("Task Status Details")
    print("------------------------------")

    for task in task_list:
        print(
            f"Point {task['point']} | "
            f"Priority: {task['priority']} | "
            f"Battery cost: {task['battery_cost']}% | "
            f"Status: {task['status']}"
        )


def print_summary(task_list, final_battery):
    """
    Print the final task summary.

    输出最终任务总结。
    """
    total_tasks = len(task_list)
    completed_tasks = calculate_completed_tasks(task_list)
    unfinished_tasks = total_tasks - completed_tasks
    completion_rate = completed_tasks / total_tasks * 100

    print("------------------------------")
    print("Task Summary")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Unfinished tasks: {unfinished_tasks}")
    print(f"Final battery: {final_battery}%")
    print(f"Task completion rate: {completion_rate:.1f}%")
    print("------------------------------")

    print_task_status_table(task_list)

    print("------------------------------")
    print("Robot Task Manager Finished")


# ==============================
# 3. Main Program
# 3. 主程序
# ==============================

total_tasks = len(tasks)

print_header(robot_name, battery, total_tasks)

# Sort tasks by priority before execution
# 执行任务前，先按照优先级排序
sorted_tasks = sort_tasks_by_priority(tasks)

print("Task execution order after priority sorting:")
print("按优先级排序后的任务执行顺序：")

for task in sorted_tasks:
    print(f"Point {task['point']} - Priority {task['priority']}")

print("------------------------------")

# Execute tasks one by one according to priority
# 按照优先级依次执行任务
for task in sorted_tasks:
    print_task_info(task)

    if check_battery(battery, task["battery_cost"]):
        move_to_point(robot_name, task["point"], task["battery_cost"])

        # Update battery after task completion
        # 任务完成后更新电量
        battery = battery - task["battery_cost"]

        # Update task status
        # 更新任务状态
        complete_task(task, battery)
    else:
        stop_task(task, battery)
        break

    print("------------------------------")


# ==============================
# 4. Final Summary
# 4. 最终总结
# ==============================

print_summary(sorted_tasks, battery)