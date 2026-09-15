"""
Innovation Features Service
Rule-based implementations for crop stress, rotation, and water/yield prediction.
"""
from typing import Dict


def analyze_crop_stress(stress_data: Dict) -> Dict:
    """Analyze crop stress levels based on multiple factors"""
    crop_type = stress_data["crop_type"].lower()
    disease_status = stress_data["disease_status"].lower()
    soil_moisture = stress_data["soil_moisture"]
    temperature = stress_data["temperature"]
    humidity = stress_data["humidity"]
    growth_stage = stress_data["growth_stage"].lower()
    water_stress_indicators = stress_data.get("water_stress_indicators", "none").lower()

    stress_factors = []
    stress_score = 0

    # Disease stress
    if disease_status == "diseased":
        stress_factors.append("Disease infection detected")
        stress_score += 30

    # Water stress analysis
    if soil_moisture < 30:
        stress_factors.append("Severe water stress - soil moisture critically low")
        stress_score += 25
    elif soil_moisture < 50:
        stress_factors.append("Moderate water stress - soil moisture below optimal")
        stress_score += 15

    # Temperature stress
    if temperature > 35:
        stress_factors.append("Heat stress - temperature critically high")
        stress_score += 20
    elif temperature > 30:
        stress_factors.append("Temperature stress - high temperature")
        stress_score += 10
    elif temperature < 10:
        stress_factors.append("Cold stress - temperature too low")
        stress_score += 15

    # Humidity stress
    if humidity > 85:
        stress_factors.append("High humidity stress - disease risk elevated")
        stress_score += 10
    elif humidity < 30:
        stress_factors.append("Low humidity stress - dehydration risk")
        stress_score += 10

    # Visible stress indicators
    if water_stress_indicators != "none":
        stress_factors.append(f"Visible stress indicators: {water_stress_indicators}")
        stress_score += 15

    # Growth stage vulnerability
    if growth_stage == "seedling":
        stress_score += 5  # Seedlings more vulnerable

    # Determine overall stress level
    if stress_score >= 50:
        stress_level = "high"
        risk_assessment = "CRITICAL: Immediate intervention required to prevent crop loss"
    elif stress_score >= 30:
        stress_level = "medium"
        risk_assessment = "MODERATE: Monitoring and intervention needed within 24-48 hours"
    else:
        stress_level = "low"
        risk_assessment = "LOW: Current conditions are manageable with normal monitoring"

    # Generate recommendations
    recommendations = []
    if disease_status == "diseased":
        recommendations.append("Apply appropriate disease treatment immediately")
        recommendations.append("Isolate affected plants if possible")
        recommendations.append("Monitor disease spread closely")

    if soil_moisture < 50:
        recommendations.append("Increase irrigation frequency to address water stress")
        recommendations.append("Consider mulching to retain soil moisture")

    if temperature > 30:
        recommendations.append("Provide shade or windbreaks to reduce heat stress")
        recommendations.append("Increase irrigation during peak heat hours")

    if humidity > 80:
        recommendations.append("Improve air circulation to reduce disease risk")
        recommendations.append("Avoid overhead irrigation")

    if stress_level == "high":
        recommendations.append("Implement emergency stress reduction measures")
        recommendations.append("Consider harvesting early if crop is mature enough")

    return {
        "stress_level": stress_level,
        "stress_factors": stress_factors,
        "risk_assessment": risk_assessment,
        "recommendations": recommendations,
        "monitoring_required": stress_level in ["medium", "high"]
    }


