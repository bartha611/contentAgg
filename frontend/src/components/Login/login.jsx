import React, { useState, useEffect } from "react";
import { Form, Input, Label, FormGroup, Button } from "reactstrap";

const Login = () => {
  const handleEnter = e => {
    const { keyCode } = e;
    if (keyCode === 13) {
      console.log("you have pressed enter");
    }
  };
  useEffect(() => {
    window.addEventListener("keydown", handleEnter);
    return () => window.removeEventListener("keydown", handleEnter);
  });
  const submit = () => {
    console.log("you have submitted form");
  };
  return (
    <Form>
      <FormGroup>
        <Label for="username">Username</Label>
        <Input type="text" id="username" placeholder="username" />
      </FormGroup>
      <FormGroup>
        <Label for="password">Password</Label>
        <Input type="password" id="password" placeholder="****" />
      </FormGroup>
      <Button onClick={() => submit()}>Submit</Button>
    </Form>
  );
};

export default Login;
