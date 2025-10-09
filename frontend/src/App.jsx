import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import Auth from './components/Auth';
import './App.css';

// 受保护的路由组件
const ProtectedRoute = ({ children }) => {
  const { user, loading } = useAuth();
  
  if (loading) {
    return <div>加载中...</div>;
  }
  
  return user ? children : <Navigate to="/auth" />;
};

// 主应用组件
const AppContent = () => {
  const { user, logout } = useAuth();

  return (
    <div className="app">
      <nav className="navbar">
        <h1>热点聚合器</h1>
        {user && (
          <div className="nav-user">
            <span>欢迎, {user.username}</span>
            <button onClick={logout} className="logout-btn">
              退出登录
            </button>
          </div>
        )}
      </nav>
      
      <Routes>
        <Route path="/auth" element={<Auth />} />
        <Route 
          path="/" 
          element={
            <ProtectedRoute>
              <div className="dashboard">
                <h2>欢迎使用热点聚合器</h2>
                <p>您已成功登录！</p>
              </div>
            </ProtectedRoute>
          } 
        />
      </Routes>
    </div>
  );
};

function App() {
  return (
    <AuthProvider>
      <Router>
        <AppContent />
      </Router>
    </AuthProvider>
  );
}

export default App;