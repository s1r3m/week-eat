import React from "react";

import styles from "./header.module.css";


function Label() {
    return (
        <div className={styles.label}>
            <h3>Week&nbsp;Eat&nbsp;Planner</h3>
        </div>
    );
}


function NavMenu(props) {
    return (
        <ul className={styles.navigation}>
        {props.items.map(item => (
                <li className={styles.menu_item}>{item}</li>
            ))}
        </ul>
    );
}

function AuthButtons(props) {
    return (
        <div className={styles.buttons}>
            <button style={{display: props.login ? "block" : "none"}} className={styles.login}>Login</button>
            <button style={{display: props.signup ? "block" : "none"}} className={styles.signup}>Sign Up</button>
            <button style={{display: props.logout ? "block" : "none"}} className={styles.logout}>Logout</button>
        </div>
    );
}


export default function Header() {
    return (
        <header className={styles.container}>
            <Label />
            <NavMenu items={["Weeks", "Meals"]} />
            <AuthButtons login={true} signup={true} logout={false}/>
        </header>
    );
}
