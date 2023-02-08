import * as React from "react";
import { Screener } from "react-ts-tradingview-widgets";
import Box from "@mui/material/Box";

export default function TVScreener() {
  return (
    <Box>
      <Screener colorTheme="dark" width="100%" height={300}></Screener>
    </Box>
  );
}
