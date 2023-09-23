import * as React from "react";
import Box from "@mui/material/Box";
import { SymbolOverview } from "widgets/react-ts-tradingview-widgets/dist";

export default function TVSymbolOverview({ symbol }: { symbol: string[][] }) {
  return (
    <Box sx={{ height: 500, width: "100%"}}>
      <SymbolOverview
        symbols={symbol}
        colorTheme="dark"
        autosize
        dateFormat="dd MMM 'yy"
      ></SymbolOverview>
    </Box>
  );
}
