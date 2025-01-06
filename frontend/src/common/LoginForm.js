import React, { useState } from "react";

import styles from "./loginForm.module.css";


const LoginForm = () => {
  const [firstName, setFirstName] = useState("test");
  const [lastName, setLastName] = useState("");
  const [age, setAge] = useState(7);
  const [address, setAddress] = useState("");
  const [classNumber, setClassNumber] = useState("");
  const [studentID, setStudentID] = useState(1);
  const [favoruiteMeal, setFavoriteMeal] = useState("0");

  const SETTER_MAP = {
    firstname: setFirstName,
    lastname: setLastName,
    age: setAge,
    address: setAddress,
    class_number: setClassNumber,
    studentid: setStudentID,
  }

  const handlerUserInput = ({ target }) => {
    const setter = SETTER_MAP[target.id]
    setter(target.value);
  };

  return (
    <form className={styles.login}>
      <label htmlFor="firstname">First name:&nbsp;
        <input id="firstname" type="text" value={firstName} onChange={handlerUserInput} />
      </label>
      <label htmlFor="lastname">Last name:&nbsp;
        <input id="lastname" type="text" value={lastName} onChange={handlerUserInput} />
      </label>
      <label htmlFor="age">Age:&nbsp;
        <input id="age" type="number" value={age} min="7" max="100" onChange={handlerUserInput} />
      </label>
      <label htmlFor="address">Address:&nbsp;
        <input id="address" type="text" value={address} onChange={handlerUserInput} />
      </label>
      <label htmlFor="class_number">Class number:&nbsp;
        <input id="class_number" type="text" value={classNumber} onChange={handlerUserInput} />
      </label>
      <label htmlFor="studentid">Student ID:&nbsp;
        <input id="studentid" type="number" value={studentID} onChange={handlerUserInput} />
      </label>
      <input className={styles.submit} type="submit" value="Register" />
    </form>
  );
}

export default LoginForm;
