import { useState } from 'react'
import './CropRecommendation.css'

export default function CropRecommendation() {
  const [formData, setFormData] = useState({
    soil_type: 'loamy',
    soil_ph: 6.5,
    temperature: 25,
    humidity: 60,
    rainfall: 800,
    water_availability: 'medium',
    season: 'summer',
    location: '',
    previous_crop: ''
  })
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState('')

  function handleChange(event) {
    const { name, value } = event.target
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))
    setResult(null)
    setError('')
  }

  async function handleRecommend() {
    setLoading(true)
    setError('')
    setResult(null)

    try {
      const response = await fetch('/api/crop/recommend', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      })
      const data = await response.json()
      if (!response.ok) {
        throw new Error(data.detail || data.message || 'Recommendation failed')
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
      <h1 className="page-title">Crop Recommendation</h1>
      <p className="page-subtitle">Get AI-powered crop suggestions based on your soil and climate conditions.</p>

      <div className="card crop-card">
        <div className="form-grid">
          <div className="form-group">
            <label>Soil Type</label>
            <select name="soil_type" value={formData.soil_type} onChange={handleChange}>
              <option value="clay">Clay</option>
              <option value="sandy">Sandy</option>
              <option value="loamy">Loamy</option>
              <option value="black">Black</option>
            </select>
          </div>

          <div className="form-group">
            <label>Soil pH (0-14)</label>
            <input
              type="number"
              name="soil_ph"
              min="0"
              max="14"
              step="0.1"
              value={formData.soil_ph}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Temperature (°C)</label>
            <input
              type="number"
              name="temperature"
              value={formData.temperature}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Humidity (%)</label>
            <input
              type="number"
              name="humidity"
              min="0"
              max="100"
              value={formData.humidity}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Rainfall (mm/year)</label>
            <input
              type="number"
              name="rainfall"
              value={formData.rainfall}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Water Availability</label>
            <select name="water_availability" value={formData.water_availability} onChange={handleChange}>
              <option value="high">High</option>
              <option value="medium">Medium</option>
              <option value="low">Low</option>
            </select>
          </div>

          <div className="form-group">
            <label>Season</label>
            <select name="season" value={formData.season} onChange={handleChange}>
              <option value="summer">Summer</option>
              <option value="winter">Winter</option>
              <option value="monsoon">Monsoon</option>
              <option value="spring">Spring</option>
            </select>
          </div>

          <div className="form-group">
            <label>Location (Optional)</label>
            <input
              type="text"
              name="location"
              value={formData.location}
              onChange={handleChange}
              placeholder="Enter your location"
            />
          </div>

          <div className="form-group">
            <label>Previous Crop (Optional)</label>
            <input
              type="text"
              name="previous_crop"
              value={formData.previous_crop}
              onChange={handleChange}
              placeholder="Previous crop grown"
            />
          </div>
        </div>

        <button
          type="button"
          className="primary-btn"
          onClick={handleRecommend}
          disabled={loading}
        >
          {loading ? 'Analyzing...' : 'Get Recommendation'}
        </button>

        {error && <div className="alert error">{error}</div>}

        {result && (
          <div className="result-card">
            <h3>Recommended Crop</h3>
            <p className="crop-name">{result.recommended_crop}</p>
            <p className="confidence">Confidence: {(result.confidence * 100).toFixed(0)}%</p>
            <p className="reasoning">{result.reasoning}</p>

            {result.alternative_crops.length > 0 && (
              <div className="alternatives">
                <h4>Alternative Options:</h4>
                <ul>
                  {result.alternative_crops.map((crop, index) => (
                    <li key={index}>{crop}</li>
                  ))}
                </ul>
              </div>
            )}

            {result.tips.length > 0 && (
              <div className="tips">
                <h4>Farming Tips:</h4>
                <ul>
                  {result.tips.map((tip, index) => (
                    <li key={index}>{tip}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  )
}