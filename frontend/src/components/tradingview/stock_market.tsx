import Box from "@mui/material/Box";
import * as React from "react";
import { StockMarket } from "react-ts-tradingview-widgets";

export default function TVStockMarket() {
  return (
    <Box>
      <StockMarket colorTheme="dark" height={400} width="100%"></StockMarket>
    </Box>
  );
}
