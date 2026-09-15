import { Link } from 'react-router-dom'
import './Dashboard.css'

export default function Dashboard() {
  return (
    <div className="dashboard">
      {/* Hero Section */}
      <div className="hero-section">
        <h1 className="page-title">🌱 Welcome to AgriSmart AI</h1>
        <p className="page-subtitle">
          Smart agriculture insights, recommendations, and crop health monitoring.
        </p>
        <p className="hero-description">
          Detect crop diseases, optimize irrigation, and get practical guidance for better farming.
        </p>
      </div>

      {/* Key Stats - Only 2 cards */}
      <div className="stats-grid stats-grid-2">
        <div className="stat-card">
          <div className="stat-icon">🤖</div>
          <div className="stat-content">
            <div className="stat-number">8</div>
            <div className="stat-label">AI-Powered Features</div>
          </div>
        </div>
        <div className="stat-card">
          <div className="stat-icon">⚙️</div>
          <div className="stat-content">
            <div className="stat-number">10</div>
            <div className="stat-label">Integrated Capabilities</div>
          </div>
        </div>
      </div>

      {/* Core Agriculture Tools */}
      <div className="section">
        <h2 className="section-title">🌾 Core Agriculture Tools</h2>
        
        <div className="module-grid module-grid-3">
          {/* Disease Detection */}
          <Link to="/disease" className="module-card primary">
            <div className="card-icon">🔬</div>
            <h3>Disease Detection</h3>
            <p>Analyze crop leaf images to identify possible diseases and receive practical precautionary guidance.</p>
            <div className="card-footer">
              <span className="cta">Start Now →</span>
            </div>
          </Link>

          {/* Crop Recommendation */}
          <Link to="/crop" className="module-card primary">
            <div className="card-icon">🌱</div>
            <h3>Crop Recommendation</h3>
            <p>Get suitable crop recommendations based on soil, climate, season, and farm conditions.</p>
            <div className="card-footer">
              <span className="cta">Explore →</span>
            </div>
          </Link>

          {/* Smart Irrigation */}
          <Link to="/irrigation" className="module-card primary">
            <div className="card-icon">💧</div>
            <h3>Smart Irrigation</h3>
            <p>Make smarter irrigation decisions using farm conditions and weather insights.</p>
            <div className="card-footer">
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
          </Link>

          {/* Innovation Suite */}
          <Link to="/innovation" className="module-card secondary">
            <div className="card-icon">🚀</div>
            <h3>Innovation Suite</h3>
            <p>Crop stress warnings, rotation planning, water & yield prediction.</p>
          </Link>
        </div>
      </div>

      {/* AI-Powered Assistance */}
      <div className="section">
        <h2 className="section-title">🤖 AI-Powered Assistance</h2>
        
        <div className="module-grid module-grid-2">
          {/* Farmer Assistant */}
          <Link to="/assistant" className="module-card ai">
            <div className="card-icon">💬</div>
            <h3>Farmer Assistant</h3>
            <p>Get clear, practical answers about crop diseases, irrigation, fertilizers, pests, and everyday farming decisions.</p>
          </Link>

          {/* AI Advisor */}
          <Link to="/advisor" className="module-card ai">
            <div className="card-icon">🎯</div>
            <h3>AI Advisor</h3>
            <p>Analyzes farm conditions and generates prioritized, actionable recommendations.</p>
          </Link>
        </div>
      </div>
    </div>
  )
}
