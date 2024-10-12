import React from 'react';
import ReactDOM from 'react-dom/client'; // Import for React 18 and above
import App from './App'; // Ensure the path to your App.js is correct

import './index.css'; // Assuming you want to import global styles

// Get the element in your HTML file where you want to mount your React app
const rootElement = document.getElementById('root');
if (!rootElement) throw new Error('Failed to find the root element');

// Create a root.
const root = ReactDOM.createRoot(rootElement);

// Render your App component within the root.
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
