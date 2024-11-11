#__all__=["
import os
import glob

# Generate __all__ with all .py files except __init__.py
__all__ = [
    os.path.basename(f)[:-3]
    for f in glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
    if os.path.basename(f) != "__init__.py"
]
