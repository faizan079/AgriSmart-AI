import { useState, useRef, useCallback } from 'react'
import './DiseaseDetection.css'

export default function DiseaseDetection() {
  const [file, setFile] = useState(null)
  const [preview, setPreview] = useState(null)
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState('')
  const [dragOver, setDragOver] = useState(false)
  const fileInputRef = useRef(null)

  const handleFile = useCallback((selectedFile) => {
    if (!selectedFile) return
    if (!selectedFile.type.startsWith('image/')) {
      setError('Please upload a valid image file (JPEG or PNG).')
      return
    }
    setFile(selectedFile)
    setPreview(URL.createObjectURL(selectedFile))
    setResult(null)
    setError('')
  }, [])

  function handleFileChange(event) {
    handleFile(event.target.files?.[0])
  }

  function handleDragOver(e) {
    e.preventDefault()
    setDragOver(true)
  }

  function handleDragLeave(e) {
    e.preventDefault()
    setDragOver(false)
  }

  function handleDrop(e) {
    e.preventDefault()
    setDragOver(false)
    const droppedFile = e.dataTransfer.files?.[0]
    handleFile(droppedFile)
  }

  async function handleAnalyze() {
    if (!file) return
    setLoading(true)
    setError('')
    setResult(null)

    const formData = new FormData()
    formData.append('file', file)

    try {
      const response = await fetch('/api/disease/predict', {
        method: 'POST',
        body: formData,
      })
      const data = await response.json()
      if (!response.ok) {
        throw new Error(data.detail || data.message || 'Prediction failed')
      }
      setResult(data.data)
    } catch (err) {
      setError(err.message || 'Could not reach backend. Is the server running?')
    } finally {
      setLoading(false)
    }
  }

  function handleClear() {
    setFile(null)
    setPreview(null)
    setResult(null)
    setError('')
    if (fileInputRef.current) fileInputRef.current.value = ''
  }

  const confidencePercent = result ? (result.confidence * 100).toFixed(1) : 0
  const isLowConf = result && result.confidence < 0.6

  return (
    <div>
      <h1 className="page-title">🔬 Disease Detection</h1>
      <p className="page-subtitle">Upload a crop or leaf image for AI-powered disease analysis.</p>

      <div className="disease-layout">
        {/* Upload Section */}
        <div className="card disease-card">
          <h2 className="card-heading">Upload Crop Image</h2>

          <div
            className={`upload-zone ${dragOver ? 'drag-over' : ''} ${preview ? 'has-image' : ''}`}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
            onClick={() => fileInputRef.current?.click()}
          >
            {preview ? (
              <img src={preview} alt="Crop preview" className="preview-img" />
            ) : (
              <div className="upload-placeholder">
                <span className="upload-icon">📷</span>
                <p className="upload-text">Drag & drop your leaf image here</p>
                <p className="upload-hint">or click to browse files</p>
                <span className="upload-formats">Supports JPEG, PNG</span>
              </div>
            )}
            <input
              ref={fileInputRef}
              type="file"
              accept="image/jpeg,image/png,image/jpg"
              onChange={handleFileChange}
              hidden
            />
          </div>

          <div className="action-row">
            <button
              type="button"
              className="primary-btn analyze-btn"
              disabled={!file || loading}
              onClick={handleAnalyze}
            >
              {loading ? (
                <>
                  <span className="spinner"></span>
                  Analyzing...
                </>
              ) : (
                '🔍 Analyze Crop'
              )}
            </button>
            {file && (
              <button type="button" className="secondary-btn" onClick={handleClear}>
                ✕ Clear
              </button>
            )}
          </div>

          {error && (
            <div className="alert alert-error">
              <span className="alert-icon">⚠️</span>
              <span>{error}</span>
            </div>
          )}
        </div>

        {/* Result Section */}
        {result && (
          <div className="card result-section">
            <div className={`result-banner ${result.is_healthy ? 'healthy' : 'diseased'}`}>
              <span className="result-emoji">{result.is_healthy ? '✅' : '⚠️'}</span>
              <div>
                <h2 className="result-title">
                  {result.is_healthy ? 'Healthy Crop' : 'Disease Detected'}
                </h2>
                <p className="result-label">{result.class_label}</p>
              </div>
            </div>

            {/* Confidence Meter */}
            <div className="confidence-section">
              <div className="confidence-header">
                <span className="confidence-title">Confidence</span>
                <span className={`confidence-value ${isLowConf ? 'low' : ''}`}>
                  {confidencePercent}%
                </span>
              </div>
              <div className="confidence-bar-bg">
                <div
                  className={`confidence-bar-fill ${isLowConf ? 'low' : ''}`}
                  style={{ width: `${confidencePercent}%` }}
                />
              </div>
              {isLowConf && (
                <p className="confidence-warning">
                  ⚠ Low confidence — consider uploading a clearer image or consult an expert.
                </p>
              )}
            </div>

            {/* Precaution */}
            <div className="precaution-section">
              <h3>💊 Recommended Action</h3>
              <p>{result.precaution}</p>
            </div>

            {/* Top Predictions */}
            {result.top_predictions && result.top_predictions.length > 1 && (
              <div className="top-predictions">
                <h3>📊 Top Predictions</h3>
                <div className="predictions-list">
                  {result.top_predictions.map((pred, index) => (
                    <div key={index} className="prediction-item">
                      <span className="pred-rank">#{index + 1}</span>
                      <span className="pred-label">{pred.class_label}</span>
                      <span className="pred-conf">{(pred.confidence * 100).toFixed(1)}%</span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Disclaimer */}
            <div className="disclaimer">
              <p>
                <strong>Note:</strong> This is an AI prediction and may not be 100% accurate.
                Always consult a local agriculture expert for critical decisions.
              </p>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
