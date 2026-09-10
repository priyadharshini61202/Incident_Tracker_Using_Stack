# 🛠️ Drill Rig Incident Tracker

A Python-based **Incident Management System** inspired by real-world drill rig and industrial equipment operations.

The project uses **Object-Oriented Programming (OOP)** and the **Stack (LIFO) data structure** to record, monitor, and handle machine incidents efficiently.

## 📌 Project Overview

During drill rig operations, multiple equipment issues can occur, such as sensor failures, motor problems, overheating, or other machine faults. This project simulates a basic incident tracking workflow where operators can record incidents and manage pending issues.

Each incident contains:

* 🏭 Machine name
* ⚠️ Problem description
* 🔴 Severity level

The system uses a **Stack**, where the most recently added incident is handled first.

## 🚀 Features

* Add new machine incidents
* Handle the latest incident
* View the next pending incident
* Display all pending incidents
* Check the number of pending incidents
* Detect empty incident stack
* Interactive command-line menu

## 🧠 DSA Concepts

This project demonstrates fundamental **Data Structures and Algorithms** concepts:

| Operation | Implementation    |
| --------- | ----------------- |
| Push      | `append()`        |
| Pop       | `pop()`           |
| Peek      | `stack[-1]`       |
| Is Empty  | `len(stack) == 0` |
| Size      | `len(stack)`      |

The core data structure follows the **LIFO (Last In, First Out)** principle.

## 🏗️ OOP Concepts

The project is implemented using a Python class:

```python
class Incident_Tracker:
```

Key OOP concepts used:

* Classes
* Objects
* Constructor
* Methods
* Encapsulation
* Dictionary-based data representation

## 💻 Technologies Used

* **Python**
* **Object-Oriented Programming**
* **Data Structures & Algorithms**
* **Stack**
* **CLI / Console Application**

## 🔧 Industrial Relevance

The project is inspired by **drill rig and industrial control-system environments**, where equipment faults and operational incidents need to be recorded and addressed.

The current implementation is a software simulation and can be extended toward real industrial applications by integrating:

* Real-time sensor data
* PLC/controller data
* Machine status
* Alarm monitoring
* Fault codes
* Incident timestamps
* Severity-based prioritization
* Maintenance history
* Database storage

## 📂 Project Structure

```text
Drill-Rig-Incident-Tracker/
│
├── incident_tracker.py
└── README.md
```

## ▶️ How to Run

Make sure Python is installed on your system.

```bash
python incident_tracker.py
```

Then use the interactive menu:

```text
========== INCIDENT MANAGER ==========
1. Add Incident
2. Handle Incident
3. View Next Incident
4. View All Incidents
5. Number of Incidents
6. Exit
```

## 📈 Future Improvements

* Add incident IDs
* Add timestamps
* Validate severity levels
* Add priority-based incident handling
* Store incident history
* Connect with sensor data
* Integrate PLC/industrial controller data
* Add database support
* Develop a graphical dashboard

## 👨‍💻 Purpose

This project was developed to strengthen my **Python, OOP, and DSA skills** while applying software concepts to an **industrial equipment and drill rig context**.

It represents a step toward combining my experience in **industrial/control systems** with software development and data-driven engineering.

---

⭐ If you find this project useful, feel free to explore or contribute.
