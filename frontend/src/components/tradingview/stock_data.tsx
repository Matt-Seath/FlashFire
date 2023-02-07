import { Box } from "@mui/material";
import * as React from "react";
import { FundamentalData } from "react-ts-tradingview-widgets";

export default function TVStockData({ symbol }: { symbol: any }) {
  return (
    <Box sx={{ height: "100%", width: "50%" }}>
      <FundamentalData
        width={"100%"}
        height={500}
        symbol={"ASX:" + symbol}
        colorTheme="dark"
      ></FundamentalData>
    </Box>
  );
}
