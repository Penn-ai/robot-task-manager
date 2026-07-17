# Learning Notes  
# 学习笔记

## Project Goal | 项目目标

The goal of this project is to practice basic Python programming through a simple robot-related task management example.

本项目的目标是通过一个简单的机器人任务管理案例，练习 Python 基础编程。

The program simulates a robot completing a list of tasks while checking its battery level.

这个程序模拟一个机器人在检查电量的同时，依次完成一组任务。

This project helps me understand how basic programming logic can be connected to robotics-related scenarios.

这个项目帮助我理解基础编程逻辑如何和机器人应用场景联系起来。

---

## Key Ideas | 核心思路

### 1. Robot State | 机器人状态

The robot has a battery level.

机器人有一个电量状态。

```python
battery = 60
```

The battery level changes after each completed task.

每完成一个任务后，机器人电量都会发生变化。

In robotics software, a robot usually has many states, such as battery level, position, speed, and task status.

在机器人软件中，机器人通常会有很多状态，例如电量、位置、速度和任务状态。

---

### 2. Task Data | 任务数据

Each task has a target point and a battery cost.

每个任务都有一个目标点和对应的电量消耗。

```python
tasks = {
    "A": 10,
    "B": 15,
    "C": 20,
    "D": 25
}
```

The key is the target point, and the value is the required battery cost.

其中，字典的 key 是目标点，value 是执行该任务所需的电量。

For example:

例如：

- `"A": 10` means moving to point A requires 10% battery.  
  `"A": 10` 表示移动到 A 点需要消耗 10% 电量。

- `"B": 15` means moving to point B requires 15% battery.  
  `"B": 15` 表示移动到 B 点需要消耗 15% 电量。

This helps me understand how dictionaries can store task-related information.

这帮助我理解字典如何存储任务相关信息。

---

### 3. Battery Check | 电量检查

Before each task, the program checks whether the robot has enough battery.

在执行每个任务之前，程序会检查机器人电量是否足够。

```python
def check_battery(battery_level, required_battery):
    if battery_level >= required_battery:
        return True
    else:
        return False
```

If the result is `True`, the robot continues the task.

如果结果是 `True`，机器人继续执行任务。

If the result is `False`, the robot stops.

如果结果是 `False`，机器人停止执行任务。

This logic is similar to a basic decision-making process in robotics.

这个逻辑类似于机器人中的基础决策过程。

---

### 4. Task Execution | 任务执行

The robot moves to each target point one by one.

机器人会按照顺序依次前往每个目标点。

```python
for point, battery_cost in tasks.items():
```

This loop reads both the target point and the required battery cost.

这个循环会同时读取目标点和该目标点对应的电量消耗。

For each task, the program follows this process:

对于每个任务，程序会按照以下流程执行：

1. Read the next target point  
   读取下一个目标点

2. Check whether the battery is enough  
   检查电量是否足够

3. If the battery is enough, complete the task  
   如果电量足够，完成任务

4. Reduce the battery level  
   扣除相应电量

5. If the battery is not enough, stop the task process  
   如果电量不足，停止任务流程

---

### 5. Task Statistics | 任务统计

The program calculates task execution results after the robot stops or completes all tasks.

当机器人停止任务或完成所有任务后，程序会统计任务执行结果。

The statistics include:

统计内容包括：

- Total tasks  
  总任务数

- Completed tasks  
  已完成任务数

- Unfinished tasks  
  未完成任务数

- Final battery  
  最终剩余电量

- Task completion rate  
  任务完成率

The task completion rate is calculated by:

任务完成率的计算方式是：

```python
completion_rate = completed_tasks / total_tasks * 100
```

This means:

这表示：

```text
Task completion rate = Completed tasks / Total tasks × 100
任务完成率 = 已完成任务数 / 总任务数 × 100
```

For example, if the robot completes 3 out of 4 tasks, the completion rate is 75%.

例如，如果机器人完成了 4 个任务中的 3 个，那么任务完成率就是 75%。

---

## Program Logic | 程序逻辑

The overall logic of this project is:

这个项目的整体逻辑是：

```text
Start program
程序开始

Set robot name and initial battery
设置机器人名称和初始电量

Define target tasks and battery costs
定义目标任务和电量消耗

Loop through each task
循环执行每个任务

Check battery before each task
每个任务前检查电量

Complete task if battery is enough
如果电量足够，则完成任务

Stop task process if battery is not enough
如果电量不足，则停止任务

Calculate task statistics
计算任务统计结果

Print task summary
输出任务总结
```

---

## What I Learned | 我的学习收获

Through this project, I practiced:

通过这个项目，我练习了：

- How to organize Python code  
  如何组织 Python 代码

- How to use variables to store robot states  
  如何使用变量存储机器人状态

- How to use dictionaries to store task information  
  如何使用字典存储任务信息

- How to use functions to separate program logic  
  如何使用函数拆分程序逻辑

- How to use if statements to make decisions  
  如何使用 if 语句进行判断

- How to use for loops to execute multiple tasks  
  如何使用 for 循环执行多个任务

- How to update variables during program execution  
  如何在程序运行过程中更新变量

- How to calculate simple task statistics  
  如何计算简单的任务统计结果

- How to write a GitHub project README and notes file  
  如何编写 GitHub 项目的 README 和 notes 文件

---

## Relationship to Robotics | 与机器人学习的关系

Although this is a simple Python project, it reflects basic robotics software logic.

虽然这是一个简单的 Python 项目，但它体现了机器人软件中的基础逻辑。

A robot usually needs to manage its own state.

机器人通常需要管理自身状态。

For example:

例如：

- Battery level  
  电量

- Current position  
  当前位置

- Target point  
  目标点

- Task status  
  任务状态

- Remaining resources  
  剩余资源

A robot also needs to decide whether it can continue a task based on its current state.

机器人还需要根据当前状态判断是否可以继续执行任务。

In this project, the battery level is used as a simple robot state, and each target point is treated as a task.

在这个项目中，电量被作为一个简单的机器人状态，每个目标点被看作一个任务。

This logic can be extended in the future to more advanced robotics topics.

这个逻辑未来可以扩展到更高级的机器人学习内容中。

For example:

例如：

- ROS2 robot nodes  
  ROS2 机器人节点

- Robot navigation  
  机器人导航

- Task planning  
  任务规划

- Autonomous mobile robots  
  自主移动机器人

- Warehouse robot simulation  
  仓储机器人仿真

- Physical AI-related robot systems  
  Physical AI 相关机器人系统

---

## Future Improvements | 后续改进方向

This project can be improved in the future by adding more realistic robot task logic.

未来可以通过加入更真实的机器人任务逻辑来改进这个项目。

Possible improvements include:

可能的改进方向包括：

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

- Add obstacle or blocked target points  
  添加障碍物或被阻挡的目标点

- Extend the logic to a ROS2 simulation project  
  将该逻辑扩展到 ROS2 仿真项目中

---

## Summary | 总结

This project is a small but important step in my robotics software learning path.

这个项目是我机器人软件学习路线中的一个小但重要的步骤。

It helps me connect Python basics with robot task execution logic.

它帮助我把 Python 基础知识和机器人任务执行逻辑联系起来。

The most important idea I learned is:

我学到的最重要思想是：

```text
A robot has states, receives tasks, checks conditions, executes actions, updates results, and outputs summaries.

机器人有状态，接收任务，检查条件，执行动作，更新结果，并输出总结。
```

This thinking will be useful for my future learning in ROS2, robot simulation, and Physical AI.

这种思维将对我未来学习 ROS2、机器人仿真和 Physical AI 有帮助。