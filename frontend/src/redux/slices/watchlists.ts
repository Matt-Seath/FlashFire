import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { Watchlist } from "./types";

interface WatchlistsState {
  currentWatchlist: Watchlist | null;
}

const initialState: WatchlistsState = {
  currentWatchlist: null,
};

export const watchlistsSlice = createSlice({
  name: "watchlists",
  initialState,
  reducers: {
    setWatchlists: (state, action: PayloadAction<Watchlist>) => {
      state.currentWatchlist = action.payload;
    },
    clearWatchlists: (state) => {
      state.currentWatchlist = null;
    },
  },
});

export const { setWatchlists, clearWatchlists } = watchlistsSlice.actions;
export default watchlistsSlice.reducer;