import * as React from "react";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import Layout from "layouts/Layout";

BackTest.getLayout = function getLayout(page: any) {
  return <Layout>{page}</Layout>;
};

export default function BackTest() {
  return (
    <Container maxWidth="lg">
      <Box
        sx={{
          my: 4,
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Typography variant="h4" component="h1" gutterBottom>
          Backtest Page
        </Typography>
      </Box>
    </Container>
  );
}
