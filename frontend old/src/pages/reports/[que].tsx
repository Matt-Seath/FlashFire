import { useRouter } from "next/router";
import { useEffect, useState } from "react";

export default function Home() {
  const router = useRouter();

  const [isReady, setIsReady] = useState(router.isReady);
  const [hasMounted, setHasMounted] = useState(false);

  // Set router.isReady when the page has mounted
  useEffect(() => {
    setIsReady(router.isReady);
  }, [router]);

  // Blocking hydration warning
  useEffect(() => {
    setHasMounted(true);
  }, []);
  if (!hasMounted) {
    return null;
  }

  return (
    <div>
      <h2>{isReady ? "REady" : "Route is not ready"}</h2>
    </div>
  );
}
