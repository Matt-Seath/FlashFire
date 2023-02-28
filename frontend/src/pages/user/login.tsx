import { NextPage } from "next";
import { Box, Stack, Typography } from "@mui/material";
import LoginForm from "../../user/LoginForm";
import Link from "next/link";
import { PATH_USER } from "../../routes/paths";
import Image from "next/image";
import Logo from "../../../public/Logo.svg";
import styles from "../../styles/GradientBG.module.css";
import Footer from "components/Footer/Footer";

// ----------------------------------------------------------------------

const LoginPage: NextPage = ({}) => {
  return (
    <Stack
      className={styles.container}
      alignItems="center"
      sx={{ height: "100vh" }}
    >
      <Box justifyContent={"center"} mt={25} mb={5}>
        <Image src={Logo} alt="sdd" width={300} />
      </Box>
      <LoginForm />

      <Typography sx={{ mt: 2 }}>Don't have an account?</Typography>
      <Link href={PATH_USER.signup}>
        <Typography color={"lightBlue"}>Sign up</Typography>
      </Link>
      <Footer />
    </Stack>
  );
};

export default LoginPage;
