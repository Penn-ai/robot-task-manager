# Robot Task Manager  
# 机器人任务管理器

## Overview | 项目概述

This project is a simple Python-based robot task manager.

本项目是一个基于 Python 的简单机器人任务管理器。

It simulates a robot completing multiple target-point tasks while checking battery level, updating task status, and calculating task completion statistics.

它模拟一个机器人按照多个目标点执行任务，同时检查电量、更新任务状态，并统计任务完成情况。

This project is part of my learning path toward robotics software, ROS2, and Physical AI-related projects.

本项目是我学习机器人软件、ROS2 和 Physical AI 相关项目过程中的一个基础练习项目。

---

## Features | 项目功能

- Define multiple robot target points  
  设置多个机器人目标点

- Assign different battery costs to different tasks  
  为不同任务设置不同的电量消耗

- Check whether the robot has enough battery before each task  
  在执行每个任务前检查机器人电量是否足够

- Stop the task process when the battery is not enough  
  当电量不足时停止任务执行

- Print the robot task execution process  
  输出机器人任务执行过程

- Calculate task statistics  
  统计任务执行结果

- Output total tasks, completed tasks, unfinished tasks, final battery, and task completion rate  
  输出总任务数、完成任务数、未完成任务数、最终剩余电量和任务完成率

---

## Project Structure | 项目结构

```text
robot-task-manager/
├── README.md
├── robot_task_manager.py
└── notes.md
```

---

## How It Works | 运行逻辑

The robot has an initial battery level.

机器人有一个初始电量。

Each target point requires a different amount of battery. Before moving to each point, the program checks whether the robot has enough battery.

每个目标点需要消耗不同的电量。在机器人移动到每个目标点之前，程序会先判断当前电量是否足够。

If the battery is enough, the robot completes the task and the battery level is reduced.

如果电量足够，机器人会完成该任务，并扣除相应电量。

If the battery is not enough, the robot stops the remaining tasks.

如果电量不足，机器人会停止后续任务。

At the end, the program prints a task summary.

最后，程序会输出任务执行总结。

---

## How to Run | 如何运行

1. Clone this repository:  
   克隆这个仓库：

```bash
git clone https://github.com/your-username/robot-task-manager.git
```

2. Enter the project folder:  
   进入项目文件夹：

```bash
cd robot-task-manager
```

3. Run the Python file:  
   运行 Python 文件：

```bash
python robot_task_manager.py
```

If your system uses Python 3, run:  
如果你的系统使用 `python3` 命令，运行：

```bash
python3 robot_task_manager.py
```

---

## Example Output | 示例输出

```text
Robot Task Manager Started
Robot name: TurtleBot3
Initial battery: 60%
Total tasks: 4
------------------------------
Next target point: A
TurtleBot3 is moving to point A.
This task will consume 10% battery.
Task at point A completed.
Battery left: 50%
------------------------------
Next target point: B
TurtleBot3 is moving to point B.
This task will consume 15% battery.
Task at point B completed.
Battery left: 35%
------------------------------
Next target point: C
TurtleBot3 is moving to point C.
This task will consume 20% battery.
Task at point C completed.
Battery left: 15%
------------------------------
Next target point: D
Battery is not enough for point D.
Robot stops the task.
------------------------------
Task Summary
Total tasks: 4
Completed tasks: 3
Unfinished tasks: 1
Final battery: 15%
Task completion rate: 75.0%
Robot Task Manager Finished
```

---

## Python Concepts Practiced | 练习到的 Python 知识

- Variables  
  变量

- Dictionaries  
  字典

- If statements  
  条件判断语句

- For loops  
  for 循环

- Functions  
  函数

- Return values  
  返回值

- Basic task statistics  
  基础任务统计

- f-string output formatting  
  f-string 格式化输出

---

## Relationship to Robotics | 与机器人学习的关系

Although this is a simple Python project, it reflects several basic ideas in robotics software.

虽然这是一个简单的 Python 项目，但它体现了机器人软件中的几个基础思想。

A robot usually has states, such as battery level, position, speed, and task status.

机器人通常会有状态，例如电量、位置、速度和任务状态。

A robot also needs to decide whether it can continue a task based on its current state.

机器人也需要根据当前状态判断是否可以继续执行任务。

In this project, the battery level is used as a simple robot state, and each target point is treated as a task.

在这个项目中，电量被作为一个简单的机器人状态，每个目标点被看作一个任务。

This logic can be extended in the future to ROS2, robot navigation, task planning, and autonomous robot simulation.

这个逻辑未来可以扩展到 ROS2、机器人导航、任务规划和自主机器人仿真项目中。

---

## Future Improvements | 后续改进方向

- Add task priority  
  添加任务优先级

- Add charging behavior  
  添加自动充电逻辑

- Add task location coordinates  
  添加任务位置坐标

- Add robot speed and travel time  
  添加机器人速度和移动时间

- Save task results to a file  
  将任务结果保存到文件

- Visualize task completion results  
  可视化任务完成结果

- Extend the logic to future ROS2 robot simulation projects  
  将该逻辑扩展到未来的 ROS2 机器人仿真项目中