import { Link } from 'react-router-dom'
import './Dashboard.css'

function getGreeting() {
  const hour = new Date().getHours()
  if (hour < 12) return 'Good morning'
  if (hour < 17) return 'Good afternoon'
  return 'Good evening'
}

export default function Dashboard() {
  return (
    <div className="dashboard">
      {/* Hero Section */}
      <div className="hero-section">
        <h1 className="page-title">🌾 {getGreeting()}, Farmer</h1>
        <p className="page-subtitle">
          Intelligent agriculture at your fingertips. AI-powered disease detection, crop recommendations, and real-time farm guidance.
        </p>
      </div>

      {/* Key Stats */}
      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-icon">🤖</div>
          <div className="stat-content">
            <div className="stat-number">8</div>
            <div className="stat-label">AI Modules</div>
          </div>
        </div>
        <div className="stat-card">
          <div className="stat-icon">📊</div>
          <div className="stat-content">
            <div className="stat-number">91%</div>
            <div className="stat-label">Disease Accuracy</div>
          </div>
        </div>
        <div className="stat-card">
          <div className="stat-icon">✅</div>
          <div className="stat-content">
            <div className="stat-number">10</div>
            <div className="stat-label">Phases Complete</div>
          </div>
        </div>
        <div className="stat-card">
          <div className="stat-icon">⚡</div>
          <div className="stat-content">
            <div className="stat-number">Live</div>
            <div className="stat-label">API Ready</div>
          </div>
        </div>
      </div>

      {/* Quick Access - Essential Modules */}
      <div className="section">
        <h2 className="section-title">⭐ Essential Tools</h2>
        
        <div className="module-grid module-grid-3">
          {/* Disease Detection */}
          <Link to="/disease" className="module-card primary">
            <div className="card-icon">🔬</div>
            <h3>Disease Detection</h3>
            <p>AI-powered leaf analysis with 91% accuracy. Instant diagnosis & treatment recommendations.</p>
            <div className="card-footer">
              <span className="badge live">Live</span>
              <span className="cta">Start Now →</span>
            </div>
          </Link>

          {/* Crop Recommendation */}
          <Link to="/crop" className="module-card primary">
            <div className="card-icon">🌱</div>
            <h3>Crop Recommendation</h3>
            <p>Get AI-powered crop suggestions based on your soil, climate, and season.</p>
            <div className="card-footer">
              <span className="badge live">Live</span>
              <span className="cta">Explore →</span>
            </div>
          </Link>

          {/* Smart Irrigation */}
          <Link to="/irrigation" className="module-card primary">
            <div className="card-icon">💧</div>
            <h3>Smart Irrigation</h3>
            <p>Real-time water analysis + weather forecasting. Optimize every drop.</p>
            <div className="card-footer">
              <span className="badge live">Live</span>
              <span className="cta">Analyze →</span>
            </div>
          </Link>
        </div>
      </div>

      {/* Advanced Features */}
      <div className="section">
        <h2 className="section-title">🚀 Advanced Features</h2>
        
        <div className="module-grid module-grid-2">
          {/* Sustainability */}
          <Link to="/sustainability" className="module-card secondary">
            <div className="card-icon">♻️</div>
            <h3>Sustainability Score</h3>
            <p>Measure environmental impact. Track water efficiency, resources, and soil health.</p>
            <div className="card-footer">
              <span className="badge live">Live</span>
            </div>
          </Link>

          {/* Innovation Suite */}
          <Link to="/innovation" className="module-card secondary">
            <div className="card-icon">🚀</div>
            <h3>Innovation Suite</h3>
            <p>Crop stress warnings, rotation planning, water & yield prediction.</p>
            <div className="card-footer">
              <span className="badge live">Live</span>
            </div>
          </Link>
        </div>
      </div>

      {/* AI Intelligence */}
      <div className="section">
        <h2 className="section-title">🤖 AI Intelligence</h2>
        
        <div className="module-grid module-grid-2">
          {/* Farmer Assistant */}
          <Link to="/assistant" className="module-card ai">
            <div className="card-icon">💬</div>
            <h3>Farmer Assistant</h3>
            <p>24/7 AI chat for farming guidance. Ask about diseases, irrigation, fertilizers, pests, and more.</p>
            <div className="card-footer">
              <span className="badge live">Live</span>
            </div>
          </Link>

          {/* AI Advisor */}
          <Link to="/advisor" className="module-card ai">
            <div className="card-icon">🎯</div>
            <h3>AI Advisor</h3>
            <p>Intelligent decision engine. Analyzes farm situation and provides prioritized actions.</p>
            <div className="card-footer">
              <span className="badge live">Live</span>
            </div>
          </Link>
        </div>
      </div>

      {/* Status Banner */}
      <div className="status-banner">
        <div className="banner-content">
          <h3>✨ Platform Status</h3>
          <p>All 8 modules operational • 10 phases complete • Backend APIs fully integrated • Ready for deployment</p>
        </div>
        <div className="banner-icon">🚀</div>
      </div>
    </div>
  )
}
