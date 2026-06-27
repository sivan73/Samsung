# Expose constants
from .constants import PI, E, GOLDEN_RATIO

# Expose wrapped built-ins
from .core_extensions import MathWrapper

# Expose custom modules
from .custom_modules.geometry import Shapes

__all__ = ["PI", "E", "GOLDEN_RATIO", "MathWrapper", "Shapes"]