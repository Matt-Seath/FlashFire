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
        <Button onClick={logout} sx={{height: "100%", width: "5rem", mr:1}}>
          <Typography
            variant="h6"
            noWrap
            sx={{
              fontSize: "0.9rem",
              display: { xs: "none", md: "flex" },
              fontFamily: "monospace",
              fontWeight: 500,
              letterSpacing: ".1rem",
              color: "grey",
              textDecoration: "none",
            }}
          >
            Logout
          </Typography>
        </Button>
        <AdbIcon sx={{ display: { xs: "flex", md: "none" }, mr: 1 }} />
        <Box sx={{ flexGrow: 0 }}>
          <IconButton
            size="large"
            color="inherit"
            component={Link}
            href={PATH_USER.root}
            sx={{ p: 0 }}
          >
            <AccountCircle color="success" />
          </IconButton>
        </Box>
      </Toolbar>
    </Container>
  );
};

export default FFProfile;
