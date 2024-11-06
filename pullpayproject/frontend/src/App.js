import axios from 'axios';
import React from 'react';
import Register from './pages/home/register'
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import Home from './pages/home/home';
import Users from './pages/users/users';
import Login from './pages/home/sign_in';
import UserDashboard from './pages/home/user_dashboard';



function App() {
  return (
    <div className="App">
      <BrowserRouter >
        <Routes>
          <Route path="/home" element={<Home />} />
          <Route path="/Register" element={<Register />} />
          <Route path="/users" element={<Users />} />
          <Route path="/login" element={<Login />} />
          <Route path="/" element={<Navigate to="/home" />} />
          <Route path="/user_dashboard" element={<UserDashboard />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;