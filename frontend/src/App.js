import React from "react";

import Header from "./common/Header";
import Footer from "./common/Footer";
import LoginForm from "./common/LoginForm";

import styles from "./App.module.css";

function Main() {
    return (
        <main className={styles.main}>
            <div className={styles.page_title}>
                <h2>New User Form</h2>
            </div>
            <div className={styles.content}>
                <LoginForm />
            </div>
        </main>
    );
}


export default function App() {
    const handlePing = async () => {
        try {
            const response = await fetch("http://localhost:8000/ping");
            const body = await response.json();
            alert(body);
        } catch (error) {
            alert("Error: Unable to reach the server: " + error);
        }
    };

    return (
        <>
            <Header />
            <Main />
            <Footer />
        </>
    );
}
