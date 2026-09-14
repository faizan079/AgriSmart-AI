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
        Welcome to AgriSmart AI — your intelligent agriculture platform.
      </p>

      <div className="grid grid-3">
        <div className="card">
          <h3>🔬 Crop Health</h3>
          <p>Upload a leaf image to detect disease using AI.</p>
          <Link to="/disease" className="link-btn">Disease Detection →</Link>
        </div>
        <div className="card">
          <h3>🌱 Crop Recommendation</h3>
          <p>Get AI-powered crop suggestions based on your soil and climate.</p>
          <Link to="/crop" className="link-btn">Get Recommendation →</Link>
        </div>
        <div className="card">
          <h3>💧 Smart Irrigation</h3>
          <p>Coming soon — intelligent irrigation advice.</p>
        </div>
      </div>

      <div className="grid grid-3" style={{ marginTop: 16 }}>
        <div className="card">
          <h3>🌤️ Weather Intelligence</h3>
          <p>Coming soon — weather-based farming guidance.</p>
        </div>
        <div className="card">
          <h3>♻️ Sustainability</h3>
          <p>Coming soon — sustainability score and tips.</p>
        </div>
        <div className="card">
          <h3>🤖 AI Advisor</h3>
          <p>Coming soon — agentic decision-making for your farm.</p>
        </div>
      </div>

      <div className="card" style={{ marginTop: 16 }}>
        <h3>📊 Development Progress</h3>
        <div className="progress-list">
          <div className="progress-item done">
            <span className="progress-icon">✅</span>
            <span>Phase 1 — Foundation & Architecture</span>
          </div>
          <div className="progress-item done">
            <span className="progress-icon">✅</span>
            <span>Phase 2 — Core Disease ML Model (91% accuracy)</span>
          </div>
          <div className="progress-item done">
            <span className="progress-icon">✅</span>
            <span>Phase 3 — Disease Prediction API</span>
          </div>
          <div className="progress-item done">
            <span className="progress-icon">✅</span>
            <span>Phase 4 — Disease Frontend Polish</span>
          </div>
          <div className="progress-item done">
            <span className="progress-icon">✅</span>
            <span>Phase 5 — Crop Recommendation</span>
          </div>
          <div className="progress-item pending">
            <span className="progress-icon">⏳</span>
            <span>Phase 6 — Smart Irrigation + Weather</span>
          </div>
          <div className="progress-item pending">
            <span className="progress-icon">⏳</span>
            <span>Phase 7–10 — Sustainability, Innovation, Gemini, Agent</span>
          </div>
        </div>
      </div>
    </div>
  )
}
