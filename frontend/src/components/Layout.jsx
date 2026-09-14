import { useState } from 'react'
import { NavLink, Outlet } from 'react-router-dom'
import './Layout.css'

const navItems = [
  { to: '/', label: 'Dashboard', end: true },
  { to: '/disease', label: 'Disease Detection' },
  { to: '/crop', label: 'Crop Recommendation' },
  { to: '/irrigation', label: 'Smart Irrigation & Weather' },
  { to: '/sustainability', label: 'Sustainability Score' },
  { to: '/innovation', label: 'Innovation Features' },
  { to: '/assistant', label: 'Farmer Assistant' },
  { to: '/advisor', label: 'AI Advisor' },
]

export default function Layout() {
  const [menuOpen, setMenuOpen] = useState(false)

  return (
    <div className="layout">
      <button
        type="button"
        className="menu-toggle"
        onClick={() => setMenuOpen((open) => !open)}
        aria-label="Toggle navigation"
      >
        ☰
      </button>

      <aside className={`sidebar ${menuOpen ? 'open' : ''}`}>
        <div className="brand">
          <span className="brand-icon">🌱</span>
          <div>
            <strong>AgriSmart AI</strong>
            <small>Intelligent Agriculture</small>
          </div>
        </div>
        <nav>
          {navItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.end}
              onClick={() => setMenuOpen(false)}
            >
              {item.label}
            </NavLink>
          ))}
        </nav>
      </aside>

      <main className="content">
        <Outlet />
      </main>
    </div>
  )
}
