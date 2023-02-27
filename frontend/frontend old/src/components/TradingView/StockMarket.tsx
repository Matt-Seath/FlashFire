import Box from "@mui/material/Box";
import * as React from "react";
import { StockMarket } from "widgets/react-ts-tradingview-widgets/dist";

export default function TVStockMarket() {
  return (
    <Box>
      <StockMarket colorTheme="dark" height={400} width="100%"></StockMarket>
    </Box>
  );
}
