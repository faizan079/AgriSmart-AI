"""
Farmer Assistant Service
Simplified rule-based assistant implementation (no API key required).
"""
from typing import Dict


# Knowledge base for common farming questions
KNOWLEDGE_BASE = {
    "disease": {
        "keywords": ["disease", "sick", "infected", "fungus", "bacteria", "virus", "symptoms"],
        "response": "For disease management, I recommend: 1) Identify the specific disease using our disease detection feature, 2) Remove affected plant parts, 3) Apply appropriate fungicides or pesticides, 4) Improve air circulation, 5) Avoid overhead irrigation. Early detection is key to preventing spread."
    },
    "irrigation": {
        "keywords": ["water", "irrigation", "dry", "moisture", "drought"],
        "response": "For irrigation guidance: Check soil moisture before watering. Most crops need 2.5-5cm water per week. Use drip irrigation for efficiency. Water early morning or late evening to reduce evaporation. Our Smart Irrigation feature can provide specific recommendations based on your crop and conditions."
    },
    "fertilizer": {
        "keywords": ["fertilizer", "nutrient", "feed", "growth", "yellow leaves"],
        "response": "For fertilization: Conduct soil testing to determine nutrient needs. Generally, apply nitrogen during vegetative growth, phosphorus during flowering, and potassium during fruit development. Organic options include compost, manure, and green manures. Over-fertilization can harm crops and environment."
    },
    "pest": {
        "keywords": ["pest", "insect", "bug", "worm", "attack", "damage"],
        "response": "For pest management: Use integrated pest management (IPM) approach. 1) Monitor regularly, 2) Use beneficial insects, 3) Apply pesticides only when necessary, 4) Rotate crops to break pest cycles, 5) Maintain field hygiene. Natural predators and organic pesticides can reduce chemical dependency."
    },
    "soil": {
        "keywords": ["soil", "earth", "land", "ph", "acidity", "alkaline"],
        "response": "For soil health: Maintain pH between 6.0-7.0 for most crops. Add organic matter regularly. Test soil annually. Use cover crops to prevent erosion. Avoid excessive tillage. Our Crop Recommendation feature considers soil conditions for optimal crop selection."
    },
    "weather": {
        "keywords": ["weather", "rain", "temperature", "climate", "season"],
        "response": "For weather adaptation: Plan activities based on forecasts. Protect crops from extreme weather. Use mulching for temperature regulation. Ensure proper drainage for heavy rain. Our Weather Intelligence feature provides specific recommendations based on current conditions."
    },
    "harvest": {
        "keywords": ["harvest", "pick", "ready", "mature", "collect"],
        "response": "For harvesting: Harvest at peak maturity for best quality. Use proper tools to avoid damage. Harvest early morning when temperatures are cool. Post-harvest handling is crucial for storage life. Different crops have different indicators of readiness."
    },
    "crop": {
        "keywords": ["crop", "plant", "grow", "cultivate", "variety"],
        "response": "For crop selection: Consider soil type, climate, water availability, and market demand. Use our Crop Recommendation feature for personalized suggestions. Crop rotation prevents soil depletion and reduces pest problems. Choose disease-resistant varieties when available."
    },
    "sustainability": {
        "keywords": ["sustainable", "environment", "eco", "organic", "green"],
        "response": "For sustainable farming: Use water efficiently, minimize chemical inputs, practice crop rotation, maintain soil health, use renewable energy when possible. Our Sustainability Score feature helps assess your current practices and suggests improvements."
    },
    "yield": {
        "keywords": ["yield", "production", "output", "productivity", "increase"],
        "response": "For improving yield: Use quality seeds, proper spacing, adequate nutrition, pest management, and timely irrigation. Our Water & Yield Prediction feature can estimate your potential yield based on current practices and suggest optimizations."
    }
}


def get_assistant_response(request_data: Dict) -> Dict:
    """Generate response based on farming knowledge base"""
    question = request_data["question"].lower()
    context = request_data.get("context", "").lower()

    # Find best matching topic
    best_match = None
    best_score = 0

    for topic, data in KNOWLEDGE_BASE.items():
        score = 0
        for keyword in data["keywords"]:
            if keyword in question:
                score += 1
            if keyword in context:
                score += 0.5

        if score > best_score:
            best_score = score
            best_match = topic

    # Generate response
    if best_match and best_score > 0:
        response = KNOWLEDGE_BASE[best_match]["response"]
        confidence = min(0.9, 0.5 + best_score * 0.1)
        related_topics = [topic.title() for topic in KNOWLEDGE_BASE.keys() if topic != best_match][:3]
    else:
        response = "I can help with farming questions about diseases, irrigation, fertilizers, pests, soil health, weather adaptation, harvesting, crop selection, sustainability, and yield improvement. Please ask a specific question about any of these topics, or use our specialized features for detailed analysis."
        confidence = 0.3
        related_topics = list(KNOWLEDGE_BASE.keys())[:3]

    return {
        "answer": response,
        "confidence": round(confidence, 2),
        "related_topics": related_topics
    }