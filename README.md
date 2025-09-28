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

### Installation

1.1. Clone repo:

```bash
git clone https://github.com/Doggich/autodep.git
cd autodep
```

1.2. Make `venv` for Python 3.X:

#### Windows
```bash
python -m venv venv
```

#### Linux/masOS
```bash
python3 -m venv venv
```

1.3. Activate `venv`:

#### Windows
```bash
.\venv\Scripts\activate
```

#### Linux/masOS
```bash
source venv/bin/activate
```

---