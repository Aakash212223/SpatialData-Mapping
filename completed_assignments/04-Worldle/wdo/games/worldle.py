import random
from typing import Optional, Dict, Any, List


def choose_target(features: List[Dict], seed: Optional[int] = None) -> Dict[str, Any]:
    """Choose a target feature for Worldle."""
    if seed is not None:
        random.seed(seed)
    return random.choice(features)


def feature_center(feature):
    """Return representative center point of a feature."""
    coords = feature['geometry']['coordinates']
    
    
    all_points = []
    if feature['geometry']['type'] == 'Polygon':
        for ring in coords:
            all_points.extend(ring)
    elif feature['geometry']['type'] == 'MultiPolygon':
        for polygon in coords:
            for ring in polygon:
                all_points.extend(ring)
    
    
    if not all_points:
        return (0, 0)
    
    lats = [p[1] for p in all_points]
    lons = [p[0] for p in all_points]
    
    return (sum(lats) / len(lats), sum(lons) / len(lons))


def guess_feedback(guess_feature, target_feature):
    """Return distance, bearing, and descriptive feedback."""
    from wdo.geometry.distance import haversine_km
    from wdo.geometry.bearing import initial_bearing, bearing_to_compass
    
    # Get center points
    guess_center = feature_center(guess_feature)
    target_center = feature_center(target_feature)
    
    # Calculate distance
    distance_km = haversine_km(guess_center, target_center)
    
    
    bearing_deg = initial_bearing(guess_center, target_center)
    compass = bearing_to_compass(bearing_deg)
    
    # Arrow symbols
    arrows = {
        "N": "↑", "NE": "↗", "E": "→", "SE": "↘",
        "S": "↓", "SW": "↙", "W": "←", "NW": "↖"
    }
    arrow = arrows.get(compass, "•")
    
    return {
        "correct": guess_feature['properties']['name'] == target_feature['properties']['name'],
        "distance_km": distance_km,
        "bearing_deg": bearing_deg,
        "compass": compass,
        "arrow": arrow
    }


def format_feedback(result) -> str:
    """Pretty-print guess feedback."""
    raise NotImplementedError
