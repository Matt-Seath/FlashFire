import * as React from "react";
import { styled } from "@mui/material/styles";
import Box from "@mui/material/Box";
import CssBaseline from "@mui/material/CssBaseline";
import Typography from "@mui/material/Typography";
import { Container } from "@mui/material";
import FFNav, { DrawerHeader } from "./drawer";


export default function Layout({ children }: { children: any }) {
  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      <FFNav />

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
