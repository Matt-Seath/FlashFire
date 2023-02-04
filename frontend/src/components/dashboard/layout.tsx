import * as React from "react";
import Box from "@mui/material/Box";
import CssBaseline from "@mui/material/CssBaseline";
import Typography from "@mui/material/Typography";
import { Container } from "@mui/material";
import FFNavigation from "./navigation";
import { DrawerHeader } from "./drawer";


export default function Layout({ children }: { children: any }) {
  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      <FFNavigation />

      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <DrawerHeader />
        <div>{children}</div>
        <Container sx={{ padding: 5 }}>
          <Typography>Hi there</Typography>
        </Container>
      </Box>
    </Box>
  );
}
