import * as React from "react";
import { TechnicalAnalysis } from "widgets/react-ts-tradingview-widgets/dist";
import Box from "@mui/material/Box";

export default function TVTechnicalAnalysis({ symbol }: { symbol: string }) {
  return (
    <Box sx={{ height: "100%", width: "30%" }}>
      <TechnicalAnalysis
        symbol={symbol}
        colorTheme="dark"
        height={800}
        width="100%"
      ></TechnicalAnalysis>
    </Box>
  );
}
