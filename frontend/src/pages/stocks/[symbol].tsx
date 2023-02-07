import * as React from "react";
import { lazy, useEffect, useState } from "react";
import { styled, useTheme, Theme } from "@mui/material/styles";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import { useRouter } from "next/router";
import TVStockData from "@/components/tradingview/stock_data";
import dynamic from "next/dynamic";
import { Height } from "@mui/icons-material";

const LazyChart = dynamic(
  () => import("@/components/tradingview/real_time_chart"),
  { ssr: false }
);

export default function Stock() {
  const router = useRouter();
  const { symbol } = router.query;

  return (
    <React.Fragment>
      <Box sx={{height: 380 }}>
        <Typography>Ticker: {symbol}</Typography>
      </Box>
      <Box
        sx={{
          display: "flex",
          height: 510,
        }}
      >
        <LazyChart symbol={symbol} />
        <TVStockData symbol={symbol} />
      </Box>
    </React.Fragment>
  );
}

// export async function getSeverSideProps() {
//   const res = await fetch("http://127.0.0.1:8000/api/");
//   const posts = await res.json();
//   console.log("fetch completed from index.tsx");

//   return {
//     props: {
//       posts,
//     },
//   };
// }
