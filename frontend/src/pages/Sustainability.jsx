import { useState } from 'react'
import './Sustainability.css'

export default function Sustainability() {
  const [formData, setFormData] = useState({
    water_usage: 5000,
    fertilizer_usage: 50,
    pesticide_usage: 20,
    crop_yield: 1000,
    crop_type: 'tomato',
    irrigation_efficiency: 70,
    soil_health: 'moderate',
    energy_usage: 100
  })
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState('')

  function handleChange(event) {
    const { name, value } = event.target
    setFormData(prev => ({
      ...prev,
      [name]: name.includes('_usage') || name.includes('_yield') || name.includes('_efficiency') ? parseFloat(value) : value
    }))
    setResult(null)
    setError('')
  }

  async function handleCalculate() {
    setLoading(true)
    setError('')
    setResult(null)

    try {
      const response = await fetch('/api/sustainability/score', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      })
      const data = await response.json()
      if (!response.ok) {
        throw new Error(data.detail || data.message || 'Calculation failed')
      }
      setResult(data.data)
    } catch (err) {
      setError(err.message || 'Could not reach backend. Is the server running?')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <h1 className="page-title">Sustainability Score</h1>
      <p className="page-subtitle">Assess the environmental impact and efficiency of your farming practices.</p>

      <div className="card sustainability-card">
        <div className="form-grid">
          <div className="form-group">
            <label>Crop Type</label>
            <select name="crop_type" value={formData.crop_type} onChange={handleChange}>
              <option value="rice">Rice</option>
              <option value="wheat">Wheat</option>
              <option value="maize">Maize</option>
              <option value="cotton">Cotton</option>
              <option value="sugarcane">Sugarcane</option>
              <option value="groundnut">Groundnut</option>
              <option value="soybean">Soybean</option>
              <option value="potato">Potato</option>
              <option value="tomato">Tomato</option>
              <option value="onion">Onion</option>
            </select>
          </div>

          <div className="form-group">
            <label>Water Usage (liters/day)</label>
            <input
              type="number"
              name="water_usage"
              min="0"
              value={formData.water_usage}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Fertilizer Usage (kg/season)</label>
            <input
              type="number"
              name="fertilizer_usage"
              min="0"
              value={formData.fertilizer_usage}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Pesticide Usage (liters/season)</label>
            <input
              type="number"
              name="pesticide_usage"
              min="0"
              value={formData.pesticide_usage}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Crop Yield (kg/season)</label>
            <input
              type="number"
              name="crop_yield"
              min="0"
              value={formData.crop_yield}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Irrigation Efficiency (%)</label>
            <input
              type="number"
              name="irrigation_efficiency"
              min="0"
              max="100"
              value={formData.irrigation_efficiency}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Soil Health</label>
            <select name="soil_health" value={formData.soil_health} onChange={handleChange}>
              <option value="poor">Poor</option>
              <option value="moderate">Moderate</option>
              <option value="good">Good</option>
            </select>
          </div>

          <div className="form-group">
            <label>Energy Usage (kWh/season)</label>
            <input
              type="number"
              name="energy_usage"
              min="0"
              value={formData.energy_usage}
              onChange={handleChange}
            />
          </div>
        </div>

        <button
          type="button"
          className="primary-btn"
          onClick={handleCalculate}
          disabled={loading}
        >
          {loading ? 'Calculating...' : 'Calculate Sustainability Score'}
        </button>

        {error && <div className="alert error">{error}</div>}

        {result && (
          <div className="result-card">
            <h3>Sustainability Assessment</h3>
            <div className="score-display">
              <div className="overall-score">
                <span className="score-number">{result.sustainability_score}</span>
                <span className="score-label">Overall Score</span>
              </div>
              <div className={`rating ${result.rating.toLowerCase()}`}>
                {result.rating}
              </div>
            </div>

            <div className="score-breakdown">
              <h4>Score Breakdown</h4>
              <div className="breakdown-item">
                <span>Water Efficiency</span>
                <div className="progress-bar">
                  <div className="progress" style={{ width: `${result.water_efficiency_score}%` }}></div>
                </div>
                <span>{result.water_efficiency_score}%</span>
              </div>
              <div className="breakdown-item">
                <span>Resource Usage</span>
                <div className="progress-bar">
                  <div className="progress" style={{ width: `${result.resource_usage_score}%` }}></div>
                </div>
                <span>{result.resource_usage_score}%</span>
              </div>
              <div className="breakdown-item">
                <span>Environmental Impact</span>
                <div className="progress-bar">
                  <div className="progress" style={{ width: `${result.environmental_impact_score}%` }}></div>
                </div>
                <span>{result.environmental_impact_score}%</span>
              </div>
            </div>

            {result.improvement_areas.length > 0 && (
              <div className="improvement-areas">
                <h4>Areas for Improvement</h4>
                <ul>
                  {result.improvement_areas.map((area, index) => (
                    <li key={index}>{area}</li>
                  ))}
                </ul>
              </div>
            )}

            <div className="recommendations">
              <h4>Recommendations</h4>
              <ul>
                {result.recommendations.map((rec, index) => (
                  <li key={index}>{rec}</li>
                ))}
              </ul>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}