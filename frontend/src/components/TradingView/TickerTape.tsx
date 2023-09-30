import * as React from "react";
import { TickerTape } from "widgets/react-ts-tradingview-widgets/dist";
import Box from "@mui/material/Box";
import { getWatchlists } from "utils/utils";
import { Watchlist } from "redux/slices/types";

export default function TVTickerTape() {
  const { watchlists }: { watchlists: Watchlist[] } = getWatchlists();

  const symbols = watchlists.flatMap((watchlist) =>
    watchlist.items.map((item) => `ASX:${item.stock.symbol.split(".")[0]}`)
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
