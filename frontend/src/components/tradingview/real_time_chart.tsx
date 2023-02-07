import * as React from "react";
import { AdvancedRealTimeChart } from "react-ts-tradingview-widgets";

export default function TWRealTimeChart({ symbol }: { symbol: any }) {
  return (
    <AdvancedRealTimeChart
      theme="dark"
      width="100%"
      height="140%"
      style="3"
      interval="3"
      timezone="Australia/Brisbane"
      hide_legend={true}
      hide_side_toolbar={true}
      hide_top_toolbar={true}
      symbol={"ASX:" + symbol}
    ></AdvancedRealTimeChart>
  );
}
