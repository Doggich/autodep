import importlib.util
import subprocess
import sys
import os
import inspect


def install_missing_modules(module_names):
    """Install required Python modules using pip"""
    for module_name in module_names:
        try:
            # Use the current Python interpreter to run pip
            subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        except subprocess.CalledProcessError as e:
            print(f"Error installing module {module_name}: {e}")
            return False
    return True


def retry_on_missing_module(max_attempts=3):
    """Decorator factory to handle ModuleNotFoundError by installing missing packages"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except ModuleNotFoundError as e:
                    module_name = e.name
                    print(f"Attempt {attempt}/{max_attempts}: Module {module_name} not found")

                    # Install missing module
                    success = install_missing_modules([module_name])

                    # If installation failed, try to adjust sys.path
                    if not success or importlib.util.find_spec(module_name) is None:
                        print(f"Installation failed for {module_name} or still not found.")
                        if attempt == max_attempts:
                            print("Max retries reached. Adding caller's directory to sys.path as fallback.")
                            # Get the caller's file path
                            caller_frame = inspect.stack()[1]
                            caller_path = os.path.dirname(os.path.abspath(caller_frame.filename))
                            if caller_path not in sys.path:
                                sys.path.append(caller_path)
                    else:
                        print(f"Successfully installed {module_name}")
            # Try one more time after adjustments
            return func(*args, **kwargs)

        return wrapper

    return decorator


@retry_on_missing_module()
def dofile(path):
    """Execute a Python script file with automatic dependency handling"""
    with open(path, 'r') as file:
        code = file.read()
        # Use the global context of the caller
        caller_globals = inspect.stack()[1][0].f_globals
        exec(code, caller_globals)

