import * as React from "react";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import Layout from "layouts/Layout";
import EnhancedTable from "components/Tables/WatchlistTable";
import ScrollableTabsButtonAuto from "components/Tabs/WatchlistTabs";

Watchlists.getLayout = function getLayout(page: any) {
  return <Layout>{page}</Layout>;
};

export default function Watchlists() {
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
          Watchlists Page
        </Typography>
        <ScrollableTabsButtonAuto />
        <EnhancedTable />
      </Box>
    </Container>
  );
}
