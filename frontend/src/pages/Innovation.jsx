import { useState } from 'react'
import './Innovation.css'

export default function Innovation() {
  const [activeTab, setActiveTab] = useState('stress')

  // Crop Stress State
  const [stressData, setStressData] = useState({
    crop_type: 'tomato',
    disease_status: 'healthy',
    soil_moisture: 60,
    temperature: 28,
    humidity: 65,
    growth_stage: 'growing',
    water_stress_indicators: 'none'
  })
  const [stressResult, setStressResult] = useState(null)

  // Crop Rotation State
  const [rotationData, setRotationData] = useState({
    current_crop: 'tomato',
    previous_crop: '',
    soil_type: 'loamy',
    soil_ph: 6.5,
    season: 'summer',
    pest_history: 'none'
  })
  const [rotationResult, setRotationResult] = useState(null)

  // Water Yield State
  const [predictionData, setPredictionData] = useState({
    crop_type: 'tomato',
    area_hectares: 1.0,
    current_water_usage: 5000,
    soil_quality: 'moderate',
    weather_conditions: 'good',
    irrigation_method: 'drip'
  })
  const [predictionResult, setPredictionResult] = useState(null)

  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  async function handleStressAnalysis() {
    setLoading(true)
    setError('')
    setStressResult(null)

    try {
      const response = await fetch('/api/innovation/stress', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(stressData),
      })
      const data = await response.json()
      if (!response.ok) throw new Error(data.detail || data.message || 'Analysis failed')
      setStressResult(data.data)
    } catch (err) {
      setError(err.message || 'Could not reach backend')
    } finally {
      setLoading(false)
    }
  }

  async function handleRotationRecommendation() {
    setLoading(true)
    setError('')
    setRotationResult(null)

    try {
      const response = await fetch('/api/innovation/rotation', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(rotationData),
      })
      const data = await response.json()
      if (!response.ok) throw new Error(data.detail || data.message || 'Recommendation failed')
      setRotationResult(data.data)
    } catch (err) {
      setError(err.message || 'Could not reach backend')
    } finally {
      setLoading(false)
    }
  }

  async function handlePrediction() {
    setLoading(true)
    setError('')
    setPredictionResult(null)

    try {
      const response = await fetch('/api/innovation/prediction', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(predictionData),
      })
      const data = await response.json()
      if (!response.ok) throw new Error(data.detail || data.message || 'Prediction failed')
      setPredictionResult(data.data)
    } catch (err) {
      setError(err.message || 'Could not reach backend')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <h1 className="page-title">Innovation Features</h1>
      <p className="page-subtitle">Advanced AI-powered farming analytics and predictions.</p>

      <div className="tabs">
        <button className={`tab ${activeTab === 'stress' ? 'active' : ''}`} onClick={() => setActiveTab('stress')}>
          Crop Stress Warning
        </button>
        <button className={`tab ${activeTab === 'rotation' ? 'active' : ''}`} onClick={() => setActiveTab('rotation')}>
          Crop Rotation
        </button>
        <button className={`tab ${activeTab === 'prediction' ? 'active' : ''}`} onClick={() => setActiveTab('prediction')}>
          Water & Yield Prediction
        </button>
      </div>

      {activeTab === 'stress' && (
        <div className="card innovation-card">
          <div className="form-grid">
            <div className="form-group">
              <label>Crop Type</label>
              <select name="crop_type" value={stressData.crop_type} onChange={(e) => setStressData({...stressData, crop_type: e.target.value})}>
                <option value="tomato">Tomato</option>
                <option value="wheat">Wheat</option>
                <option value="rice">Rice</option>
                <option value="maize">Maize</option>
                <option value="cotton">Cotton</option>
              </select>
            </div>
            <div className="form-group">
              <label>Disease Status</label>
              <select name="disease_status" value={stressData.disease_status} onChange={(e) => setStressData({...stressData, disease_status: e.target.value})}>
                <option value="healthy">Healthy</option>
                <option value="diseased">Diseased</option>
              </select>
            </div>
            <div className="form-group">
              <label>Soil Moisture (%)</label>
              <input type="number" name="soil_moisture" min="0" max="100" value={stressData.soil_moisture} onChange={(e) => setStressData({...stressData, soil_moisture: parseFloat(e.target.value)})} />
            </div>
            <div className="form-group">
              <label>Temperature (°C)</label>
              <input type="number" name="temperature" value={stressData.temperature} onChange={(e) => setStressData({...stressData, temperature: parseFloat(e.target.value)})} />
            </div>
            <div className="form-group">
              <label>Humidity (%)</label>
              <input type="number" name="humidity" min="0" max="100" value={stressData.humidity} onChange={(e) => setStressData({...stressData, humidity: parseFloat(e.target.value)})} />
            </div>
            <div className="form-group">
              <label>Growth Stage</label>
              <select name="growth_stage" value={stressData.growth_stage} onChange={(e) => setStressData({...stressData, growth_stage: e.target.value})}>
                <option value="seedling">Seedling</option>
                <option value="growing">Growing</option>
                <option value="mature">Mature</option>
              </select>
            </div>
          </div>
          <button className="primary-btn" onClick={handleStressAnalysis} disabled={loading}>
            {loading ? 'Analyzing...' : 'Analyze Crop Stress'}
          </button>
          {error && <div className="alert error">{error}</div>}
          {stressResult && (
            <div className="result-card">
              <h3>Crop Stress Analysis</h3>
              <div className={`stress-level ${stressResult.stress_level}`}>
                Stress Level: {stressResult.stress_level.toUpperCase()}
              </div>
              <p className="risk">{stressResult.risk_assessment}</p>
              {stressResult.stress_factors.length > 0 && (
                <div className="factors">
                  <h4>Stress Factors:</h4>
                  <ul>
                    {stressResult.stress_factors.map((factor, i) => <li key={i}>{factor}</li>)}
                  </ul>
                </div>
              )}
              <div className="recommendations">
                <h4>Recommendations:</h4>
                <ul>
                  {stressResult.recommendations.map((rec, i) => <li key={i}>{rec}</li>)}
                </ul>
              </div>
            </div>
          )}
        </div>
      )}

      {activeTab === 'rotation' && (
        <div className="card innovation-card">
          <div className="form-grid">
            <div className="form-group">
              <label>Current Crop</label>
              <select name="current_crop" value={rotationData.current_crop} onChange={(e) => setRotationData({...rotationData, current_crop: e.target.value})}>
                <option value="tomato">Tomato</option>
                <option value="wheat">Wheat</option>
                <option value="rice">Rice</option>
                <option value="maize">Maize</option>
                <option value="cotton">Cotton</option>
              </select>
            </div>
            <div className="form-group">
              <label>Previous Crop</label>
              <input type="text" name="previous_crop" value={rotationData.previous_crop} onChange={(e) => setRotationData({...rotationData, previous_crop: e.target.value})} placeholder="Previous crop (optional)" />
            </div>
            <div className="form-group">
              <label>Soil Type</label>
              <select name="soil_type" value={rotationData.soil_type} onChange={(e) => setRotationData({...rotationData, soil_type: e.target.value})}>
                <option value="loamy">Loamy</option>
                <option value="clay">Clay</option>
                <option value="sandy">Sandy</option>
                <option value="black">Black</option>
              </select>
            </div>
            <div className="form-group">
              <label>Soil pH</label>
              <input type="number" name="soil_ph" min="0" max="14" step="0.1" value={rotationData.soil_ph} onChange={(e) => setRotationData({...rotationData, soil_ph: parseFloat(e.target.value)})} />
            </div>
            <div className="form-group">
              <label>Season</label>
              <select name="season" value={rotationData.season} onChange={(e) => setRotationData({...rotationData, season: e.target.value})}>
                <option value="summer">Summer</option>
                <option value="winter">Winter</option>
                <option value="monsoon">Monsoon</option>
                <option value="spring">Spring</option>
              </select>
            </div>
          </div>
          <button className="primary-btn" onClick={handleRotationRecommendation} disabled={loading}>
            {loading ? 'Analyzing...' : 'Get Rotation Recommendation'}
          </button>
          {error && <div className="alert error">{error}</div>}
          {rotationResult && (
            <div className="result-card">
              <h3>Crop Rotation Recommendation</h3>
              <p className="recommended-crop">Recommended Next Crop: {rotationResult.recommended_next_crop}</p>
              <p className="soil-impact">{rotationResult.soil_health_impact}</p>
              <p className="timing">{rotationResult.timing_recommendation}</p>
              <div className="benefits">
                <h4>Rotation Benefits:</h4>
                <ul>
                  {rotationResult.rotation_benefits.map((benefit, i) => <li key={i}>{benefit}</li>)}
                </ul>
              </div>
              {rotationResult.alternatives.length > 0 && (
                <div className="alternatives">
                  <h4>Alternative Options:</h4>
                  <ul>
                    {rotationResult.alternatives.map((alt, i) => <li key={i}>{alt}</li>)}
                  </ul>
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {activeTab === 'prediction' && (
        <div className="card innovation-card">
          <div className="form-grid">
            <div className="form-group">
              <label>Crop Type</label>
              <select name="crop_type" value={predictionData.crop_type} onChange={(e) => setPredictionData({...predictionData, crop_type: e.target.value})}>
                <option value="tomato">Tomato</option>
                <option value="wheat">Wheat</option>
                <option value="rice">Rice</option>
                <option value="maize">Maize</option>
                <option value="cotton">Cotton</option>
              </select>
            </div>
            <div className="form-group">
              <label>Area (Hectares)</label>
              <input type="number" name="area_hectares" min="0" step="0.1" value={predictionData.area_hectares} onChange={(e) => setPredictionData({...predictionData, area_hectares: parseFloat(e.target.value)})} />
            </div>
            <div className="form-group">
              <label>Current Water Usage (Liters)</label>
              <input type="number" name="current_water_usage" min="0" value={predictionData.current_water_usage} onChange={(e) => setPredictionData({...predictionData, current_water_usage: parseFloat(e.target.value)})} />
            </div>
            <div className="form-group">
              <label>Soil Quality</label>
              <select name="soil_quality" value={predictionData.soil_quality} onChange={(e) => setPredictionData({...predictionData, soil_quality: e.target.value})}>
                <option value="good">Good</option>
                <option value="moderate">Moderate</option>
                <option value="poor">Poor</option>
              </select>
            </div>
            <div className="form-group">
              <label>Weather Conditions</label>
              <select name="weather_conditions" value={predictionData.weather_conditions} onChange={(e) => setPredictionData({...predictionData, weather_conditions: e.target.value})}>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="moderate">Moderate</option>
                <option value="poor">Poor</option>
              </select>
            </div>
            <div className="form-group">
              <label>Irrigation Method</label>
              <select name="irrigation_method" value={predictionData.irrigation_method} onChange={(e) => setPredictionData({...predictionData, irrigation_method: e.target.value})}>
                <option value="drip">Drip</option>
                <option value="sprinkler">Sprinkler</option>
                <option value="flood">Flood</option>
              </select>
            </div>
          </div>
          <button className="primary-btn" onClick={handlePrediction} disabled={loading}>
            {loading ? 'Predicting...' : 'Predict Water & Yield'}
          </button>
          {error && <div className="alert error">{error}</div>}
          {predictionResult && (
            <div className="result-card">
              <h3>Water & Yield Prediction</h3>
              <div className="prediction-grid">
                <div className="prediction-item">
                  <span className="label">Water Required:</span>
                  <span className="value">{predictionResult.estimated_water_requirement.toLocaleString()} L</span>
                </div>
                <div className="prediction-item">
                  <span className="label">Estimated Yield:</span>
                  <span className="value">{predictionResult.estimated_yield.toLocaleString()} kg</span>
                </div>
                <div className="prediction-item">
                  <span className="label">Yield Range:</span>
                  <span className="value">{predictionResult.yield_range}</span>
                </div>
                <div className="prediction-item">
                  <span className="label">Water Efficiency:</span>
                  <span className="value">{predictionResult.water_efficiency_score}%</span>
                </div>
              </div>
              <div className="optimization-tips">
                <h4>Optimization Tips:</h4>
                <ul>
                  {predictionResult.optimization_tips.map((tip, i) => <li key={i}>{tip}</li>)}
                </ul>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  )
}