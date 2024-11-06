import React from 'react';
import { Link } from 'react-router-dom';
import './home.css';

const LandingPage = () => {
  return (
    <div className="landing-container">
      {/* Hero Section */}
      <header className="hero-section">
        <h1>Welcome to Pullpay</h1>
        <p1>Your church payment solution</p1>
        <button className="cta-button"><Link to="/login">Login</Link></button>

      </header>

      {/* Intro Section */}
      <section className="intro-section">
        <h2>Why Choose Us?</h2>
        <p1>
          Our platform empowers churches to strengthen their missions through dedicated digital solutions designed for generosity and engagement. By simplifying giving, administrative tasks, and personalized engagement, we enable churches to cultivate a culture of generosity. Our suite of tools helps communities of faith increase donations, deepen relationships, and create seamless giving experiences that support growth and community impact.
        </p1>
      </section>


      {/* Call to Action */}
      <footer className="cta-footer">
        <h2>Ready to Get Started?</h2>
        <button className="cta-button"><Link to="/register">Register</Link></button>
      </footer>
    </div>
  );
};

export default LandingPage;
