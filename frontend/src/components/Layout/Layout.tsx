import * as React from "react";
import Box from "@mui/material/Box";
import CssBaseline from "@mui/material/CssBaseline";
import FFNavigation from "./Navigation";
import { DrawerHeader } from "./Drawer";

export default function Layout({ children }: { children: any }) {
  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      <FFNavigation />
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <DrawerHeader />
        {children}
      </Box>
    </Box>
  );
}
