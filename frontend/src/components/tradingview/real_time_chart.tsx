import * as React from "react";
import { AdvancedRealTimeChart } from "react-ts-tradingview-widgets";

export default function TWRealTimeChart({ symbol }: { symbol: any }) {
  return (
    <AdvancedRealTimeChart
      theme="dark"
      width="100%"
      height="140%"
      timezone="Australia/Brisbane"
      symbol={"ASX:" + symbol}
    ></AdvancedRealTimeChart>
  );
}
