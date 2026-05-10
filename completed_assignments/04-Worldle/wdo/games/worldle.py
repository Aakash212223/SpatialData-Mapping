import random
from typing import Optional, Dict, Any, List


def choose_target(features: List[Dict], seed: Optional[int] = None) -> Dict[str, Any]:
    """Choose a target feature for Worldle++."""
    if seed is not None:
        random.seed(seed)
    return random.choice(features)


def feature_center(feature):
    """Return representative center point of a feature."""
    raise NotImplementedError


def guess_feedback(guess_feature, target_feature):
    """Return distance, bearing, and descriptive feedback."""
    raise NotImplementedError


def format_feedback(result) -> str:
    """Pretty-print guess feedback."""
    raise NotImplementedError
