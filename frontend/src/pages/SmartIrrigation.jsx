import { useState } from 'react'
import './SmartIrrigation.css'

export default function SmartIrrigation() {
  const [irrigationData, setIrrigationData] = useState({
    crop_type: 'tomato',
    soil_moisture: 45,
    growth_stage: 'growing',
    temperature: 28,
    humidity: 65,
    rainfall_forecast: 0
  })
  const [weatherData, setWeatherData] = useState({
    location: '',
    current_temp: 28,
    current_humidity: 65,
    rainfall_expected: false,
    wind_speed: 5
  })
  const [loading, setLoading] = useState(false)
  const [irrigationResult, setIrrigationResult] = useState(null)
  const [weatherResult, setWeatherResult] = useState(null)
  const [error, setError] = useState('')
  const [activeTab, setActiveTab] = useState('irrigation')

  function handleIrrigationChange(event) {
    const { name, value, type, checked } = event.target
    setIrrigationData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : (type === 'number' ? parseFloat(value) : value)
    }))
    setIrrigationResult(null)
    setError('')
  }

  function handleWeatherChange(event) {
    const { name, value, type, checked } = event.target
    setWeatherData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : (type === 'number' ? parseFloat(value) : value)
    }))
    setWeatherResult(null)
    setError('')
  }

  async function handleIrrigationAnalysis() {
    setLoading(true)
    setError('')
    setIrrigationResult(null)

    try {
      const response = await fetch('/api/irrigation/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(irrigationData),
      })
      const data = await response.json()
      if (!response.ok) {
        throw new Error(data.detail || data.message || 'Analysis failed')
      }
      setIrrigationResult(data.data)
    } catch (err) {
      setError(err.message || 'Could not reach backend. Is the server running?')
    } finally {
      setLoading(false)
    }
  }

  async function handleWeatherAnalysis() {
    setLoading(true)
    setError('')
    setWeatherResult(null)

    try {
      const response = await fetch('/api/irrigation/weather', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(weatherData),
      })
      const data = await response.json()
      if (!response.ok) {
        throw new Error(data.detail || data.message || 'Analysis failed')
      }
      setWeatherResult(data.data)
    } catch (err) {
      setError(err.message || 'Could not reach backend. Is the server running?')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <h1 className="page-title">Smart Irrigation & Weather</h1>
      <p className="page-subtitle">AI-powered irrigation analysis and weather-based farming recommendations.</p>

      <div className="tabs">
        <button
          className={`tab ${activeTab === 'irrigation' ? 'active' : ''}`}
          onClick={() => setActiveTab('irrigation')}
        >
          Irrigation Analysis
        </button>
        <button
          className={`tab ${activeTab === 'weather' ? 'active' : ''}`}
          onClick={() => setActiveTab('weather')}
        >
          Weather Intelligence
        </button>
      </div>

      {activeTab === 'irrigation' && (
        <div className="card irrigation-card">
          <div className="form-grid">
            <div className="form-group">
              <label>Crop Type</label>
              <select name="crop_type" value={irrigationData.crop_type} onChange={handleIrrigationChange}>
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
              <label>Soil Moisture (%)</label>
              <input
                type="number"
                name="soil_moisture"
                min="0"
                max="100"
                value={irrigationData.soil_moisture}
                onChange={handleIrrigationChange}
              />
            </div>

            <div className="form-group">
              <label>Growth Stage</label>
              <select name="growth_stage" value={irrigationData.growth_stage} onChange={handleIrrigationChange}>
                <option value="seedling">Seedling</option>
                <option value="growing">Growing</option>
                <option value="mature">Mature</option>
              </select>
            </div>

            <div className="form-group">
              <label>Temperature (°C)</label>
              <input
                type="number"
                name="temperature"
                value={irrigationData.temperature}
                onChange={handleIrrigationChange}
              />
            </div>

            <div className="form-group">
              <label>Humidity (%)</label>
              <input
                type="number"
                name="humidity"
                min="0"
                max="100"
                value={irrigationData.humidity}
                onChange={handleIrrigationChange}
              />
            </div>

            <div className="form-group">
              <label>Rainfall Forecast (mm)</label>
              <input
                type="number"
                name="rainfall_forecast"
                min="0"
                value={irrigationData.rainfall_forecast}
                onChange={handleIrrigationChange}
              />
            </div>
          </div>

          <button
            type="button"
            className="primary-btn"
            onClick={handleIrrigationAnalysis}
            disabled={loading}
          >
            {loading ? 'Analyzing...' : 'Analyze Irrigation Needs'}
          </button>

          {error && <div className="alert error">{error}</div>}

          {irrigationResult && (
            <div className="result-card">
              <h3>Irrigation Analysis Result</h3>
              <div className="status-indicator">
                <span className={`status ${irrigationResult.irrigation_needed ? 'needed' : 'not-needed'}`}>
                  {irrigationResult.irrigation_needed ? 'IRRIGATION NEEDED' : 'NO IRRIGATION NEEDED'}
                </span>
              </div>
              <p className="recommendation">{irrigationResult.recommendation}</p>
              <div className="details">
                <p><strong>Water Amount:</strong> {irrigationResult.water_amount} mm</p>
                <p><strong>Urgency:</strong> <span className={`urgency ${irrigationResult.urgency}`}>{irrigationResult.urgency.toUpperCase()}</span></p>
                <p><strong>Next Check:</strong> {irrigationResult.next_check_time}</p>
              </div>
            </div>
          )}
        </div>
      )}

      {activeTab === 'weather' && (
        <div className="card weather-card">
          <div className="form-grid">
            <div className="form-group">
              <label>Location</label>
              <input
                type="text"
                name="location"
                value={weatherData.location}
                onChange={handleWeatherChange}
                placeholder="Enter your location"
              />
            </div>

            <div className="form-group">
              <label>Current Temperature (°C)</label>
              <input
                type="number"
                name="current_temp"
                value={weatherData.current_temp}
                onChange={handleWeatherChange}
              />
            </div>

            <div className="form-group">
              <label>Current Humidity (%)</label>
              <input
                type="number"
                name="current_humidity"
                min="0"
                max="100"
                value={weatherData.current_humidity}
                onChange={handleWeatherChange}
              />
            </div>

            <div className="form-group">
              <label>Rainfall Expected</label>
              <select name="rainfall_expected" value={weatherData.rainfall_expected} onChange={handleWeatherChange}>
                <option value={false}>No</option>
                <option value={true}>Yes</option>
              </select>
            </div>

            <div className="form-group">
              <label>Wind Speed (km/h)</label>
              <input
                type="number"
                name="wind_speed"
                min="0"
                value={weatherData.wind_speed}
                onChange={handleWeatherChange}
              />
            </div>
          </div>

          <button
            type="button"
            className="primary-btn"
            onClick={handleWeatherAnalysis}
            disabled={loading}
          >
            {loading ? 'Analyzing...' : 'Analyze Weather Conditions'}
          </button>

          {error && <div className="alert error">{error}</div>}

          {weatherResult && (
            <div className="result-card">
              <h3>Weather Analysis Result</h3>
              <p className="conditions"><strong>Current Conditions:</strong> {weatherResult.current_conditions}</p>
              <p className={`risk ${weatherResult.action_required ? 'high' : 'low'}`}>
                <strong>Risk Assessment:</strong> {weatherResult.risk_assessment}
              </p>

              {weatherResult.action_required && weatherResult.priority_actions.length > 0 && (
                <div className="priority-actions">
                  <h4>Priority Actions:</h4>
                  <ul>
                    {weatherResult.priority_actions.map((action, index) => (
                      <li key={index} className="urgent">{action}</li>
                    ))}
                  </ul>
                </div>
              )}

              <div className="recommendations">
                <h4>Recommendations:</h4>
                <ul>
                  {weatherResult.recommendations.map((rec, index) => (
                    <li key={index}>{rec}</li>
                  ))}
                </ul>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  )
}