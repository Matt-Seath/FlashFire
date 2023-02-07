import * as React from "react";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import { useRouter } from "next/router";
import TWRealTimeChart from "@/components/tradingview/real_time_chart";

export default function Stock() {
  const router = useRouter();
  const { symbol } = router.query;
  return <TWRealTimeChart symbol={symbol} />;
}
