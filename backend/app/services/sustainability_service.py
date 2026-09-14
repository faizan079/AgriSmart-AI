"""
Sustainability Score Service
Formula-based sustainability assessment for farming practices.
"""
from typing import Dict


# Crop-specific baseline values for comparison
CROP_BASELINES = {
    "rice": {
        "water_per_kg": 2500,  # liters per kg
        "fertilizer_per_kg": 0.05,  # kg per kg
        "pesticide_per_kg": 0.02,  # liters per kg
        "energy_per_kg": 0.5  # kWh per kg
    },
    "wheat": {
        "water_per_kg": 1500,
        "fertilizer_per_kg": 0.04,
        "pesticide_per_kg": 0.015,
        "energy_per_kg": 0.3
    },
    "maize": {
        "water_per_kg": 1200,
        "fertilizer_per_kg": 0.045,
        "pesticide_per_kg": 0.018,
        "energy_per_kg": 0.25
    },
    "cotton": {
        "water_per_kg": 2000,
        "fertilizer_per_kg": 0.06,
        "pesticide_per_kg": 0.03,
        "energy_per_kg": 0.8
    },
    "sugarcane": {
        "water_per_kg": 1800,
        "fertilizer_per_kg": 0.055,
        "pesticide_per_kg": 0.025,
        "energy_per_kg": 0.6
    },
    "groundnut": {
        "water_per_kg": 800,
        "fertilizer_per_kg": 0.03,
        "pesticide_per_kg": 0.01,
        "energy_per_kg": 0.2
    },
    "soybean": {
        "water_per_kg": 900,
        "fertilizer_per_kg": 0.025,
        "pesticide_per_kg": 0.008,
        "energy_per_kg": 0.25
    },
    "potato": {
        "water_per_kg": 200,
        "fertilizer_per_kg": 0.02,
        "pesticide_per_kg": 0.012,
        "energy_per_kg": 0.15
    },
    "tomato": {
        "water_per_kg": 180,
        "fertilizer_per_kg": 0.018,
        "pesticide_per_kg": 0.015,
        "energy_per_kg": 0.2
    },
    "onion": {
        "water_per_kg": 250,
        "fertilizer_per_kg": 0.022,
        "pesticide_per_kg": 0.01,
        "energy_per_kg": 0.18
    }
}


def calculate_sustainability_score(farming_data: Dict) -> Dict:
    """Calculate overall sustainability score based on farming practices"""
    crop_type = farming_data["crop_type"].lower()
    water_usage = farming_data["water_usage"]
    fertilizer_usage = farming_data["fertilizer_usage"]
    pesticide_usage = farming_data["pesticide_usage"]
    crop_yield = farming_data["crop_yield"]
    irrigation_efficiency = farming_data["irrigation_efficiency"]
    soil_health = farming_data["soil_health"].lower()
    energy_usage = farming_data.get("energy_usage", 0.0)

    # Get crop baseline or use average
    baseline = CROP_BASELINES.get(crop_type, {
        "water_per_kg": 1500,
        "fertilizer_per_kg": 0.04,
        "pesticide_per_kg": 0.015,
        "energy_per_kg": 0.3
    })

    # Calculate Water Efficiency Score (0-100)
    if crop_yield > 0:
        water_per_kg = water_usage / crop_yield
        water_ratio = baseline["water_per_kg"] / water_per_kg if water_per_kg > 0 else 0
        water_efficiency_score = min(100, max(0, water_ratio * 50))  # 50% of baseline = 50 points
    else:
        water_efficiency_score = 0

    # Adjust for irrigation efficiency
    water_efficiency_score = water_efficiency_score * (irrigation_efficiency / 100)

    # Calculate Resource Usage Score (0-100)
    if crop_yield > 0:
        fertilizer_per_kg = fertilizer_usage / crop_yield
        pesticide_per_kg = pesticide_usage / crop_yield
        energy_per_kg = energy_usage / crop_yield if energy_usage > 0 else 0

        fertilizer_ratio = baseline["fertilizer_per_kg"] / fertilizer_per_kg if fertilizer_per_kg > 0 else 1
        pesticide_ratio = baseline["pesticide_per_kg"] / pesticide_per_kg if pesticide_per_kg > 0 else 1
        energy_ratio = baseline["energy_per_kg"] / energy_per_kg if energy_per_kg > 0 else 1

        resource_score = min(100, max(0, (
            fertilizer_ratio * 0.4 +
            pesticide_ratio * 0.4 +
            energy_ratio * 0.2
        ) * 50))
    else:
        resource_score = 0

    # Calculate Environmental Impact Score (0-100)
    soil_health_scores = {"poor": 20, "moderate": 50, "good": 80}
    soil_score = soil_health_scores.get(soil_health, 50)

    # Penalty for high pesticide and fertilizer use
    environmental_penalty = 0
    if crop_yield > 0:
        fertilizer_per_kg = fertilizer_usage / crop_yield
        pesticide_per_kg = pesticide_usage / crop_yield
        if fertilizer_per_kg > baseline["fertilizer_per_kg"] * 1.5:
            environmental_penalty += 20
        if pesticide_per_kg > baseline["pesticide_per_kg"] * 1.5:
            environmental_penalty += 20

    environmental_score = min(100, max(0, soil_score - environmental_penalty))

    # Calculate Overall Sustainability Score
    overall_score = (
        water_efficiency_score * 0.35 +
        resource_score * 0.35 +
        environmental_score * 0.30
    )

    # Determine rating
    if overall_score >= 80:
        rating = "Excellent"
    elif overall_score >= 60:
        rating = "Good"
    elif overall_score >= 40:
        rating = "Fair"
    else:
        rating = "Poor"

    # Generate recommendations
    recommendations = []
    improvement_areas = []

    if water_efficiency_score < 50:
        recommendations.append("Improve water efficiency through drip irrigation or mulching")
        improvement_areas.append("Water Efficiency")

    if resource_score < 50:
        recommendations.append("Optimize fertilizer and pesticide use based on soil testing")
        improvement_areas.append("Resource Management")

    if environmental_score < 50:
        recommendations.append("Focus on soil health through organic matter addition and crop rotation")
        improvement_areas.append("Environmental Impact")

    if irrigation_efficiency < 70:
        recommendations.append("Upgrade irrigation systems to improve water efficiency")
        improvement_areas.append("Irrigation Infrastructure")

    if soil_health == "poor":
        recommendations.append("Implement soil testing and organic farming practices")
        improvement_areas.append("Soil Health Management")

    if pesticide_usage > baseline["pesticide_per_kg"] * crop_yield * 1.2:
        recommendations.append("Consider integrated pest management to reduce pesticide dependency")
        improvement_areas.append("Pest Management")

    # Add positive recommendations if scores are good
    if water_efficiency_score >= 70:
        recommendations.append("Excellent water efficiency - maintain current practices")

    if environmental_score >= 70:
        recommendations.append("Good environmental practices - continue sustainable farming")

    # Score breakdown
    score_breakdown = {
        "water_efficiency": round(water_efficiency_score, 1),
        "resource_usage": round(resource_score, 1),
        "environmental_impact": round(environmental_score, 1)
    }

    return {
        "sustainability_score": round(overall_score, 1),
        "score_breakdown": score_breakdown,
        "rating": rating,
        "water_efficiency_score": round(water_efficiency_score, 1),
        "resource_usage_score": round(resource_score, 1),
        "environmental_impact_score": round(environmental_score, 1),
        "recommendations": recommendations,
        "improvement_areas": improvement_areas
    }