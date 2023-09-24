import * as React from "react";
import { TickerTape } from "widgets/react-ts-tradingview-widgets/dist";
import Box from "@mui/material/Box";
import { getUser } from "utils/getUser";
import { Watchlist } from "redux/slices/user";

export default function TVTickerTape() {
  const {
    user: { watchlists },
  } = getUser();

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
