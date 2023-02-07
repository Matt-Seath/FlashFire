import * as React from "react";
import { styled, useTheme, Theme, CSSObject } from "@mui/material/styles";
import Box from "@mui/material/Box";
import MuiDrawer from "@mui/material/Drawer";
import List from "@mui/material/List";
import Divider from "@mui/material/Divider";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import CandlestickChartIcon from "@mui/icons-material/CandlestickChart";
import WhatshotIcon from "@mui/icons-material/Whatshot";
import EqualizerIcon from "@mui/icons-material/Equalizer";
import TroubleshootIcon from "@mui/icons-material/Troubleshoot";
import QueryStatsIcon from "@mui/icons-material/QueryStats";
import ReceiptLongIcon from "@mui/icons-material/ReceiptLong";
import ContentPasteSearchIcon from "@mui/icons-material/ContentPasteSearch";
import SettingsIcon from "@mui/icons-material/Settings";

import Link from "next/link";

export const drawerWidth = 240;

export const DrawerHeader = styled("div")(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  justifyContent: "flex-end",
  padding: theme.spacing(9, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
}));

const openedMixin = (theme: Theme): CSSObject => ({
  width: drawerWidth,
  transition: theme.transitions.create("width", {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.enteringScreen,
  }),
  overflowX: "hidden",
});

const closedMixin = (theme: Theme): CSSObject => ({
  transition: theme.transitions.create("width", {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  overflowX: "hidden",
  width: `calc(${theme.spacing(7)} + 1px)`,
  [theme.breakpoints.up("sm")]: {
    width: `calc(${theme.spacing(8)} + 1px)`,
  },
});

const Drawer = styled(MuiDrawer, {
  shouldForwardProp: (prop) => prop !== "open",
})(({ theme, open }) => ({
  width: drawerWidth,
  flexShrink: 0,
  whiteSpace: "nowrap",
  boxSizing: "border-box",
  ...(open && {
    ...openedMixin(theme),
    "& .MuiDrawer-paper": openedMixin(theme),
  }),
  ...(!open && {
    ...closedMixin(theme),
    "& .MuiDrawer-paper": closedMixin(theme),
  }),
}));

const styles = {
  largeIcon: {
    width: 60,
    height: 60,
  },
};

export default function FFDrawer({ open }: { open: any }) {
  const theme = useTheme();

  return (
    <Drawer variant="permanent" open={open}>
      <List>
        {["FlashFire"].map((text, index) => (
          <ListItem key={text} disablePadding sx={{ display: "block" }}>
            <Link href="/" passHref>
              <ListItemButton
                sx={{
                  MaxHeight: 2,
                  justifyContent: "left",
                  px: 2,
                }}
              >
                <Box
                  component="img"
                  sx={{
                    maxHeight: 32,
                    mr: open ? 3 : "auto",
                    justifyContent: open ? "initial" : "center",
                  }}
                  alt="FlashFire Logo"
                  src="/FF_Logo.svg"
                />
                <Box
                  component="img"
                  sx={{
                    maxWidth: 90,
                    justifyContent: open ? "initial" : "center",
                    opacity: open ? 1 : 0,
                  }}
                  alt="FlashFire Logo"
                  src="/FF_Text.svg"
                />
              </ListItemButton>
            </Link>
          </ListItem>
        ))}
      </List>
      <Divider />
      <List>
        {["Portfolio", "Trader", "Transactions", "Watchlists", "Backtest"].map(
          (text, index) => (
            <ListItem key={text} disablePadding sx={{ display: "block" }}>
              <Link href={("/" + text).toLowerCase()} passHref>
                <ListItemButton
                  sx={{
                    minHeight: 48,
                    justifyContent: open ? "initial" : "center",
                    px: 2.5,
                  }}
                >
                  <ListItemIcon
                    sx={{
                      minWidth: 0,
                      mr: open ? 3 : "auto",
                      justifyContent: "center",
                    }}
                  >
                    {text === "Portfolio" && <EqualizerIcon />}
                    {text === "Trader" && <WhatshotIcon />}
                    {text === "Transactions" && <ReceiptLongIcon />}
                    {text === "Watchlists" && <CandlestickChartIcon />}
                    {text === "Backtest" && <TroubleshootIcon />}
                  </ListItemIcon>
                  <ListItemText primary={text} sx={{ opacity: open ? 1 : 0 }} />
                </ListItemButton>
              </Link>
            </ListItem>
          )
        )}
      </List>
      <Divider />
      <List>
        {["Analytics", "Reports", "Settings"].map((text, index) => (
          <ListItem key={text} disablePadding sx={{ display: "block" }}>
            <Link href={("/" + text).toLowerCase()} passHref>
              <ListItemButton
                sx={{
                  minHeight: 48,
                  justifyContent: open ? "initial" : "center",
                  px: 2.5,
                }}
              >
                <ListItemIcon
                  sx={{
                    minWidth: 0,
                    mr: open ? 3 : "auto",
                    justifyContent: "center",
                  }}
                >
                  {text === "Analytics" && <QueryStatsIcon />}
                  {text === "Reports" && <ContentPasteSearchIcon />}
                  {text === "Settings" && <SettingsIcon />}
                </ListItemIcon>
                <ListItemText primary={text} sx={{ opacity: open ? 1 : 0 }} />
              </ListItemButton>
            </Link>
          </ListItem>
        ))}
      </List>
    </Drawer>
  );
}
