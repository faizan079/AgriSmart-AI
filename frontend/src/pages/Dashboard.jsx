import { Link } from 'react-router-dom'

function getGreeting() {
  const hour = new Date().getHours()
  if (hour < 12) return 'Good morning'
  if (hour < 17) return 'Good afternoon'
  return 'Good evening'
}

export default function Dashboard() {
  return (
    <div>
      <h1 className="page-title">🌾 {getGreeting()}, Farmer</h1>
      <p className="page-subtitle">
        Welcome to AgriSmart AI — your complete intelligent agriculture platform.
      </p>

      {/* Stats Overview */}
      <div className="grid grid-4" style={{ marginBottom: 24 }}>
        <div className="card stats-card">
          <div className="stat-number">8</div>
          <div className="stat-label">AI Modules</div>
        </div>
        <div className="card stats-card">
          <div className="stat-number">10</div>
          <div className="stat-label">Phases Complete</div>
        </div>
        <div className="card stats-card">
          <div className="stat-number">91%</div>
          <div className="stat-label">Disease Accuracy</div>
        </div>
        <div className="card stats-card">
          <div className="stat-number">∞</div>
          <div className="stat-label">Always Learning</div>
        </div>
      </div>

      {/* Phase 1-4: Disease Detection */}
      <div style={{ marginBottom: 24 }}>
        <h2 style={{ fontSize: '1.3rem', marginBottom: 12, color: '#1b5e20' }}>🔬 Phase 1-4: Disease Detection</h2>
        <div className="grid grid-1">
          <div className="card">
            <h3>🔬 Crop Health Analysis</h3>
            <p>Upload a leaf image to detect diseases using advanced AI with 91% accuracy. Get instant diagnosis and treatment recommendations.</p>
            <Link to="/disease" className="link-btn">🚀 Start Disease Detection →</Link>
          </div>
        </div>
      </div>

      {/* Phase 5: Crop Recommendation */}
      <div style={{ marginBottom: 24 }}>
        <h2 style={{ fontSize: '1.3rem', marginBottom: 12, color: '#1b5e20' }}>🌱 Phase 5: Smart Farming</h2>
        <div className="grid grid-1">
          <div className="card">
            <h3>🌱 Crop Recommendation</h3>
            <p>Get AI-powered crop suggestions based on your soil pH, temperature, humidity, rainfall, and water availability. Maximize your yield with data-driven choices.</p>
            <Link to="/crop" className="link-btn">💡 Get Smart Recommendation →</Link>
          </div>
        </div>
      </div>

      {/* Phase 6-10: Advanced Features */}
      <div style={{ marginBottom: 24 }}>
        <h2 style={{ fontSize: '1.3rem', marginBottom: 12, color: '#1b5e20' }}>⚡ Phase 6-10: Advanced Intelligence</h2>
        
        <div className="grid grid-3">
          <div className="card">
            <h3>💧 Smart Irrigation</h3>
            <p>Real-time irrigation analysis + weather forecasting. Optimize water usage and prevent over/under-watering.</p>
            <Link to="/irrigation" className="link-btn">Analyze Now →</Link>
          </div>

          <div className="card">
            <h3>♻️ Sustainability Score</h3>
            <p>Measure environmental impact of your farming. Track water efficiency, resource usage, and soil health.</p>
            <Link to="/sustainability" className="link-btn">Calculate Score →</Link>
          </div>

          <div className="card">
            <h3>🚀 Innovation Suite</h3>
            <p>Crop stress warnings, rotation planning, water & yield prediction. Advanced analytics for modern farming.</p>
            <Link to="/innovation" className="link-btn">Explore Features →</Link>
          </div>
        </div>
      </div>

      {/* Phase 9-10: AI Agents */}
      <div style={{ marginBottom: 24 }}>
        <h2 style={{ fontSize: '1.3rem', marginBottom: 12, color: '#1b5e20' }}>🤖 Phase 9-10: AI Advisors</h2>
        
        <div className="grid grid-2">
          <div className="card">
            <h3>💬 Farmer Assistant</h3>
            <p>Chat with AI about diseases, irrigation, fertilizers, pests, soil health, weather, harvesting, crops, sustainability, and yield improvement. Instant answers to farming questions.</p>
            <Link to="/assistant" className="link-btn">Ask Assistant →</Link>
          </div>

          <div className="card">
            <h3>🤖 AI Advisor</h3>
            <p>Intelligent decision-making engine. Analyzes multiple farm factors (disease, moisture, weather, growth stage) and provides prioritized actionable recommendations with urgency levels.</p>
            <Link to="/advisor" className="link-btn">Get AI Advice →</Link>
          </div>
        </div>
      </div>

      {/* Development Progress */}
      <div className="card" style={{ marginTop: 24 }}>
        <h3>📊 Development Progress (All 10 Phases Complete)</h3>
        <div className="progress-list">
          <div className="progress-item done">
            <span className="progress-icon">✅</span>
            <span><strong>Phase 1</strong> — Foundation & Architecture</span>
          </div>
          <div className="progress-item done">
            <span className="progress-icon">✅</span>
            <span><strong>Phase 2</strong> — Core Disease ML Model (91% accuracy)</span>
          </div>
          <div className="progress-item done">
            <span className="progress-icon">✅</span>
            <span><strong>Phase 3</strong> — Disease Prediction API</span>
          </div>
          <div className="progress-item done">
            <span className="progress-icon">✅</span>
            <span><strong>Phase 4</strong> — Disease Frontend Polish</span>
          </div>
          <div className="progress-item done">
            <span className="progress-icon">✅</span>
            <span><strong>Phase 5</strong> — Crop Recommendation (Rule-based)</span>
          </div>
          <div className="progress-item done">
            <span className="progress-icon">✅</span>
            <span><strong>Phase 6</strong> — Smart Irrigation + Weather Intelligence</span>
          </div>
          <div className="progress-item done">
            <span className="progress-icon">✅</span>
            <span><strong>Phase 7</strong> — Sustainability Score & Metrics</span>
          </div>
          <div className="progress-item done">
            <span className="progress-icon">✅</span>
            <span><strong>Phase 8</strong> — Innovation Features (Stress, Rotation, Prediction)</span>
          </div>
          <div className="progress-item done">
            <span className="progress-icon">✅</span>
            <span><strong>Phase 9</strong> — Farmer Assistant (Rule-based + Ready for Gemini)</span>
          </div>
          <div className="progress-item done">
            <span className="progress-icon">✅</span>
            <span><strong>Phase 10</strong> — AI Advisor (Agentic Decision Engine)</span>
          </div>
        </div>
        <div style={{ marginTop: 20, padding: 16, backgroundColor: '#e8f5e9', borderRadius: 8, borderLeft: '4px solid #2e7d32' }}>
          <p style={{ margin: 0, color: '#1b5e20', fontSize: '0.95rem' }}>
            <strong>✨ Status:</strong> All 8 modules + 10 phases complete. Backend APIs fully operational. Frontend connected and tested. Ready for SIH 2026 evaluation.
          </p>
        </div>
      </div>

      {/* Key Features */}
      <div className="card" style={{ marginTop: 16 }}>
        <h3>🎯 Key Features at a Glance</h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 12 }}>
          <div style={{ padding: 12, backgroundColor: '#f5f5f5', borderRadius: 6 }}>
            <strong>Disease Detection</strong><br/>
            <small>91% accuracy ML model</small>
          </div>
          <div style={{ padding: 12, backgroundColor: '#f5f5f5', borderRadius: 6 }}>
            <strong>Crop Recommendation</strong><br/>
            <small>13+ crop database</small>
          </div>
          <div style={{ padding: 12, backgroundColor: '#f5f5f5', borderRadius: 6 }}>
            <strong>Smart Irrigation</strong><br/>
            <small>Real-time analysis</small>
          </div>
          <div style={{ padding: 12, backgroundColor: '#f5f5f5', borderRadius: 6 }}>
            <strong>Weather Intelligence</strong><br/>
            <small>Risk assessment</small>
          </div>
          <div style={{ padding: 12, backgroundColor: '#f5f5f5', borderRadius: 6 }}>
            <strong>Sustainability Scoring</strong><br/>
            <small>Environmental impact</small>
          </div>
          <div style={{ padding: 12, backgroundColor: '#f5f5f5', borderRadius: 6 }}>
            <strong>Crop Stress Analysis</strong><br/>
            <small>Early warning system</small>
          </div>
          <div style={{ padding: 12, backgroundColor: '#f5f5f5', borderRadius: 6 }}>
            <strong>Crop Rotation</strong><br/>
            <small>Soil health planning</small>
          </div>
          <div style={{ padding: 12, backgroundColor: '#f5f5f5', borderRadius: 6 }}>
            <strong>Yield & Water Prediction</strong><br/>
            <small>Production forecasting</small>
          </div>
          <div style={{ padding: 12, backgroundColor: '#f5f5f5', borderRadius: 6 }}>
            <strong>Farmer Assistant</strong><br/>
            <small>24/7 AI guidance</small>
          </div>
          <div style={{ padding: 12, backgroundColor: '#f5f5f5', borderRadius: 6 }}>
            <strong>AI Advisor</strong><br/>
            <small>Decision engine</small>
          </div>
          <div style={{ padding: 12, backgroundColor: '#f5f5f5', borderRadius: 6 }}>
            <strong>Gemini Integration</strong><br/>
            <small>Ready (Phase 9)</small>
          </div>
          <div style={{ padding: 12, backgroundColor: '#f5f5f5', borderRadius: 6 }}>
            <strong>API Architecture</strong><br/>
            <small>FastAPI modular</small>
          </div>
        </div>
      </div>
    </div>
  )
}
