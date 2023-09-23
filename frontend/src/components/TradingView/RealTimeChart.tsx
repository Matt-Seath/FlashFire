import { Box } from "@mui/material";
import * as React from "react";
import { AdvancedRealTimeChart } from "widgets/react-ts-tradingview-widgets/dist";

export default function TVRealTimeChart({ symbol }: { symbol: any }) {
  return (
    <Box sx={{ height: 500, width: "100%" }}>
      <AdvancedRealTimeChart
        theme="dark"
        autosize
        style="1"
        interval="3"
        timezone="Australia/Brisbane"
        hide_legend={true}
        hide_side_toolbar={true}
        hide_top_toolbar={true}
        symbol={symbol}
      ></AdvancedRealTimeChart>
    </Box>
  );
}
