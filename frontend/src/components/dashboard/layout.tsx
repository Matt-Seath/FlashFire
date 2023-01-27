import * as React from "react";
import Container from "@mui/material/Container";
import FFDrawer from "./drawer";
import FFAppBar from "./appbar";

export default function FFDashboardNav() {
  return (
    <Container>
      <FFDrawer />
      <FFAppBar />
    </Container>
  );
}
