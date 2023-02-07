import * as React from "react";
import Container from "@mui/material/Container";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import TVStockMarket from "@/components/tradingview/stock_market";

const rounded = (num: any) => (Math.round(num * 100) / 100).toFixed(2);

function Home({ posts }: { posts: any }) {
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
          Home Page
        </Typography>
        <TVStockMarket />
      </Box>
    </Container>
  );
}

export default Home;
