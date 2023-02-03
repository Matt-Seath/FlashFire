import * as React from "react";
import Container from "@mui/material/Container";
import { Box } from "@mui/material";

const rounded = (num: any) => (Math.round(num * 100) / 100).toFixed(2);

function Home({ posts }: { posts: any }) {
  return (
    <Container>
      <div>
        {console.log(typeof posts)}
        {console.log(posts)}
        {posts.map((post: any) => (
          <div>
            <p>{post.symbol}</p>
            <p>{post.long_name}</p>
            <p>{post.sector}</p>
            {post.history.map((hist: any) => (
              <Box sx={{ display: "flex" }}>
                <p>Date: {hist.date}</p>
                <p>Open: {rounded(hist.open)}</p>
                <p>Close: {rounded(hist.close)}</p>
                <p>High: {rounded(hist.high)}</p>
                <p>Low: {rounded(hist.low)}</p>
                <p>Volume: {rounded(hist.volume)}</p>
              </Box>
            ))}
          </div>
        ))}
      </div>
    </Container>
  );
}

export async function getStaticProps() {
  const res = await fetch("http://127.0.0.1:8000/api/");
  const posts = await res.json();
  console.log("fetch completed from index.tsx");

  return {
    props: {
      posts,
    },
  };
}

export default Home;
