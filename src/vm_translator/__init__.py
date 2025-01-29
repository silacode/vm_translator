"""VM Translator module."""

import importlib
import os
from pathlib import Path

# You can leave this empty but with a docstring
# or add version information
__version__ = "0.1.0"
__author__ = "Siladitya Samaddar"

# Automatically import all modules in the package
__all__ = []
for module in os.listdir(Path(__file__).parent):
    if module.endswith(".py") and module != "__init__.py":
        module_name = module[:-3]  # Remove '.py'
        __all__ += [module_name]  # noqa: PLE0604
        globals()[module_name] = importlib.import_module(f".{module_name}", __package__)
