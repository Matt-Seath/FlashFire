import { Box } from "@mui/material";
import * as React from "react";

interface LoginProps {
  setIsLoggedIn: (isLoggedIn: boolean) => void;
}

export default function Login({ setIsLoggedIn }: LoginProps) {
  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  return (
    <Box sx={{ height: 500, width: "100%" }}>
      <div>
        <h2>Login Page</h2>
        <button onClick={handleLogin}>Login</button>
      </div>
    </Box>
  );
}
