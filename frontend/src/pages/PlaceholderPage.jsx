export default function PlaceholderPage({ title, phase }) {
  return (
    <div className="card">
      <h1 className="page-title">{title}</h1>
      <p className="page-subtitle">
        This module will be implemented in {phase}. Part 1 only sets up the navigation shell.
      </p>
    </div>
  )
}
