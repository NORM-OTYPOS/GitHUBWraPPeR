// src/App.tsx
import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Home from './pages/ Home';
import Report from './pages/Report';

const App: React.FC = () => {
    return (
        <div>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/report/:username" element={<Report />} />
            </Routes>
        </div>
    );
};

export default App;
