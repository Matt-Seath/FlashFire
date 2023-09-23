import { Box } from "@mui/material";
import * as React from "react";
import { FundamentalData } from "widgets/react-ts-tradingview-widgets/dist";

export default function TVStockData({ symbol }: { symbol: any }) {
  return (
    <Box sx={{ height: "100%", width: "70%" }}>
      <FundamentalData
        width={"100%"}
        height={800}
        symbol={symbol}
        colorTheme="dark"
      ></FundamentalData>
    </Box>
  );
}
