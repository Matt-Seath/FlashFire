import { NextPage } from "next";
import { Stack, Typography } from "@mui/material";
import SignupForm from "../../user/SignupForm";
import { PATH_USER } from "../../routes/paths";
import Link from "next/link";
import Logo from "../../../public/Logo.svg";

// ----------------------------------------------------------------------

const Signup: NextPage = ({}) => {
  return (
    <div>
      <img src={Logo} alt="sdd" />
      <Stack
        justifyContent="center"
        alignItems="center"
        sx={{ height: "100vh" }}
      >
        <SignupForm />

        <Typography sx={{ mt: 2 }}>Already have an account?</Typography>
        <Link href={PATH_USER.login}>
          <Typography color={"lightBlue"}>Log in</Typography>
        </Link>
      </Stack>
    </div>
  );
};

export default Signup;
