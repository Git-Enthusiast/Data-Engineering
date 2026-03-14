# Python Module Search Path, PYTHONPATH & Key CLI Commands --- Complete Guide

## Quick summary

- When you `import name`, Python must locate the object referred to by
    `name`. It does that by searching a list of directories (and using
    import machinery).
- Search order (conceptual): **current directory → PYTHONPATH →
    standard library → site-packages (third-party)**.
- In practice there are details such as `sys.path[0]`, `.pth` files,
    namespace packages, zip imports, and user site directories.

This guide explains:

- How Python finds modules
- How to inspect and modify the module search path
- Best practices for imports
- The most important Python CLI commands

------------------------------------------------------------------------

## 1. How Python Finds Modules

When Python executes:

``` python
import modulename
```

Python uses the **import system** (`importlib`) to locate the module.

Python checks several possibilities:

- `modulename.py`
- `modulename/` directory (a package)
- compiled extensions (`.pyd`, `.so`)
- modules provided by import hooks

------------------------------------------------------------------------

### Python Module Search Order

1. **Current directory (script location)**
2. **Directories in `PYTHONPATH`**
3. **Standard Library**
4. **Site-packages**
5. **Programmatically added paths**

------------------------------------------------------------------------

## 2. Understanding sys.path

`sys.path` is a list containing directories Python searches.

Example:

``` python
import sys
print(sys.path)
```

Example output:

```text
['C:\\project',
 'C:\\Python312\\Lib',
 'C:\\Python312\\Lib\\site-packages']
```

------------------------------------------------------------------------

### sys.path\[0\]

The first element is special.

- When running a script → directory of script
- Interactive shell → empty string `''`

Example:

``` bash
python C:\projects\main.py
```

Inside Python:

``` python
import sys
print(sys.path[0])
```

Output:

```text
C:\projects
```

------------------------------------------------------------------------

## 3. PYTHONPATH Environment Variable

`PYTHONPATH` allows you to add extra directories to Python's module
search path.

Separator:

- Windows → `;`
- Linux/Mac → `:`

------------------------------------------------------------------------

### Windows (temporary)

``` cmd
set PYTHONPATH=D:\python_modules
python script.py
```

------------------------------------------------------------------------

### Windows PowerShell

``` powershell
$env:PYTHONPATH="D:\python_modules"
python script.py
```

------------------------------------------------------------------------

### Permanent setting

``` cmd
setx PYTHONPATH "D:\python_modules"
```

Restart terminal after running.

------------------------------------------------------------------------

### Linux / Mac

Temporary:

``` bash
export PYTHONPATH="/home/user/modules"
python script.py
```

Persistent:

Add to:

```text
~/.bashrc
~/.zshrc
```

------------------------------------------------------------------------

## 4. Modifying sys.path in Python

Instead of modifying environment variables you can change the path in
code.

``` python
import sys

sys.path.append("D:\\python_modules")

import helper
```

Insert with high priority:

``` python
sys.path.insert(0, "D:\\python_modules")
```

------------------------------------------------------------------------

## 5. Loading Modules Using importlib

Example loading module directly from path:

``` python
import importlib.util
from pathlib import Path

path = Path("D:/modules/helper.py")

spec = importlib.util.spec_from_file_location("helper", str(path))
module = importlib.util.module_from_spec(spec)

spec.loader.exec_module(module)
```

This method loads modules **without modifying sys.path**.

------------------------------------------------------------------------

## 6. Running Modules with -m

Running Python modules:

```bash
python -m package.module
```

Advantages:

- Handles package imports correctly
- Useful for running tools like:

```bash
python -m pip
python -m http.server
```

------------------------------------------------------------------------

## 7. Packages and **init**.py

Example package structure:

```text
project/
   mypkg/
      __init__.py
      module.py
```

Import example:

``` python
import mypkg.module
```

------------------------------------------------------------------------

### Relative Imports

Inside packages:

``` python
from .utils import helper
from ..common import config
```

Relative imports work only when the module is run as part of a package.

------------------------------------------------------------------------

## 8. site-packages and .pth files

Third-party libraries are installed in **site-packages**.

Find location:

``` python
import site

print(site.getsitepackages())
print(site.getusersitepackages())
```

`.pth` files can automatically add directories to Python's path.

------------------------------------------------------------------------

## 9. Common Import Problems

### Name Collision

Avoid naming files like:

```text
random.py
math.py
```

These can shadow standard modules.

------------------------------------------------------------------------

### Module Not Found

Check:

```text
sys.path
```

Ensure module directory is included.

------------------------------------------------------------------------

### Circular Imports

Occurs when:

```text
A imports B
B imports A
```

Solution: move imports inside functions or restructure modules.

------------------------------------------------------------------------

## 10. Best Practices

- Use **packages** instead of random scripts
- Avoid modifying `sys.path` frequently
- Use **virtual environments**
- Use `python -m` for running modules

------------------------------------------------------------------------

## 11. Top 7 Python CLI Commands

### 1. Find Python Location

Windows:

```cmd
where python
```

Linux/Mac:

```bash
which python3
```

------------------------------------------------------------------------

### 2. Run Python Script

```bash
python script.py
```

Example:

```bash
python hello.py
```

------------------------------------------------------------------------

### 3. Run Python Code Directly

```bash
python -c "print('Hello World')"
```

------------------------------------------------------------------------

### 4. Check Python Version

```bash
python --version
```

Windows launcher:

```cmd
py -0
```

------------------------------------------------------------------------

### 5. Manage Packages

Install package:

```bash
pip install package_name
```

List packages:

```bash
pip list
```

------------------------------------------------------------------------

### 6. Open Python Interpreter

```bash
python
```

Example session:

```python
>>> 5+10
15
```

Exit:

```python
exit()
```

------------------------------------------------------------------------

### 7. Install Python via CLI

Windows:

```cmd
choco install python
```

Mac:

```bash
brew install python
```

Ubuntu:

```bash
sudo apt install python3
```

------------------------------------------------------------------------

## 12. Windows Python Launcher Tips

List installed Python versions:

```cmd
py -0p
```

Run specific version:

```cmd
py -3.10
```

------------------------------------------------------------------------

## 13. Practical Examples

### Import module from another drive

``` cmd
set PYTHONPATH=D:\utils
python main.py
```

------------------------------------------------------------------------

### Using sys.path

``` python
import sys
sys.path.insert(0,"D:\\utils")
import helper
```

------------------------------------------------------------------------

## 14. Troubleshooting Checklist

- `python --version`
- `where python`
- `python -m pip list`
- `python -c "import sys; print(sys.path)"`

------------------------------------------------------------------------

## 15. TL;DR

- Python searches modules using **sys.path**
- `PYTHONPATH` adds custom directories
- Prefer **packages + virtual environments**
- Use `python -m` for modules
- Key commands:

```bash
where python
python script.py
python -c "..."
python --version
pip install package
python
```
