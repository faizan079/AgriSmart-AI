import { useState } from 'react'
import './FarmerAssistant.css'

export default function FarmerAssistant() {
  const [question, setQuestion] = useState('')
  const [context, setContext] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState('')

  async function handleAsk() {
    if (!question.trim()) return

    setLoading(true)
    setError('')
    setResult(null)

    try {
      const response = await fetch('/api/assistant/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question, context }),
      })
      const data = await response.json()
      if (!response.ok) throw new Error(data.detail || data.message || 'Failed to get response')
      setResult(data.data)
    } catch (err) {
      setError(err.message || 'Could not reach backend')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <h1 className="page-title">Farmer Assistant</h1>
      <p className="page-subtitle">Get AI-powered farming guidance and answers to your questions.</p>

      <div className="card assistant-card">
        <div className="chat-interface">
          <div className="input-section">
            <div className="form-group">
              <label>Your Question</label>
              <textarea
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="Ask about diseases, irrigation, fertilizers, pests, soil health, weather, harvesting, crops, sustainability, or yield improvement..."
                rows={3}
              />
            </div>
            <div className="form-group">
              <label>Additional Context (Optional)</label>
              <textarea
                value={context}
                onChange={(e) => setContext(e.target.value)}
                placeholder="Provide any additional context about your farm or situation..."
                rows={2}
              />
            </div>
            <button
              className="primary-btn"
              onClick={handleAsk}
              disabled={loading || !question.trim()}
            >
              {loading ? 'Thinking...' : 'Ask Assistant'}
            </button>
          </div>

          {error && <div className="alert error">{error}</div>}

          {result && (
            <div className="result-card">
              <div className="answer-section">
                <h3>Assistant Response</h3>
                <p className="answer">{result.answer}</p>
                <div className="confidence">
                  Confidence: {(result.confidence * 100).toFixed(0)}%
                </div>
              </div>

              {result.related_topics.length > 0 && (
                <div className="related-topics">
                  <h4>Related Topics</h4>
                  <div className="topic-chips">
                    {result.related_topics.map((topic, index) => (
                      <span key={index} className="topic-chip">{topic}</span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}

          <div className="quick-questions">
            <h4>Quick Questions:</h4>
            <div className="question-chips">
              <button onClick={() => setQuestion('How do I manage crop diseases?')}>Disease Management</button>
              <button onClick={() => setQuestion('When should I irrigate my crops?')}>Irrigation Timing</button>
              <button onClick={() => setQuestion('What fertilizer should I use?')}>Fertilizer Guide</button>
              <button onClick={() => setQuestion('How can I improve soil health?')}>Soil Health</button>
              <button onClick={() => setQuestion('What should I do about pests?')}>Pest Control</button>
              <button onClick={() => setQuestion('How can I increase my crop yield?')}>Yield Improvement</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}