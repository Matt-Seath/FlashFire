import * as React from "react";
import Container from "@mui/material/Container";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import TVStockMarket from "@/components/TradingView/StockMarket";
import TVScreener from "@/components/TradingView/Screener";

const rounded = (num: any) => (Math.round(num * 100) / 100).toFixed(2);


function Home({ posts }: { posts: any }) {
  return (

    <React.Fragment>
      <Box
        sx={{
          display: "flex",
          height: 510,
        }}
      >
        <TVStockMarket />
        <TVScreener />

      </Box>
      <Box
        sx={{
          display: "flex",
          height: 510,
        }}
      >
        
      </Box>
    </React.Fragment>
  );
}

export default Home;