def recommend_crop_rotation(rotation_data: Dict) -> Dict:
    """Recommend next crop based on rotation principles"""
    current_crop = rotation_data["current_crop"].lower()
    previous_crop = rotation_data.get("previous_crop", "").lower()
    soil_type = rotation_data["soil_type"].lower()
    soil_ph = rotation_data["soil_ph"]
    season = rotation_data["season"].lower()
    pest_history = rotation_data.get("pest_history", "none").lower()

    # Crop rotation database
    rotation_rules = {
        "rice": {
            "good_followers": ["wheat", "maize", "groundnut", "soybean"],
            "avoid": ["sugarcane", "cotton"],
            "benefits": ["Nitrogen balance", "Soil structure improvement", "Pest break"]
        },
        "wheat": {
            "good_followers": ["maize", "groundnut", "soybean", "cotton"],
            "avoid": ["rice", "wheat"],
            "benefits": ["Disease break", "Nutrient cycling", "Weed control"]
        },
        "maize": {
            "good_followers": ["wheat", "soybean", "groundnut", "potato"],
            "avoid": ["maize", "sugarcane"],
            "benefits": ["Nitrogen fixation", "Pest management", "Soil health"]
        },
        "cotton": {
            "good_followers": ["wheat", "maize", "groundnut", "sugarcane"],
            "avoid": ["cotton", "okra"],
            "benefits": ["Soil health recovery", "Pest break", "Nutrient balance"]
        },
        "sugarcane": {
            "good_followers": ["wheat", "maize", "groundnut", "soybean"],
            "avoid": ["sugarcane", "rice"],
            "benefits": ["Soil recovery", "Pest management", "Nutrient cycling"]
        },
        "groundnut": {
            "good_followers": ["wheat", "maize", "cotton", "sugarcane"],
            "avoid": ["groundnut", "soybean"],
            "benefits": ["Nitrogen fixation for next crop", "Soil structure", "Pest break"]
        },
        "soybean": {
            "good_followers": ["wheat", "maize", "rice", "cotton"],
            "avoid": ["soybean", "groundnut"],
            "benefits": ["Nitrogen fixation", "Soil health", "Disease break"]
        },
        "potato": {
            "good_followers": ["wheat", "maize", "groundnut", "cotton"],
            "avoid": ["potato", "tomato"],
            "benefits": ["Disease break", "Soil structure", "Pest management"]
        },
        "tomato": {
            "good_followers": ["wheat", "maize", "groundnut", "onion"],
            "avoid": ["tomato", "potato", "brinjal"],
            "benefits": ["Disease break", "Soil health", "Pest management"]
        },
        "onion": {
            "good_followers": ["wheat", "maize", "groundnut", "tomato"],
            "avoid": ["onion", "garlic"],
            "benefits": ["Soil health", "Pest break", "Nutrient cycling"]
        }
    }

    # Get rotation rules for current crop
    rules = rotation_rules.get(current_crop, {
        "good_followers": ["wheat", "maize", "groundnut"],
        "avoid": [current_crop],
        "benefits": ["Soil health improvement", "Pest break", "Nutrient balance"]
    })

    # Filter good followers based on season and soil
    suitable_crops = []
    for crop in rules["good_followers"]:
        # Filter based on soil type compatibility
        soil_compatible = True
        if soil_type == "clay" and crop in ["groundnut", "onion"]:
            soil_compatible = False
        elif soil_type == "sandy" and crop in ["rice", "sugarcane"]:
            soil_compatible = False
        elif soil_type == "black" and crop in ["groundnut", "onion"]:
            soil_compatible = False

        # Filter based on pH compatibility
        ph_compatible = True
        if soil_ph < 5.5 and crop in ["wheat", "maize", "cotton"]:
            ph_compatible = False
        elif soil_ph > 7.5 and crop in ["potato", "groundnut"]:
            ph_compatible = False

        # Filter based on season compatibility
        season_compatible = True
        if season == "winter" and crop in ["rice", "sugarcane", "groundnut"]:
            season_compatible = False
        elif season == "summer" and crop in ["wheat", "potato"]:
            season_compatible = False

        if soil_compatible and ph_compatible and season_compatible:
            suitable_crops.append(crop)

    # Create a deterministic scoring system based on input combinations
    crop_scores = []
    
    # Create a hash of the input parameters for deterministic but varied results
    input_hash = abs(hash(f"{current_crop}_{soil_type}_{soil_ph}_{season}"))
    
    for i, crop in enumerate(rules["good_followers"]):
        score = 0
        
        # Avoid same crop
        if crop == current_crop:
            score -= 10
            continue
        
        # Use the input hash to vary scoring - same inputs always give same result
        score += (input_hash + i) % 5
        
        # Current crop specific prioritization
        if current_crop == "rice":
            if crop == "wheat": score += 3
            elif crop == "maize": score += 2
            elif crop == "groundnut": score += 2
        elif current_crop == "wheat":
            if crop == "maize": score += 3
            elif crop == "groundnut": score += 2
            elif crop == "cotton": score += 2
        elif current_crop == "maize":
            if crop == "wheat": score += 3
            elif crop == "soybean": score += 2
            elif crop == "groundnut": score += 2
        elif current_crop == "cotton":
            if crop == "wheat": score += 3
            elif crop == "maize": score += 2
            elif crop == "groundnut": score += 2
        elif current_crop == "tomato":
            if crop == "wheat": score += 3
            elif crop == "maize": score += 2
            elif crop == "groundnut": score += 2
        elif current_crop == "groundnut":
            if crop == "wheat": score += 3
            elif crop == "maize": score += 2
            elif crop == "cotton": score += 2
        elif current_crop == "soybean":
            if crop == "wheat": score += 3
            elif crop == "maize": score += 2
            elif crop == "cotton": score += 2
        
        # Soil type influence
        if soil_type == "clay":
            if crop in ["rice", "wheat", "cotton"]: score += 2
        elif soil_type == "sandy":
            if crop in ["groundnut", "soybean", "maize"]: score += 2
        elif soil_type == "loamy":
            if crop in ["wheat", "maize", "groundnut"]: score += 1
        elif soil_type == "black":
            if crop in ["cotton", "wheat", "maize"]: score += 2
        
        # Season influence
        if season == "summer":
            if crop in ["rice", "maize", "cotton"]: score += 2
        elif season == "winter":
            if crop in ["wheat", "mustard", "chickpea"]: score += 2
        elif season == "monsoon":
            if crop in ["rice", "groundnut"]: score += 2
        elif season == "spring":
            if crop in ["maize", "groundnut"]: score += 2
        
        # pH influence
        if 6.0 <= soil_ph <= 7.0:
            score += 1
        elif soil_ph < 6.0:
            if crop in ["potato", "groundnut"]: score += 2
        elif soil_ph > 7.0:
            if crop in ["wheat", "maize"]: score += 2
        
        crop_scores.append((crop, score))
    
    # Sort by score and select best
    crop_scores.sort(key=lambda x: x[1], reverse=True)
    
    # Avoid crops with pest history
    if pest_history != "none" and previous_crop:
        # Avoid crops from same family if pest history exists
        if previous_crop in ["tomato", "potato", "brinjal"]:
            # Nightshade family - avoid tomatoes, potatoes, brinjal
            crop_scores = [(c, s) for c, s in crop_scores if c not in ["tomato", "potato", "brinjal"]]
        elif previous_crop in ["groundnut", "soybean"]:
            # Legume family - avoid other legumes
            crop_scores = [(c, s) for c, s in crop_scores if c not in ["groundnut", "soybean"]]
    
    # Select best recommendation
    if crop_scores:
        recommended_next_crop = crop_scores[0][0].title()
        alternatives = [crop[0].title() for crop in crop_scores[1:4]]
    else:
        recommended_next_crop = "Wheat"  # Default safe option
        alternatives = ["Maize", "Groundnut"]

    # Determine soil health impact
    if current_crop in ["groundnut", "soybean"]:
        soil_impact = "Positive - Nitrogen fixation improves soil fertility"
    elif current_crop in ["rice", "sugarcane"]:
        soil_impact = "Moderate - May require soil amendments"
    else:
        soil_impact = "Neutral - Standard soil impact"

    # Timing recommendation
    season_timing = {
        "summer": "Rotate after monsoon for winter crops",
        "winter": "Rotate after harvest for summer crops",
        "monsoon": "Rotate after monsoon for winter crops",
        "spring": "Rotate after spring harvest for summer crops"
    }

    return {
        "recommended_next_crop": recommended_next_crop,
        "rotation_benefits": rules["benefits"],
        "soil_health_impact": soil_impact,
        "timing_recommendation": season_timing.get(season, "Rotate after current crop harvest"),
        "alternatives": alternatives
    }


