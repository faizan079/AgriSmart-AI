"""
Crop Recommendation Service
Rule-based crop recommendation system based on soil and climate conditions.
"""
from typing import Dict, List


# Crop database with requirements
CROP_DATABASE = {
    "rice": {
        "soil_types": ["clay", "loamy", "sandy"],
        "ph_range": (5.5, 7.0),
        "temp_range": (20, 35),
        "humidity_range": (70, 90),
        "rainfall_range": (1000, 2500),
        "water_need": "high",
        "seasons": ["monsoon", "summer"],
        "tips": [
            "Requires abundant water supply",
            "Best in clay or loamy soil",
            "Maintain standing water during growth stages",
            "Apply nitrogen fertilizer in split doses"
        ]
    },
    "wheat": {
        "soil_types": ["loamy", "clay", "sandy"],
        "ph_range": (6.0, 7.5),
        "temp_range": (15, 25),
        "humidity_range": (40, 60),
        "rainfall_range": (400, 800),
        "water_need": "medium",
        "seasons": ["winter", "spring"],
        "tips": [
            "Requires cool climate",
            "Well-drained loamy soil ideal",
            "Moderate water requirement",
            "Apply phosphorus and potassium fertilizers"
        ]
    },
    "maize": {
        "soil_types": ["loamy", "sandy", "clay"],
        "ph_range": (5.5, 7.5),
        "temp_range": (18, 32),
        "humidity_range": (50, 70),
        "rainfall_range": (500, 1200),
        "water_need": "medium",
        "seasons": ["summer", "monsoon"],
        "tips": [
            "Requires warm climate",
            "Tolerant to various soil types",
            "Moderate water requirement",
            "Apply nitrogen fertilizer at critical stages"
        ]
    },
    "cotton": {
        "soil_types": ["black", "loamy", "clay"],
        "ph_range": (6.0, 8.0),
        "temp_range": (21, 32),
        "humidity_range": (40, 60),
        "rainfall_range": (500, 1000),
        "water_need": "medium",
        "seasons": ["summer", "monsoon"],
        "tips": [
            "Requires warm climate",
            "Black soil ideal for cultivation",
            "Moderate water requirement",
            "Regular pest monitoring required"
        ]
    },
    "sugarcane": {
        "soil_types": ["loamy", "clay", "sandy"],
        "ph_range": (6.0, 7.5),
        "temp_range": (20, 35),
        "humidity_range": (60, 80),
        "rainfall_range": (1000, 2500),
        "water_need": "high",
        "seasons": ["summer", "monsoon"],
        "tips": [
            "Requires abundant water supply",
            "Long duration crop (12-18 months)",
            "Rich loamy soil ideal",
            "High nitrogen fertilizer requirement"
        ]
    },
    "groundnut": {
        "soil_types": ["sandy", "loamy"],
        "ph_range": (5.5, 7.0),
        "temp_range": (25, 35),
        "humidity_range": (50, 70),
        "rainfall_range": (400, 800),
        "water_need": "low",
        "seasons": ["summer", "monsoon"],
        "tips": [
            "Requires well-drained sandy soil",
            "Drought tolerant crop",
            "Low water requirement",
            "Avoid waterlogging conditions"
        ]
    },
    "soybean": {
        "soil_types": ["loamy", "clay", "sandy"],
        "ph_range": (6.0, 7.0),
        "temp_range": (20, 30),
        "humidity_range": (50, 70),
        "rainfall_range": (500, 1000),
        "water_need": "medium",
        "seasons": ["monsoon", "summer"],
        "tips": [
            "Requires moderate climate",
            "Well-drained soil ideal",
            "Fixes nitrogen in soil",
            "Good rotation crop"
        ]
    },
    "potato": {
        "soil_types": ["sandy", "loamy"],
        "ph_range": (5.0, 6.5),
        "temp_range": (15, 25),
        "humidity_range": (60, 80),
        "rainfall_range": (400, 800),
        "water_need": "medium",
        "seasons": ["winter", "spring"],
        "tips": [
            "Requires cool climate",
            "Sandy loam soil ideal",
            "Moderate water requirement",
            "Avoid waterlogging"
        ]
    },
    "tomato": {
        "soil_types": ["loamy", "sandy"],
        "ph_range": (6.0, 7.0),
        "temp_range": (18, 30),
        "humidity_range": (50, 70),
        "rainfall_range": (400, 800),
        "water_need": "medium",
        "seasons": ["summer", "spring"],
        "tips": [
            "Requires warm climate",
            "Well-drained soil essential",
            "Regular watering required",
            "Support/staking needed for plants"
        ]
    },
    "onion": {
        "soil_types": ["loamy", "sandy", "clay"],
        "ph_range": (6.0, 7.5),
        "temp_range": (15, 25),
        "humidity_range": (50, 70),
        "rainfall_range": (300, 600),
        "water_need": "low",
        "seasons": ["winter", "spring"],
        "tips": [
            "Requires cool climate",
            "Well-drained soil essential",
            "Low water requirement",
            "Avoid waterlogging"
        ]
    },
    "chilli": {
        "soil_types": ["loamy", "sandy"],
        "ph_range": (6.0, 7.0),
        "temp_range": (20, 30),
        "humidity_range": (50, 70),
        "rainfall_range": (500, 1000),
        "water_need": "medium",
        "seasons": ["summer", "monsoon"],
        "tips": [
            "Requires warm climate",
            "Well-drained soil ideal",
            "Moderate water requirement",
            "Regular pest monitoring required"
        ]
    },
    "brinjal": {
        "soil_types": ["loamy", "clay"],
        "ph_range": (6.0, 7.0),
        "temp_range": (20, 32),
        "humidity_range": (50, 70),
        "rainfall_range": (500, 1000),
        "water_need": "medium",
        "seasons": ["summer", "monsoon"],
        "tips": [
            "Requires warm climate",
            "Well-drained soil ideal",
            "Moderate water requirement",
            "Regular pruning beneficial"
        ]
    }
}


