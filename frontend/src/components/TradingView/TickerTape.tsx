import * as React from "react";
import { TickerTape } from "widgets/react-ts-tradingview-widgets/dist";
import Box from "@mui/material/Box";
import useAuth from "user/useAuth";

interface Watchlist {
  name: string;
  items: string[];
}

export default function TVTickerTape() {
  const {
    user: { watchlists },
  } = useAuth();

  const symbols = watchlists.flatMap((watchlist: Watchlist) =>
    watchlist.items.map((item) => `ASX:${item.split(".")[0]}`)
  );

  const tickerSymbols = symbols.map((symbol: string) => ({
    proName: symbol,
    title: symbol.split(":")[1],
  }));

  return (
    <Box>
      <TickerTape
        colorTheme="dark"
        displayMode="regular"
        symbols={tickerSymbols}
      ></TickerTape>
    </Box>
  );
}
