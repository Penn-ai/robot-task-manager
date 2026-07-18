# Review Robot Program  
# 机器人复习程序

## 1. Project Purpose | 项目目的

This file is used to review basic Linux, Git, and Python knowledge through a simple robot-related Python program.

这个文件用于通过一个简单的机器人 Python 程序，复习 Linux、Git 和 Python 基础知识。

The goal is not to build a real robot system, but to strengthen my understanding of basic programming logic before learning ROS2 and robot simulation.

这个项目的目标不是构建真正的机器人系统，而是在学习 ROS2 和机器人仿真之前，巩固基础编程逻辑。

---

## 2. What This Project Reviews | 本项目复习内容

This small project reviews the following topics:

这个小项目复习以下内容：

### Linux Commands | Linux 命令

- `pwd` — show current directory  
  显示当前所在文件夹

- `ls` — list files and folders  
  查看当前文件夹中的文件和文件夹

- `cd` — change directory  
  进入或切换文件夹

- `mkdir` — create a new folder  
  创建新文件夹

- `touch` — create a new file  
  创建新文件

- `rm` — remove a file  
  删除文件

- `cp` — copy a file  
  复制文件

- `mv` — move or rename a file  
  移动文件或重命名文件

### Git Commands | Git 命令

- `git status` — check project status  
  查看项目当前状态

- `git add .` — add changes to the staging area  
  把修改加入暂存区

- `git commit -m "message"` — save a local version  
  保存一个本地版本

- `git push` — upload local commits to GitHub  
  把本地版本上传到 GitHub

### Python Basics | Python 基础

- Variables  
  变量

- Strings  
  字符串

- Numbers  
  数字

- If / else statements  
  条件判断语句

- For loops  
  for 循环

- Lists  
  列表

- Functions  
  函数

- Return values  
  返回值

- f-string output  
  f-string 格式化输出

---

## 3. Program Scenario | 程序场景

This program simulates a simple robot completing tasks at different target points.

这个程序模拟一个简单机器人依次前往不同目标点完成任务。

The robot has:

机器人具有：

- A name  
  一个名称

- An initial battery level  
  一个初始电量

- A list of target points  
  一组目标点

- A fixed battery cost for each task  
  每个任务固定消耗的电量

The robot will move to each target point one by one.

机器人会按照顺序依次前往每个目标点。

Before moving to a target point, the robot checks whether the battery is enough.

在前往每个目标点之前，机器人会检查电量是否足够。

If the battery is enough, the robot completes the task.

如果电量足够，机器人完成任务。

If the battery is not enough, the robot stops.

如果电量不足，机器人停止任务。

---

## 4. Program Logic | 程序逻辑

The program follows this process:

程序按照以下流程运行：

```text
Start program
程序开始

Set robot name
设置机器人名称

Set initial battery
设置初始电量

Set target points
设置目标点列表

Loop through each target point
循环执行每个目标点任务

Check battery
检查电量

If battery is enough:
如果电量足够：

    Move to target point
    移动到目标点

    Reduce battery
    扣除电量

    Count completed task
    记录已完成任务

If battery is not enough:
如果电量不足：

    Stop the task
    停止任务

Print task summary
输出任务总结
```

---

## 5. Key Python Concepts | 核心 Python 知识

### 5.1 Variables | 变量

Variables are used to store information.

变量用于存储信息。

Example:

示例：

```python
robot_name = "TurtleBot3"
battery = 60
battery_cost = 10
```

In this project:

在本项目中：

- `robot_name` stores the robot name  
  `robot_name` 存储机器人名称

- `battery` stores the current battery level  
  `battery` 存储当前电量

- `battery_cost` stores the battery consumed by each task  
  `battery_cost` 存储每个任务消耗的电量

---

### 5.2 Strings | 字符串

Strings are text data. They need quotation marks.

字符串是文本数据，需要使用引号。

Example:

示例：

```python
robot_name = "TurtleBot3"
task_status = "running"
```

---

### 5.3 Numbers | 数字

Numbers are used for calculation.

数字用于计算。

Example:

示例：

```python
battery = 60
battery_cost = 10
battery = battery - battery_cost
```

This means:

这表示：

```text
New battery = Current battery - Battery cost
新电量 = 当前电量 - 任务消耗电量
```

---

### 5.4 List | 列表

A list can store multiple values.

列表可以存储多个值。

Example:

示例：

```python
target_points = ["A", "B", "C", "D"]
```

In this project, the list stores all target points the robot needs to visit.

在本项目中，列表用于存储机器人需要前往的所有目标点。

---

### 5.5 For Loop | for 循环

A for loop is used to repeat actions.

for 循环用于重复执行动作。

Example:

示例：

```python
for point in target_points:
    print(point)
```

This means:

这表示：

```text
Take one target point from the list each time.
每次从列表中取出一个目标点。
```

---

### 5.6 If / Else | 条件判断

If / else is used for decision-making.

if / else 用于进行条件判断。

Example:

示例：