def calculate_crop_score(crop_data: Dict, user_conditions: Dict) -> float:
    """Calculate compatibility score for a crop based on user conditions"""
    score = 0.0
    max_score = 6.0  # Total number of factors

    # Soil type compatibility
    if user_conditions["soil_type"] in crop_data["soil_types"]:
        score += 1.0
    else:
        score += 0.3  # Partial credit for wrong soil type

    # pH compatibility
    ph_min, ph_max = crop_data["ph_range"]
    if ph_min <= user_conditions["soil_ph"] <= ph_max:
        score += 1.0
    elif abs(user_conditions["soil_ph"] - ph_min) < 1.0 or abs(user_conditions["soil_ph"] - ph_max) < 1.0:
        score += 0.5  # Partial credit for near-optimal pH

    # Temperature compatibility
    temp_min, temp_max = crop_data["temp_range"]
    if temp_min <= user_conditions["temperature"] <= temp_max:
        score += 1.0
    elif abs(user_conditions["temperature"] - temp_min) < 5 or abs(user_conditions["temperature"] - temp_max) < 5:
        score += 0.5

    # Humidity compatibility
    humidity_min, humidity_max = crop_data["humidity_range"]
    if humidity_min <= user_conditions["humidity"] <= humidity_max:
        score += 1.0
    elif abs(user_conditions["humidity"] - humidity_min) < 10 or abs(user_conditions["humidity"] - humidity_max) < 10:
        score += 0.5

    # Rainfall compatibility
    rainfall_min, rainfall_max = crop_data["rainfall_range"]
    if rainfall_min <= user_conditions["rainfall"] <= rainfall_max:
        score += 1.0
    elif abs(user_conditions["rainfall"] - rainfall_min) < 200 or abs(user_conditions["rainfall"] - rainfall_max) < 200:
        score += 0.5

    # Water availability compatibility
    if user_conditions["water_availability"] == crop_data["water_need"]:
        score += 1.0
    elif (user_conditions["water_availability"] == "medium" and crop_data["water_need"] in ["low", "high"]) or \
         (user_conditions["water_availability"] == "high" and crop_data["water_need"] in ["medium", "low"]):
        score += 0.5

    return score / max_score


def recommend_crop(user_conditions: Dict) -> Dict:
    """Recommend crop based on user conditions"""
    season = user_conditions["season"].lower()

    # Filter crops by season
    seasonal_crops = {
        crop: data for crop, data in CROP_DATABASE.items()
        if season in data["seasons"]
    }

    if not seasonal_crops:
        seasonal_crops = CROP_DATABASE  # Fallback to all crops if no seasonal match

    # Calculate scores for all seasonal crops
    crop_scores = []
    for crop_name, crop_data in seasonal_crops.items():
        score = calculate_crop_score(crop_data, user_conditions)
        crop_scores.append((crop_name, score, crop_data))

    # Sort by score (highest first)
    crop_scores.sort(key=lambda x: x[1], reverse=True)

    if not crop_scores:
        return {
            "recommended_crop": "No suitable crop found",
            "confidence": 0.0,
            "reasoning": "No crops match the given conditions. Please adjust your input parameters.",
            "alternative_crops": [],
            "tips": ["Try adjusting soil pH, temperature, or water availability parameters"]
        }

    # Get top recommendation
    best_crop, best_score, best_crop_data = crop_scores[0]

    # Get alternatives (top 3)
    alternatives = [crop[0] for crop in crop_scores[1:4] if crop[1] > 0.5]

    # Generate reasoning
    reasoning_parts = []
    if user_conditions["soil_type"] in best_crop_data["soil_types"]:
        reasoning_parts.append(f"soil type '{user_conditions['soil_type']}' is ideal")
    if best_crop_data["ph_range"][0] <= user_conditions["soil_ph"] <= best_crop_data["ph_range"][1]:
        reasoning_parts.append(f"soil pH {user_conditions['soil_ph']} is within optimal range")
    if best_crop_data["temp_range"][0] <= user_conditions["temperature"] <= best_crop_data["temp_range"][1]:
        reasoning_parts.append(f"temperature {user_conditions['temperature']}°C is suitable")
    if user_conditions["water_availability"] == best_crop_data["water_need"]:
        reasoning_parts.append(f"water availability '{user_conditions['water_availability']}' matches requirements")

    reasoning = f"{best_crop.title()} is recommended because " + ", ".join(reasoning_parts) + "."
    if not reasoning_parts:
        reasoning = f"{best_crop.title()} is the best match among available options for the {season} season."

    return {
        "recommended_crop": best_crop.title(),
        "confidence": round(best_score, 2),
        "reasoning": reasoning,
        "alternative_crops": [alt.title() for alt in alternatives],
        "tips": best_crop_data["tips"]
    }