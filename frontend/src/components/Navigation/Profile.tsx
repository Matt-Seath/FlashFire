import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import Menu from "@mui/material/Menu";
import MenuIcon from "@mui/icons-material/Menu";
import Container from "@mui/material/Container";
import Button from "@mui/material/Button";
import MenuItem from "@mui/material/MenuItem";
import AdbIcon from "@mui/icons-material/Adb";
import useAuth from "user/useAuth";
import { AccountCircle } from "@mui/icons-material";
import Link from "next/link";
import { PATH_USER } from "../../routes/paths";

// ----------------------------------------------------------------------

// ----------------------------------------------------------------------

const FFProfile = ({}) => {
  const {
    user,
    logout,
    request: {
      logout: { status, error },
    },
  } = useAuth();

  return (
    <Container
      maxWidth="xl"
      sx={{ display: "flex", justifyContent: "flex-end" }}
    >
      <Toolbar disableGutters>
        <Box display={"grid"} marginRight={2}>
          <Button href={PATH_USER.root} sx={{ m: 0, p: 0 }}>
            <Typography
              sx={{
                fontSize: "0.7rem",
                display: { xs: "none", md: "flex" },
                fontFamily: "inherit",
                fontWeight: 500,
                color: "lightBlue",
                letterSpacing: ".1rem",
                textDecoration: "none",
                textTransform: "none",
                direction: "rtl",
                textAlign: "start",
              }}
            >
              {user?.email}
            </Typography>
          </Button>

          <Button onClick={logout} sx={{ m: 0, p: 0, justifyContent: "end" }}>
            <Typography
              sx={{
                fontSize: "0.7rem",
                display: { xs: "none", md: "flex" },
                fontFamily: "inherit",
                fontWeight: 500,
                color: "grey",
                letterSpacing: ".1rem",
                textDecoration: "none",
                textTransform: "none",
              }}
            >
              Logout
            </Typography>
          </Button>
        </Box>
        <Box sx={{ flexGrow: 0, mr: -3 }}>
          <IconButton
            size="large"
            component={Link}
            href={PATH_USER.root}
            sx={{ p: 0, m: 0 }}
          >
            <AccountCircle color="primary" sx={{ fontSize: "2.2rem" }} />
          </IconButton>
        </Box>
      </Toolbar>
    </Container>
  );
};

export default FFProfile;
