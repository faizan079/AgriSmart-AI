"""
Smart Irrigation Service
Rule-based irrigation recommendation system.
"""
from typing import Dict


# Crop water requirements database
CROP_WATER_NEEDS = {
    "rice": {
        "critical_moisture": 60,
        "optimal_moisture": 80,
        "water_per_irrigation": 50,  # mm
        "growth_stages": {
            "seedling": {"water_factor": 0.7, "critical_moisture": 65},
            "growing": {"water_factor": 1.0, "critical_moisture": 60},
            "mature": {"water_factor": 0.8, "critical_moisture": 55}
        }
    },
    "wheat": {
        "critical_moisture": 40,
        "optimal_moisture": 60,
        "water_per_irrigation": 30,  # mm
        "growth_stages": {
            "seedling": {"water_factor": 0.6, "critical_moisture": 45},
            "growing": {"water_factor": 1.0, "critical_moisture": 40},
            "mature": {"water_factor": 0.5, "critical_moisture": 35}
        }
    },
    "maize": {
        "critical_moisture": 45,
        "optimal_moisture": 65,
        "water_per_irrigation": 35,  # mm
        "growth_stages": {
            "seedling": {"water_factor": 0.7, "critical_moisture": 50},
            "growing": {"water_factor": 1.0, "critical_moisture": 45},
            "mature": {"water_factor": 0.6, "critical_moisture": 40}
        }
    },
    "cotton": {
        "critical_moisture": 40,
        "optimal_moisture": 60,
        "water_per_irrigation": 40,  # mm
        "growth_stages": {
            "seedling": {"water_factor": 0.6, "critical_moisture": 45},
            "growing": {"water_factor": 1.0, "critical_moisture": 40},
            "mature": {"water_factor": 0.7, "critical_moisture": 35}
        }
    },
    "sugarcane": {
        "critical_moisture": 55,
        "optimal_moisture": 75,
        "water_per_irrigation": 60,  # mm
        "growth_stages": {
            "seedling": {"water_factor": 0.8, "critical_moisture": 60},
            "growing": {"water_factor": 1.0, "critical_moisture": 55},
            "mature": {"water_factor": 0.9, "critical_moisture": 50}
        }
    },
    "groundnut": {
        "critical_moisture": 35,
        "optimal_moisture": 55,
        "water_per_irrigation": 25,  # mm
        "growth_stages": {
            "seedling": {"water_factor": 0.7, "critical_moisture": 40},
            "growing": {"water_factor": 1.0, "critical_moisture": 35},
            "mature": {"water_factor": 0.5, "critical_moisture": 30}
        }
    },
    "soybean": {
        "critical_moisture": 40,
        "optimal_moisture": 60,
        "water_per_irrigation": 30,  # mm
        "growth_stages": {
            "seedling": {"water_factor": 0.7, "critical_moisture": 45},
            "growing": {"water_factor": 1.0, "critical_moisture": 40},
            "mature": {"water_factor": 0.6, "critical_moisture": 35}
        }
    },
    "potato": {
        "critical_moisture": 45,
        "optimal_moisture": 65,
        "water_per_irrigation": 35,  # mm
        "growth_stages": {
            "seedling": {"water_factor": 0.8, "critical_moisture": 50},
            "growing": {"water_factor": 1.0, "critical_moisture": 45},
            "mature": {"water_factor": 0.7, "critical_moisture": 40}
        }
    },
    "tomato": {
        "critical_moisture": 50,
        "optimal_moisture": 70,
        "water_per_irrigation": 30,  # mm
        "growth_stages": {
            "seedling": {"water_factor": 0.7, "critical_moisture": 55},
            "growing": {"water_factor": 1.0, "critical_moisture": 50},
            "mature": {"water_factor": 0.8, "critical_moisture": 45}
        }
    },
    "onion": {
        "critical_moisture": 40,
        "optimal_moisture": 60,
        "water_per_irrigation": 25,  # mm
        "growth_stages": {
            "seedling": {"water_factor": 0.7, "critical_moisture": 45},
            "growing": {"water_factor": 1.0, "critical_moisture": 40},
            "mature": {"water_factor": 0.5, "critical_moisture": 35}
        }
    }
}


def analyze_irrigation_needs(user_conditions: Dict) -> Dict:
    """Analyze irrigation needs based on crop and soil conditions"""
    crop_type = user_conditions["crop_type"].lower()
    soil_moisture = user_conditions["soil_moisture"]
    growth_stage = user_conditions["growth_stage"].lower()
    temperature = user_conditions["temperature"]
    humidity = user_conditions["humidity"]
    rainfall_forecast = user_conditions.get("rainfall_forecast", 0.0)

    # Get crop data
    if crop_type not in CROP_WATER_NEEDS:
        return {
            "irrigation_needed": False,
            "recommendation": f"Crop type '{crop_type}' not in database. Using general guidelines.",
            "water_amount": 0,
            "urgency": "low",
            "next_check_time": "24 hours"
        }

    crop_data = CROP_WATER_NEEDS[crop_type]
    stage_data = crop_data["growth_stages"].get(growth_stage, crop_data["growth_stages"]["growing"])

    # Calculate critical moisture for current growth stage
    critical_moisture = stage_data["critical_moisture"]
    optimal_moisture = crop_data["optimal_moisture"]

    # Adjust for temperature and humidity
    temp_factor = 1.0 + (temperature - 25) * 0.02 if temperature > 25 else 1.0
    humidity_factor = 1.0 - (humidity - 50) * 0.01 if humidity > 50 else 1.0

    # Calculate adjusted critical moisture
    adjusted_critical = critical_moisture * temp_factor * humidity_factor

    # Determine irrigation need
    irrigation_needed = soil_moisture < adjusted_critical

    # Calculate water amount
    if irrigation_needed:
        water_deficit = adjusted_critical - soil_moisture
        base_water = crop_data["water_per_irrigation"]
        stage_factor = stage_data["water_factor"]
        water_amount = round(base_water * stage_factor * (1 + water_deficit / 20), 1)
    else:
        water_amount = 0

    # Determine urgency
    if soil_moisture < adjusted_critical * 0.7:
        urgency = "high"
    elif soil_moisture < adjusted_critical * 0.9:
        urgency = "medium"
    else:
        urgency = "low"

    # Check rainfall forecast
    if rainfall_forecast > 10:  # More than 10mm expected
        irrigation_needed = False
        water_amount = 0
        urgency = "low"
        recommendation = f"Rainfall expected ({rainfall_forecast}mm). Irrigation not needed. Check again after rain."
    elif irrigation_needed:
        recommendation = f"Irrigation needed. Soil moisture ({soil_moisture}%) below critical level ({adjusted_critical:.1f}%). Apply {water_amount}mm water."
    else:
        recommendation = f"Soil moisture adequate ({soil_moisture}%). No irrigation needed currently."

    # Determine next check time
    if urgency == "high":
        next_check = "6 hours"
    elif urgency == "medium":
        next_check = "12 hours"
    else:
        next_check = "24 hours"

    return {
        "irrigation_needed": irrigation_needed,
        "recommendation": recommendation,
        "water_amount": water_amount,
        "urgency": urgency,
        "next_check_time": next_check
    }