```python
if battery >= battery_cost:
    print("Battery enough.")
else:
    print("Battery low.")
```

This means:

这表示：

```text
If the battery is enough, continue.
If the battery is not enough, stop.
如果电量足够，就继续。
如果电量不足，就停止。
```

---

### 5.7 Function | 函数

A function is a reusable block of code.

函数是一段可以重复使用的代码。

Example:

示例：

```python
def move_to_point(point):
    print(f"Robot is moving to point {point}.")
```

This function simulates the robot moving to a target point.

这个函数用于模拟机器人移动到目标点。

---

### 5.8 Return | 返回值

`return` sends a result back to the program.

`return` 会把结果返回给程序。

Example:

示例：

```python
def check_battery(battery_level, required_battery):
    if battery_level >= required_battery:
        return True
    else:
        return False
```

If the battery is enough, the function returns `True`.

如果电量足够，函数返回 `True`。

If the battery is not enough, the function returns `False`.

如果电量不足，函数返回 `False`。

---

## 6. How to Run | 如何运行

Open the terminal in VS Code.

在 VS Code 中打开终端。

Run:

运行：

```bash
python review_robot.py
```

If your system uses Python 3, run:

如果你的系统使用 `python3` 命令，运行：

```bash
python3 review_robot.py
```

---

## 7. Example Output | 示例输出

```text
Review Robot Program Started
Robot name: TurtleBot3
Initial battery: 60%
Target points: ['A', 'B', 'C', 'D']
Battery cost per task: 15%
Low battery threshold: 15%
------------------------------
Next target point: A
Battery check passed.
TurtleBot3 is moving to point A.
Task at point A completed.
Battery left: 45%
------------------------------
Next target point: B
Battery check passed.
TurtleBot3 is moving to point B.
Task at point B completed.
Battery left: 30%
------------------------------
Next target point: C
Battery check passed.
TurtleBot3 is moving to point C.
Task at point C completed.
Battery left: 15%
------------------------------
Next target point: D
Battery check passed.
TurtleBot3 is moving to point D.
Task at point D completed.
Battery left: 0%
------------------------------
Task Summary
Total tasks: 4
Completed tasks: 4
Unfinished tasks: 0
Final battery: 0%
Robot status: Task process finished.
```

---

## 8. What I Learned | 我的学习收获

Through this review project, I practiced how to connect basic Python concepts with a robot-related scenario.

通过这个复习项目，我练习了如何把 Python 基础知识和机器人相关场景联系起来。

I learned that a simple robot program can be built from the following basic elements:

我理解到，一个简单的机器人程序可以由以下基础元素组成：

- Robot state  
  机器人状态

- Task list  
  任务列表

- Battery check  
  电量检查

- Task execution  
  任务执行

- Task result summary  
  任务结果总结

This is a basic form of robot task management logic.

这是一种基础的机器人任务管理逻辑。

---

## 9. Relationship to Future Robotics Learning | 与未来机器人学习的关系

This project is simple, but the logic is useful for future robotics learning.

这个项目虽然简单，但其中的逻辑对未来机器人学习很有用。

In future ROS2 and robot simulation projects, robots will also need to:

在未来的 ROS2 和机器人仿真项目中，机器人同样需要：

- Receive tasks  
  接收任务

- Check current state  
  检查当前状态

- Make decisions  
  做出判断

- Execute actions  
  执行动作

- Update results  
  更新结果

- Report status  
  输出状态

This project helps me build the foundation for learning ROS2, robot navigation, and Physical AI.

这个项目帮助我为学习 ROS2、机器人导航和 Physical AI 打下基础。

---

## 10. Review Checklist | 复习检查清单

After completing this project, I should be able to explain:

完成这个项目后，我应该能够解释：

- What `pwd`, `ls`, `cd`, `mkdir`, `touch`, `rm`, `cp`, and `mv` mean  
  `pwd`、`ls`、`cd`、`mkdir`、`touch`、`rm`、`cp`、`mv` 的含义

- What `git status`, `git add`, `git commit`, and `git push` do  
  `git status`、`git add`、`git commit`、`git push` 的作用

- What variables, strings, and numbers are  
  什么是变量、字符串和数字

- How `if / else` works  
  `if / else` 如何工作

- How a `for` loop works  
  `for` 循环如何工作

- How a list stores multiple values  
  列表如何存储多个值

- How a function organizes reusable logic  
  函数如何组织可重复使用的逻辑

- How `return` sends results back to the program  
  `return` 如何把结果返回给程序

---

## 11. Summary | 总结

This review project helps me turn basic Linux, Git, and Python knowledge into practical skills.

这个复习项目帮助我把 Linux、Git 和 Python 基础知识转化为实际技能。

The most important idea is:

最重要的思想是：

```text
A robot has states, receives tasks, checks conditions, executes actions, updates data, and prints results.

机器人有状态，接收任务，检查条件，执行动作，更新数据，并输出结果。
```

This thinking will be useful when I start learning ROS2 and robot simulation.

这种思维在我开始学习 ROS2 和机器人仿真时会非常有用。