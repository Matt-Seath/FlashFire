import * as React from "react";
import Box from "@mui/material/Box";
import { SymbolOverview } from "widgets/react-ts-tradingview-widgets/dist";

export default function TVSymbolOverview({ symbol }: { symbol: string[][] }) {
  return (
    <Box>
      <SymbolOverview
        symbols={symbol}
        colorTheme="dark"
        height={400}
        width="100%"
        dateFormat="dd MMM 'yy"
      ></SymbolOverview>
      ;
    </Box>
  );
}
