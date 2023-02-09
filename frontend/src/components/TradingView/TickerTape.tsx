import * as React from "react";
import { TickerTape } from "react-ts-tradingview-widgets";
import Box from "@mui/material/Box";

export default function TVTickerTape() {
  return (
    <Box>
      <TickerTape
        colorTheme="dark"
        displayMode="regular"
        symbols={[
          { proName: "ASX:A2M", title: "A2M" },
          { proName: "ASX:WES", title: "WES" },
        ]}
      ></TickerTape>
    </Box>
  );
}
