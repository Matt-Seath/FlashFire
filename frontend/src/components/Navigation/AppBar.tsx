import * as React from "react";
import { styled, useTheme } from "@mui/material/styles";
import MuiAppBar, { AppBarProps as MuiAppBarProps } from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import { drawerWidth } from "./Drawer";
import SearchBar from "./SearchBar";
import FFProfile from "./Profile";
import TVTickerTape from "../TradingView/TickerTape";

interface AppBarProps extends MuiAppBarProps {
  open?: boolean;
}

interface DrawerProps {
  open: boolean;
  setOpen: React.Dispatch<React.SetStateAction<boolean>>;
}

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== "open",
})<AppBarProps>(({ theme, open }) => ({
  width: `calc(100% - ${65}px)`,
  transition: theme.transitions.create(["width", "margin"], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(["width", "margin"], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));

export default function FFAppBar({ open, setOpen }: DrawerProps) {
  const theme = useTheme();

  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };

  return (
    <AppBar position="fixed" open={open}>
      <Toolbar>
        <IconButton
          color="inherit"
          aria-label="open drawer"
          onClick={handleDrawerClose}
          edge="start"
          sx={{
            ...(!open && { display: "none" }),
          }}
        >
          <MenuIcon />
        </IconButton>
        <IconButton
          color="inherit"
          aria-label="close drawer"
          onClick={handleDrawerOpen}
          edge="start"
          sx={{
            ...(open && { display: "none" }),
          }}
        >
          <MenuIcon />
        </IconButton>
        <SearchBar />
        <FFProfile />
      </Toolbar>
      <TVTickerTape />
    </AppBar>
  );
}
