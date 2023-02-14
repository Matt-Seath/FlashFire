import * as React from "react";
import { useEffect, useState } from "react";
import Head from "next/head";
import { AppProps } from "next/app";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import { CacheProvider, EmotionCache } from "@emotion/react";
import theme from "../theme";
import createEmotionCache from "../createEmotionCache";
import "../styles/globals.css";
import Layout from "@/components/Layout/Layout";
import { useRouter } from "next/router";
import Login from "@/components/Auth/Login";

const lightTheme = createTheme({
  palette: {
    mode: "light",
  },
});

const darkTheme = createTheme({
  palette: {
    mode: "dark",
  },
});

function getActiveTheme(themeMode: "light" | "dark") {
  return themeMode === "light" ? lightTheme : darkTheme;
}

// Client-side cache, shared for the whole session of the user in the browser.
const clientSideEmotionCache = createEmotionCache();

interface MyAppProps extends AppProps {
  emotionCache?: EmotionCache;
}

export default function MyApp(props: MyAppProps) {
  const { Component, emotionCache = clientSideEmotionCache, pageProps } = props;
  const [activeTheme, setActiveTheme] = useState(lightTheme);
  const [selectedTheme, setSelectedTheme] = useState<"light" | "dark">("light");
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const router = useRouter();

  const toggleTheme: React.MouseEventHandler<HTMLAnchorElement> = () => {
    const desiredTheme = selectedTheme === "light" ? "dark" : "light";

    setSelectedTheme(desiredTheme);
  };

  useEffect(() => {
    async function checkLogin() {
      try {
        const response = await fetch("/api/check-login");
        if (response.ok) {
          setIsLoggedIn(true);
        } else {
          router.push("/login");
        }
      } catch (error) {
        console.error(error);
      }
    }
    checkLogin();
  }, []);

  useEffect(() => {
    setActiveTheme(getActiveTheme(selectedTheme));
  }, [selectedTheme]);

  if (!isLoggedIn) {
    return <Login />;
  }

  return (
    <CacheProvider value={emotionCache}>
      <Head>
        <meta name="viewport" content="initial-scale=1, width=device-width" />
      </Head>
      <ThemeProvider theme={darkTheme}>
        <CssBaseline />
        <Layout>
          <Component {...pageProps} toggleTheme={toggleTheme} />
        </Layout>
      </ThemeProvider>
    </CacheProvider>
  );
}
