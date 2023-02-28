import { NextPage } from "next";
import { Box, Stack, Typography } from "@mui/material";
import SignupForm from "../../user/SignupForm";
import { PATH_USER } from "../../routes/paths";
import Link from "next/link";
import Image from "next/image";
import Logo from "../../../public/Logo.svg";
import styles from "../../styles/GradientBG.module.css";
import Footer from "components/Footer/Footer";

// ----------------------------------------------------------------------

const Signup: NextPage = ({}) => {
  return (
    <Stack
      className={styles.container}
      alignItems="center"
      sx={{ height: "100vh" }}
    >
      <Box justifyContent={"center"} mt={25} mb={5}>
        <Image src={Logo} alt="sdd" width={300} />
      </Box>
      <SignupForm />

      <Typography sx={{ mt: 2 }}>Already have an account?</Typography>
      <Link href={PATH_USER.login}>
        <Typography color={"lightBlue"}>Log in</Typography>
      </Link>
      <Footer />
    </Stack>
  );
};

export default Signup;
