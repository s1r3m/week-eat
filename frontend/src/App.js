import React from 'react';

import Header from './common/Header';
import Footer from './common/Footer';


function App() {
    const handlePing = async () => {
        try {
            const response = await fetch('http://localhost:8000/ping');
            const body = await response.json();
            alert(body);
        } catch (error) {
            alert('Error: Unable to reach the server: ' + error);
        }
    };

    return (
        <>
            <Header />
            <button onClick={handlePing}>Ping</button>
            <Footer />
        </>
    );
}

export default App;