def predict_water_yield(prediction_data: Dict) -> Dict:
    """Predict water requirements and yield estimates"""
    crop_type = prediction_data["crop_type"].lower()
    area_hectares = prediction_data["area_hectares"]
    current_water_usage = prediction_data["current_water_usage"]
    soil_quality = prediction_data["soil_quality"].lower()
    weather_conditions = prediction_data["weather_conditions"].lower()
    irrigation_method = prediction_data["irrigation_method"].lower()

    # Crop-specific water and yield data
    crop_data = {
        "rice": {"water_per_hectare": 25000, "yield_per_hectare": 5000},
        "wheat": {"water_per_hectare": 15000, "yield_per_hectare": 3000},
        "maize": {"water_per_hectare": 12000, "yield_per_hectare": 4000},
        "cotton": {"water_per_hectare": 20000, "yield_per_hectare": 2000},
        "sugarcane": {"water_per_hectare": 18000, "yield_per_hectare": 8000},
        "groundnut": {"water_per_hectare": 8000, "yield_per_hectare": 1500},
        "soybean": {"water_per_hectare": 9000, "yield_per_hectare": 2000},
        "potato": {"water_per_hectare": 2000, "yield_per_hectare": 2500},
        "tomato": {"water_per_hectare": 1800, "yield_per_hectare": 3000},
        "onion": {"water_per_hectare": 2500, "yield_per_hectare": 2000}
    }

    crop_info = crop_data.get(crop_type, {"water_per_hectare": 15000, "yield_per_hectare": 3000})

    # Adjust water requirement based on irrigation method
    irrigation_efficiency = {
        "drip": 0.9,
        "sprinkler": 0.75,
        "flood": 0.5
    }

    efficiency = irrigation_efficiency.get(irrigation_method, 0.7)
    base_water_requirement = crop_info["water_per_hectare"] * area_hectares
    estimated_water_requirement = base_water_requirement / efficiency

    # Adjust yield based on soil quality and weather
    soil_factor = {"good": 1.2, "moderate": 1.0, "poor": 0.7}
    weather_factor = {"excellent": 1.1, "good": 1.0, "moderate": 0.9, "poor": 0.75}

    soil_multiplier = soil_factor.get(soil_quality, 1.0)
    weather_multiplier = weather_factor.get(weather_conditions, 1.0)

    base_yield = crop_info["yield_per_hectare"] * area_hectares
    estimated_yield = base_yield * soil_multiplier * weather_multiplier

    # Calculate yield range
    yield_range_low = estimated_yield * 0.8
    yield_range_high = estimated_yield * 1.2
    yield_range = f"{int(yield_range_low)} - {int(yield_range_high)} kg"

    # Calculate water efficiency score
    if current_water_usage > 0:
        water_efficiency_score = min(100, (base_water_requirement / current_water_usage) * 100)
    else:
        water_efficiency_score = 50  # Default score

    # Generate optimization tips
    optimization_tips = []

    if irrigation_method == "flood":
        optimization_tips.append("Consider switching to drip irrigation for 40-50% water savings")
        optimization_tips.append("Implement laser leveling for better flood irrigation efficiency")

    if soil_quality == "poor":
        optimization_tips.append("Improve soil quality through organic matter addition")
        optimization_tips.append("Consider soil testing and targeted amendments")

    if weather_conditions == "poor":
        optimization_tips.append("Plan for drought-resistant varieties if poor weather persists")
        optimization_tips.append("Implement water conservation measures")

    if water_efficiency_score < 70:
        optimization_tips.append("Current water usage is inefficient - review irrigation practices")
        optimization_tips.append("Consider soil moisture sensors for precision irrigation")

    optimization_tips.append("Monitor crop growth stages for precise water application")
    optimization_tips.append("Consider mulching to reduce water evaporation")

    return {
        "estimated_water_requirement": round(estimated_water_requirement, 0),
        "estimated_yield": round(estimated_yield, 0),
        "yield_range": yield_range,
        "water_efficiency_score": round(water_efficiency_score, 1),
        "optimization_tips": optimization_tips
    }