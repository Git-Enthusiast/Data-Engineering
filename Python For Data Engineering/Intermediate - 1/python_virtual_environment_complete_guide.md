# Python Virtual Environment --- Complete Guide

A comprehensive guide to **Python Virtual Environments**, explaining
what they are, why they are needed, how they work, and the different
ways to create and manage them.

------------------------------------------------------------------------

## 1. Introduction to Python Libraries

Before understanding virtual environments, we must first understand
**Python libraries**.

Python libraries are collections of **pre-written code** that help
developers perform common tasks without writing everything from scratch.

There are **two main types of libraries** in Python.

### 1.1 Standard Libraries

Standard libraries are **built-in libraries** that come with Python
installation.

They do **not require installation**.

Examples:

- math
- os
- sys
- datetime
- json
- random

Example:

``` python
import math
print(math.sqrt(16))
```

Output:

```text
4.0
```

------------------------------------------------------------------------

### 1.2 Third-Party Libraries

Third-party libraries are **created by the Python community** and must
be installed manually.

They are installed using **pip** (Python package manager).

Examples:

- numpy
- pandas
- requests
- flask
- django
- tensorflow

Install example:

``` bash
pip install numpy
```

------------------------------------------------------------------------

## 2. The Problem Without Virtual Environments

When working on **multiple Python projects**, each project may require
**different versions of the same library**.

Example:

| Project | Required NumPy Version |
| ----------- | ------------------------ |
| Project A | NumPy 1.9 |
| Project B | NumPy 1.3 |

If you install:

``` bash
pip install numpy==1.9
```

Then later:

``` bash
pip install numpy==1.3
```

The new version replaces the old one.

Problems:

- Project A may stop working
- Project B may break
- Dependency conflicts occur

This becomes serious in **large applications**.

------------------------------------------------------------------------

## 3. What is a Python Virtual Environment?

A **Virtual Environment** is a **self-contained directory** that
contains:

- A specific Python interpreter
- Installed libraries for that project
- Independent package management

Each project gets its **own isolated Python environment**.

**Definition:**

A Python virtual environment is an **isolated runtime environment** that
allows projects to have **separate dependencies and package versions**.

------------------------------------------------------------------------

## 4. How Virtual Environments Solve the Problem

Instead of installing packages globally, separate environments are
created.

Example structure:

```text
System
│
├── Project_A
│   └── venv
│       └── numpy 1.9
│
└── Project_B
    └── venv
        └── numpy 1.3
```

Both projects run **independently** without conflicts.

------------------------------------------------------------------------

## 5. Benefits of Virtual Environments

### Dependency Isolation

Each project has its **own libraries**, preventing conflicts.

### Version Control

Different projects can use **different versions** of the same package.

Example:

```text
Project A → Django 3
Project B → Django 5
```

### Clean System Environment

Global Python installation remains **clean and minimal**.

### Safe Experimentation

You can install or remove packages without affecting other projects.

### Easy Project Sharing

Dependencies can be shared using **requirements.txt**.

Create requirements file:

``` bash
pip freeze > requirements.txt
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 6. Ways to Create Virtual Environments

Common methods:

1. venv (built-in)
2. virtualenv
3. virtualenvwrapper
4. virtualenvwrapper-win
5. conda environments

------------------------------------------------------------------------

## 7. Method 1 --- Using venv (Built-in)

`venv` is the **official virtual environment module** included with
Python 3.

Create environment:

``` bash
python -m venv venv
```

Folder structure:

```text
project/
│
├── venv/
│   ├── Scripts
│   ├── Lib
│   └── pyvenv.cfg
```

Activate:

Windows:

``` bash
venv\Scripts\activate
```

Mac/Linux:

``` bash
source venv/bin/activate
```

Install packages:

``` bash
pip install numpy
```

Deactivate:

``` bash
deactivate
```

------------------------------------------------------------------------

## 8. Method 2 --- Using virtualenv

Install:

``` bash
pip install virtualenv
```

Create environment:

``` bash
virtualenv myenv
```

Specify Python version:

``` bash
virtualenv -p python3 myenv
```

Activate:

Windows:

``` bash
myenv\Scripts\activate
```

Linux/Mac:

``` bash
source myenv/bin/activate
```

------------------------------------------------------------------------

## 9. Method 3 --- Using virtualenvwrapper

Install:

``` bash
pip install virtualenvwrapper
```

Commands:

Create environment:

```bash
mkvirtualenv myenv
```

Activate:

```bash
workon myenv
```

Delete:

```bash
rmvirtualenv myenv
```

------------------------------------------------------------------------

## 10. Method 4 --- virtualenvwrapper-win (Windows)

Install:

``` bash
pip install virtualenvwrapper-win
```

Create environment:

``` bash
mkvirtualenv myenv
```

Activate:

``` bash
workon myenv
```

Deactivate:

``` bash
deactivate
```

------------------------------------------------------------------------

## 11. Method 5 --- Using Conda

Used widely in **data science and machine learning**.

Tools:

- Anaconda
- Miniconda

Create environment:

``` bash
conda create --name myenv python=3.10
```

Activate:

``` bash
conda activate myenv
```

Deactivate:

``` bash
conda deactivate
```

------------------------------------------------------------------------

## 12. Useful Virtual Environment Commands

Show installed packages:

``` bash
pip list
```

Export dependencies:

``` bash
pip freeze > requirements.txt
```

Install from requirements file:

``` bash
pip install -r requirements.txt
```

Delete environment by removing folder.

Linux/Mac:

``` bash
rm -rf venv
```

Windows:

``` bash
rmdir /s venv
```

------------------------------------------------------------------------

## 13. Best Practices

- Create **one environment per project**
- Do **not commit venv to Git**
- Use **requirements.txt**
- Use clear environment names

Example `.gitignore`:

```text
venv/
```

------------------------------------------------------------------------

## 14. Typical Project Structure

```text
my_project/
│
├── venv/
├── src/
├── main.py
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

## 15. When Should You Use Virtual Environments?

Use them when:

- Working on multiple Python projects
- Using third-party libraries
- Building web applications
- Doing data science or ML work
- Sharing code with other developers

------------------------------------------------------------------------

## 16. Summary

Python Virtual Environments allow developers to create **isolated
environments for each project**.

They help:

- prevent dependency conflicts
- maintain clean systems
- manage package versions
- make projects reproducible

Common tools:

- venv
- virtualenv
- virtualenvwrapper
- virtualenvwrapper-win
- conda

Using virtual environments is considered a **best practice in Python
development**.
