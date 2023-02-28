import { NextPage } from "next";
import { Stack, Typography } from "@mui/material";
import LoginForm from "../../user/LoginForm";
import Link from "next/link";
import { PATH_USER } from "../../routes/paths";

// ----------------------------------------------------------------------

const LoginPage: NextPage = ({}) => {
  return (
    <Stack justifyContent="center" alignItems="center" sx={{ height: "100vh" }}>
      <LoginForm />

      <Typography sx={{ mt: 2 }}>Don't have an account?</Typography>
      <Link href={PATH_USER.signup}>
        <Typography color={"lightBlue"}>Sign up</Typography>
      </Link>
    </Stack>
  );
};

export default LoginPage;
