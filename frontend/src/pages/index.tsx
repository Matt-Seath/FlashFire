import * as React from "react";
import Container from "@mui/material/Container";

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
            <p>{post.history.close}</p>
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
