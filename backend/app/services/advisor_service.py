"""
Agentic Advisor Service
Decision-making engine that analyzes multiple farm factors and provides actionable recommendations.
"""
from typing import Dict


def analyze_farm_situation(advisor_data: Dict) -> Dict:
    """Analyze farm situation and make data-driven decisions"""
    crop_type = advisor_data["crop_type"].lower()
    disease_status = advisor_data["disease_status"].lower()
    soil_moisture = advisor_data["soil_moisture"]
    weather_forecast = advisor_data["weather_forecast"].lower()
    growth_stage = advisor_data["growth_stage"].lower()

    # Decision logic based on multiple factors
    decision_factors = []
    urgency_score = 0

    # Disease analysis
    if disease_status == "diseased":
        decision_factors.append("Disease detected - immediate treatment required")
        urgency_score += 30
    elif "healthy" not in disease_status:
        decision_factors.append(f"Disease status: {disease_status} - monitoring required")
        urgency_score += 10

    # Soil moisture analysis
    if soil_moisture < 30:
        decision_factors.append("Critical water stress - irrigation urgent")
        urgency_score += 25
    elif soil_moisture < 50:
        decision_factors.append("Moderate water stress - irrigation needed")
        urgency_score += 15
    elif soil_moisture > 80:
        decision_factors.append("Excess moisture - risk of waterlogging")
        urgency_score += 10

    # Weather analysis
    if weather_forecast == "poor":
        decision_factors.append("Poor weather forecast - protective measures needed")
        urgency_score += 20
    elif weather_forecast == "moderate":
        decision_factors.append("Moderate weather - normal monitoring")
        urgency_score += 5

    # Growth stage vulnerability
    if growth_stage == "seedling":
        decision_factors.append("Seedling stage - high vulnerability")
        urgency_score += 10
    elif growth_stage == "mature":
        decision_factors.append("Mature stage - harvest timing important")
        urgency_score += 5

    # Make decision based on urgency score
    if urgency_score >= 50:
        decision = "IMMEDIATE INTERVENTION REQUIRED"
        priority = "urgent"
        reasoning = f"Critical situation identified: {', '.join(decision_factors)}. Immediate action required to prevent crop loss."
        action_steps = [
            "Implement emergency measures immediately",
            "Increase monitoring frequency to every 6 hours",
            "Apply appropriate treatments based on identified issues",
            "Consider temporary protective measures if weather is poor",
            "Document all actions taken for analysis"
        ]
        follow_up = "6 hours"
        monitoring_required = True

    elif urgency_score >= 30:
        decision = "PRIORITY ACTION NEEDED"
        priority = "high"
        reasoning = f"Significant concerns identified: {', '.join(decision_factors)}. Action required within 24 hours."
        action_steps = [
            "Address identified issues within 24 hours",
            "Increase monitoring to every 12 hours",
            "Apply recommended treatments",
            "Prepare contingency plans if conditions worsen"
        ]
        follow_up = "12 hours"
        monitoring_required = True

    elif urgency_score >= 15:
        decision = "MONITORING AND PLANNING"
        priority = "medium"
        reasoning = f"Moderate concerns: {', '.join(decision_factors)}. Continue monitoring and prepare for potential action."
        action_steps = [
            "Continue regular monitoring",
            "Prepare resources for potential intervention",
            "Review and adjust farming practices if needed",
            "Monitor weather forecasts closely"
        ]
        follow_up = "24 hours"
        monitoring_required = True

    else:
        decision = "ROUTINE MONITORING"
        priority = "low"
        reasoning = f"Conditions are stable: {', '.join(decision_factors) if decision_factors else 'No immediate concerns'}. Continue normal farming practices."
        action_steps = [
            "Continue standard farming practices",
            "Monitor crops regularly",
            "Maintain irrigation and fertilization schedules",
            "Watch for any changes in conditions"
        ]
        follow_up = "48 hours"
        monitoring_required = False

    return {
        "decision": decision,
        "reasoning": reasoning,
        "priority": priority,
        "action_steps": action_steps,
        "monitoring_required": monitoring_required,
        "follow_up_time": follow_up
    }