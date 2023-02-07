import * as React from "react";
import { CompanyProfile } from "react-ts-tradingview-widgets";
import Box from "@mui/material/Box";

export default function TVProfile({ symbol }: { symbol: string }) {
  return (
    <Box sx={{ height: 500, width: "40%" }}>
      <CompanyProfile
        symbol={symbol}
        colorTheme="dark"
        height={500}
        width="100%"
      ></CompanyProfile>
    </Box>
  );
}
