import { useState } from 'react'
import './AIAdvisor.css'

export default function AIAdvisor() {
  const [advisorData, setAdvisorData] = useState({
    crop_type: 'tomato',
    disease_status: 'healthy',
    soil_moisture: 60,
    weather_forecast: 'good',
    growth_stage: 'growing'
  })
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState('')

  function handleChange(event) {
    const { name, value } = event.target
    setAdvisorData(prev => ({
      ...prev,
      [name]: name === 'soil_moisture' ? parseFloat(value) : value
    }))
    setResult(null)
    setError('')
  }

  async function handleAnalyze() {
    setLoading(true)
    setError('')
    setResult(null)

    try {
      const response = await fetch('/api/advisor/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(advisorData),
      })
      const data = await response.json()
      if (!response.ok) throw new Error(data.detail || data.message || 'Analysis failed')
      setResult(data.data)
    } catch (err) {
      setError(err.message || 'Could not reach backend')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <h1 className="page-title">AI Advisor</h1>
      <p className="page-subtitle">Intelligent decision-making engine that analyzes your farm situation and provides actionable recommendations.</p>

      <div className="card advisor-card">
        <div className="form-grid">
          <div className="form-group">
            <label>Crop Type</label>
            <select name="crop_type" value={advisorData.crop_type} onChange={handleChange}>
              <option value="tomato">Tomato</option>
              <option value="wheat">Wheat</option>
              <option value="rice">Rice</option>
              <option value="maize">Maize</option>
              <option value="cotton">Cotton</option>
            </select>
          </div>

          <div className="form-group">
            <label>Disease Status</label>
            <select name="disease_status" value={advisorData.disease_status} onChange={handleChange}>
              <option value="healthy">Healthy</option>
              <option value="diseased">Diseased</option>
              <option value="suspected">Suspected Disease</option>
            </select>
          </div>

          <div className="form-group">
            <label>Soil Moisture (%)</label>
            <input
              type="number"
              name="soil_moisture"
              min="0"
              max="100"
              value={advisorData.soil_moisture}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Weather Forecast</label>
            <select name="weather_forecast" value={advisorData.weather_forecast} onChange={handleChange}>
              <option value="good">Good</option>
              <option value="moderate">Moderate</option>
              <option value="poor">Poor</option>
            </select>
          </div>

          <div className="form-group">
            <label>Growth Stage</label>
            <select name="growth_stage" value={advisorData.growth_stage} onChange={handleChange}>
              <option value="seedling">Seedling</option>
              <option value="growing">Growing</option>
              <option value="mature">Mature</option>
            </select>
          </div>
        </div>

        <button
          className="primary-btn"
          onClick={handleAnalyze}
          disabled={loading}
        >
          {loading ? 'Analyzing...' : 'Get AI Recommendation'}
        </button>

        {error && <div className="alert error">{error}</div>}

        {result && (
          <div className="result-card">
            <div className={`decision-banner ${result.priority}`}>
              <h3>{result.decision}</h3>
              <span className="priority-badge">{result.priority.toUpperCase()}</span>
            </div>

            <div className="reasoning-section">
              <h4>Reasoning</h4>
              <p>{result.reasoning}</p>
            </div>

            <div className="action-steps">
              <h4>Action Steps</h4>
              <ol>
                {result.action_steps.map((step, index) => (
                  <li key={index}>{step}</li>
                ))}
              </ol>
            </div>

            <div className="follow-up-info">
              <div className="info-item">
                <span className="label">Monitoring Required:</span>
                <span className={`value ${result.monitoring_required ? 'yes' : 'no'}`}>
                  {result.monitoring_required ? 'Yes' : 'No'}
                </span>
              </div>
              <div className="info-item">
                <span className="label">Follow-up Time:</span>
                <span className="value">{result.follow_up_time}</span>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}