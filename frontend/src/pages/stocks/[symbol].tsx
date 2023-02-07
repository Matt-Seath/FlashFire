import * as React from "react";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import { useRouter } from "next/router";
import TWRealTimeChart from "@/components/tradingview/real_time_chart";

export default function Stock({ posts }: { posts: any }) {
  const router = useRouter();
  const { symbol } = router.query;
  console.log("posts")
  return (
    <React.Fragment>
      <TWRealTimeChart symbol={symbol} />
    </React.Fragment>
  );
}

export async function getSeverSideProps() {
  const res = await fetch("http://127.0.0.1:8000/api/");
  const posts = await res.json();
  console.log("fetch completed from index.tsx");

  return {
    props: {
      posts,
    },
  };
}
