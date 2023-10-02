import * as React from "react";
import { TickerTape } from "widgets/react-ts-tradingview-widgets/dist";
import Box from "@mui/material/Box";
import { getWatchlists } from "utils/utils";
import { Watchlist } from "redux/slices/types";
import { useTypeDispatch, useTypedSelector } from "redux/store";
import { setWatchlists } from "redux/slices/watchlists";

export default function TVTickerTape() {
  const dispatch = useTypeDispatch();
  const storedWatchlists: Watchlist[] = useTypedSelector(
    (state) => state.watchlists.watchlists
  );
  const { watchlists }: { watchlists: Watchlist[] } = getWatchlists();
  const currentWatchlists =
    storedWatchlists !== null ? storedWatchlists : watchlists;

  if (!storedWatchlists) {
    try {
      dispatch(setWatchlists(watchlists));
      console.log("Updated Watchlist Slice");
    } catch (error) {
      console.error(error);
    }
  }

  if (!currentWatchlists) {
    return null;
  }

  const symbols = currentWatchlists.flatMap((watchlist) =>
    watchlist.items.map((item) => `ASX:${item.stock.symbol.split(".")[0]}`)
  );

  const tickerSymbols = symbols.map((symbol: string) => ({
    proName: symbol,
    title: symbol.split(":")[1],
  }));

  return (
    <Box>
      <TickerTape colorTheme="dark" displayMode="regular"></TickerTape>
    </Box>
  );
}
