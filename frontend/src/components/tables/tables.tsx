export async function getStaticProps() {
  const res = await fetch("http://127.0.0.1:8000/api/");
  const posts = await res.json();
  console.log(posts);

  return {
    props: {
      posts,
    },
  };
}
