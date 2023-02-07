import Box from "@mui/material/Box";
import * as React from "react";
import { Timeline } from "react-ts-tradingview-widgets";

export default function TVTimeline({ symbol }: { symbol: any }) {
  return (
    <Box>
      <Timeline
        colorTheme="dark"
        feedMode="symbol"
        symbol={symbol}
        height={500}
        width="100%"
      ></Timeline>
    </Box>
  );
}
