import * as React from "react";
import Container from "@mui/material/Container";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import TradingView from "@/components/tables/tradingview";

const rounded = (num: any) => (Math.round(num * 100) / 100).toFixed(2);

function Home({ posts }: { posts: any }) {
  return (
    <Container maxWidth="lg">
      <Box
        sx={{
          my: 4,
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Typography variant="h4" component="h1" gutterBottom>
          Home Page
        </Typography>
        <TradingView />
      </Box>
    </Container>
  );
}

// export async function getStaticProps() {
//   const res = await fetch("http://127.0.0.1:8000/api/");
//   const posts = await res.json();
//   console.log("fetch completed from index.tsx");

//   return {
//     props: {
//       posts,
//     },
//   };
// }

export default Home;
