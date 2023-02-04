import { useRouter } from "next/router";

const Post = () => {
  const router = useRouter();
  const { symbol } = router.query;

  return <p>Post: {symbol}</p>;
};

export default Post;
