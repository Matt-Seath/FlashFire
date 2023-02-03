import * as React from "react";
import Container from "@mui/material/Container";
import { Box } from "@mui/material";

const rounded = (num: any) => (Math.round(num * 100) / 100).toFixed(2);

function Home({ posts }: { posts: any }) {
  return (
    <Container>
      <p>Home Page</p>
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
