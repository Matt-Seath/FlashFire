import * as React from "react";
import { lazy, useEffect, useState } from "react";
import { styled, useTheme, Theme } from "@mui/material/styles";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import { useRouter } from "next/router";
import dynamic from "next/dynamic";
import TVProfile from "@/components/TradingView/Profile";
import TVStockData from "@/components/TradingView/StockData";
import StocksJSON from "@/pages/api/stocks.json";

const LazyChart = dynamic(
  () => import("@/components/TradingView/RealTimeChart"),
  { ssr: false }
);

interface Stock {
  symbol: string;
  long_name: string;
  sector: string | null;
}

export default function Stock() {
  const router = useRouter();
  const { symbol } = router.query as { symbol: string };
  const ticker = "ASX:" + symbol;
  const stocks = [...StocksJSON];
  const title = stocks.find((e) => e.symbol == symbol);

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
          justifyContent: "space-between",
          height: 80,
        }}
      >
        <h1>{title?.symbol + ": " + title?.long_name}</h1>
        <Box
          sx={{
            display: "flex",
          }}
        >
          <Button variant="contained" color="success">
            BUY
          </Button>
          <Button variant="contained" color="error">
            SELL
          </Button>
        </Box>
      </Box>
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
