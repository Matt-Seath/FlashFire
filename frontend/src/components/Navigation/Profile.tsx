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
        <Typography
          variant="h6"
          noWrap
          component={Link}
          href={PATH_USER.root}
          sx={{
            mr: 2,
            display: { xs: "none", md: "flex" },
            fontFamily: "monospace",
            fontWeight: 700,
            letterSpacing: ".3rem",
            color: "inherit",
            textDecoration: "none",
          }}
        >
          {user?.email}
        </Typography>
        <AdbIcon sx={{ display: { xs: "flex", md: "none" }, mr: 1 }} />
        <Box sx={{ flexGrow: 0 }}>
          <IconButton
            size="large"
            color="inherit"
            component={Link}
            href={PATH_USER.root}
            sx={{ p: 0 }}
          >
            <AccountCircle />
          </IconButton>
        </Box>
      </Toolbar>
    </Container>
  );
};

export default FFProfile;
