import * as React from "react";
import { Screener } from "widgets/react-ts-tradingview-widgets/dist";
import Box from "@mui/material/Box";

export default function TVScreener() {
  return (
    <Box>
      <Screener colorTheme="dark" width="100%" height={300}></Screener>
    </Box>
  );
}
