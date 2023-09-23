import * as React from "react";
import { CompanyProfile } from "widgets/react-ts-tradingview-widgets/dist";
import Box from "@mui/material/Box";

export default function TVProfile({ symbol }: { symbol: string }) {
  return (
    <Box sx={{ height: "100%", width: "100%" }}>
      <CompanyProfile
        symbol={symbol}
        colorTheme="dark"
        height={500}
        width="100%"
      ></CompanyProfile>
    </Box>
  );
}
