"""
Weather Intelligence Service
Rule-based weather analysis and recommendations.
"""
from typing import Dict


def analyze_weather_conditions(weather_data: Dict) -> Dict:
    """Analyze weather conditions and provide farming recommendations"""
    location = weather_data["location"]
    current_temp = weather_data["current_temp"]
    current_humidity = weather_data["current_humidity"]
    rainfall_expected = weather_data.get("rainfall_expected", False)
    wind_speed = weather_data.get("wind_speed", 0.0)

    # Determine current conditions summary
    conditions = []
    if current_temp > 35:
        conditions.append("extremely hot")
    elif current_temp > 30:
        conditions.append("hot")
    elif current_temp > 20:
        conditions.append("warm")
    elif current_temp > 10:
        conditions.append("moderate")
    else:
        conditions.append("cold")

    if current_humidity > 80:
        conditions.append("very humid")
    elif current_humidity > 60:
        conditions.append("humid")
    elif current_humidity < 30:
        conditions.append("dry")

    if rainfall_expected:
        conditions.append("rain expected")

    if wind_speed > 20:
        conditions.append("windy")

    current_conditions = ", ".join(conditions).capitalize()

    # Risk assessment
    risks = []
    risk_level = "low"

    if current_temp > 35:
        risks.append("High temperature stress risk for crops")
        risk_level = "medium"

    if current_humidity > 80 and current_temp > 25:
        risks.append("High disease risk due to heat and humidity")
        risk_level = "high"

    if rainfall_expected and current_humidity > 70:
        risks.append("Fungal disease risk with rain and high humidity")
        risk_level = "medium"

    if current_temp < 5:
        risks.append("Frost damage risk for sensitive crops")
        risk_level = "high"

    if wind_speed > 25:
        risks.append("Physical damage risk from strong winds")
        risk_level = "medium"

    if not risks:
        risks.append("Current conditions are favorable for most crops")

    risk_assessment = f"{risk_level.upper()} RISK: " + "; ".join(risks)

    # Generate recommendations
    recommendations = []

    # Temperature-based recommendations
    if current_temp > 35:
        recommendations.append("Increase irrigation frequency to prevent heat stress")
        recommendations.append("Provide shade or mulching for sensitive crops")
        recommendations.append("Avoid chemical spraying during peak heat hours")
    elif current_temp < 10:
        recommendations.append("Reduce irrigation to prevent waterlogging")
        recommendations.append("Consider frost protection measures")
    elif current_temp > 25 and current_humidity < 40:
        recommendations.append("Ensure adequate irrigation for heat stress prevention")

    # Humidity-based recommendations
    if current_humidity > 80:
        recommendations.append("Monitor crops closely for fungal diseases")
        recommendations.append("Improve air circulation around plants")
        recommendations.append("Avoid overhead irrigation if possible")
    elif current_humidity < 30:
        recommendations.append("Increase irrigation frequency")
        recommendations.append("Consider drought-resistant crops if this persists")

    # Rainfall-based recommendations
    if rainfall_expected:
        recommendations.append("Delay irrigation - natural rainfall expected")
        recommendations.append("Ensure proper drainage to prevent waterlogging")
        recommendations.append("Postpone any chemical applications until after rain")
    else:
        recommendations.append("Plan irrigation based on current soil moisture")

    # Wind-based recommendations
    if wind_speed > 20:
        recommendations.append("Secure young plants and provide windbreaks")
        recommendations.append("Avoid spraying chemicals during high winds")
        recommendations.append("Check irrigation systems for wind damage")

    # General recommendations
    recommendations.append("Monitor crop health regularly")
    recommendations.append("Adjust farming activities based on weather changes")

    # Determine if immediate action is required
    action_required = risk_level in ["high"]

    # Priority actions
    priority_actions = []
    if action_required:
        if current_temp > 35:
            priority_actions.append("URGENT: Increase irrigation immediately to prevent heat stress")
        if current_humidity > 80 and current_temp > 25:
            priority_actions.append("URGENT: Apply preventive fungicides for disease protection")
        if current_temp < 5:
            priority_actions.append("URGENT: Implement frost protection measures")
        if wind_speed > 25:
            priority_actions.append("URGENT: Secure plants and structures against wind damage")

    return {
        "current_conditions": current_conditions,
        "risk_assessment": risk_assessment,
        "recommendations": recommendations,
        "action_required": action_required,
        "priority_actions": priority_actions
    }