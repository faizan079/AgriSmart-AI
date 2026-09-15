# AgriSmart AI

**Intelligent Agriculture for a Sustainable Future** — SIH 2026 Internal Hackathon

AgriSmart AI is an AI-powered smart agriculture platform designed to help farmers make better decisions about crop health, crop selection, irrigation, weather conditions, sustainability, and farm management.

## Features

### 1. AI Crop Disease Detection

The core machine-learning module detects crop diseases from leaf images.

- Upload a crop/leaf image
- Detect disease or healthy condition
- Display prediction result and confidence
- Provide basic precautions and recommendations

The disease detection model is designed to support real-world crop health monitoring.

### 2. Crop Recommendation

Recommends suitable crops based on agricultural and environmental conditions.

Inputs include:

- Soil type
- Soil pH
- Temperature
- Humidity
- Rainfall
- Water availability
- Season
- Location
- Previous crop

The recommendation is dynamically generated from the provided farm conditions.

### 3. Smart Irrigation

Provides irrigation recommendations based on crop and environmental conditions.

The module considers:

- Crop type
- Growth stage
- Soil moisture
- Temperature
- Humidity
- Rainfall/weather conditions

It provides information such as:

- Whether irrigation is required
- Recommended irrigation amount
- Urgency
- Next monitoring/check time
- Reason behind the recommendation

### 4. Weather Intelligence

Combines weather information with agricultural conditions to provide actionable farming recommendations.

Examples include:

- Delaying irrigation when rain is expected
- Monitoring crops during unfavorable weather
- Adjusting farming activities
- Advising precautions during hot, humid, or rainy conditions

### 5. Sustainability Score

Provides an indicative sustainability score based on agricultural resource usage and crop conditions.

The score considers factors such as:

- Water efficiency
- Resource usage
- Crop health
- Irrigation efficiency

The module also provides suggestions for improving sustainable farming practices.

### 6. Innovation Features

AgriSmart AI includes additional intelligent agriculture capabilities:

- Crop Stress Warning
- Crop Rotation Recommendation
- Water & Yield Prediction

These features provide additional decision support beyond basic disease detection.

### 7. Gemini Farmer Assistant

A Gemini-powered AI assistant that allows farmers to ask agriculture-related questions using natural language.

The assistant can provide guidance related to:

- Crop diseases
- Irrigation
- Weather
- Crop management
- Farming precautions
- General agricultural questions

The goal is to provide simple and farmer-friendly explanations.

### 8. Agentic Advisor

The Agentic Advisor combines information from multiple agricultural modules to generate context-aware recommendations.

It can consider:

- Crop information
- Disease status
- Soil moisture
- Weather conditions
- Growth stage
- Irrigation requirements
- Sustainability information

The advisor analyzes the available context and provides an overall action-oriented recommendation.

## Project Structure

```text
AgriSmart-AI/
│
├── backend/
│   └── app/
│       ├── api/
│       ├── services/
│       ├── models/
│       ├── schemas/
│       └── main.py
│
├── frontend/
│   └── src/
│
├── model/
│   ├── training/
│   ├── inference/
│   ├── evaluation/
│   └── weights/
│
├── report/
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md