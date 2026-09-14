import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'
import Layout from './components/Layout'
import Dashboard from './pages/Dashboard'
import DiseaseDetection from './pages/DiseaseDetection'
import CropRecommendation from './pages/CropRecommendation'
import SmartIrrigation from './pages/SmartIrrigation'
import Sustainability from './pages/Sustainability'
import Innovation from './pages/Innovation'
import FarmerAssistant from './pages/FarmerAssistant'
import AIAdvisor from './pages/AIAdvisor'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Dashboard />} />
          <Route path="disease" element={<DiseaseDetection />} />
          <Route path="crop" element={<CropRecommendation />} />
          <Route path="irrigation" element={<SmartIrrigation />} />
          <Route path="sustainability" element={<Sustainability />} />
          <Route path="innovation" element={<Innovation />} />
          <Route path="assistant" element={<FarmerAssistant />} />
          <Route path="advisor" element={<AIAdvisor />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
