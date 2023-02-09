import * as React from "react";
import { lazy, useEffect, useState } from "react";
import { styled, useTheme, Theme } from "@mui/material/styles";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import { useRouter } from "next/router";
import dynamic from "next/dynamic";
import TVProfile from "@/components/TradingView/Profile";
import TVStockData from "@/components/TradingView/StockData";

const LazyChart = dynamic(
  () => import("@/components/TradingView/RealTimeChart"),
  { ssr: false }
);

export default function Stock() {
  const router = useRouter();
  const { symbol } = router.query as { symbol: string };
  const ticker = "ASX:" + symbol;

  React.useEffect(() => {
    const logo = document.querySelector(
      "label__link-w6JJhLCp"
    ) as HTMLInputElement | null;
    if (logo != null) {
      console.log(logo);
    } else {
      console.log("No");
    }
  });

  return (
    <React.Fragment>
      <Box
        sx={{
          display: "flex",
          height: 510,
        }}
      >
        <LazyChart symbol={ticker} />
        <TVStockData symbol={ticker} />
      </Box>
      <Box
        sx={{
          display: "flex",
          height: 510,
        }}
      >
        <TVProfile symbol={ticker} />
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
