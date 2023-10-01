import * as React from "react";
import { TickerTape } from "widgets/react-ts-tradingview-widgets/dist";
import Box from "@mui/material/Box";
import { getUser, getWatchlists } from "utils/utils";
import { Watchlist } from "redux/slices/types";
import { useTypeDispatch } from "redux/store";
import { setWatchlists } from "redux/slices/watchlists";

export default function TVTickerTape() {
  const { user } = getUser();
  const wl: Watchlist[] = user.watchlists;
  const dispatch = useTypeDispatch();
  const { watchlists } = getWatchlists();

  React.useEffect(() => {
    try {
      const res = dispatch(setWatchlists(wl));
      console.log(res);
    } catch (error) {
      console.error("not happenin", error);
    }
  });

  console.log(watchlists);

  if (!watchlists) {
    return null;
  }

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
