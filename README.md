# Autodep

Automatically install missing Python modules when they are imported.

## Usage

### As a decorator

```python
from autodep import retry_on_missing_module

@retry_on_missing_module(max_attempts=2)
def my_function():
    import some_missing_module
    ...
```

### Execute a script file

```python
from autodep import dofile

dofile("path/to/your_script.py")
```

### Install dependencies

```bash
pip install -r requirements.txt
```