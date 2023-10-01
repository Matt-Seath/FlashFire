import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { Watchlist } from "./types";

interface WatchlistState {
  currentWatchlist: Watchlist | null;
}

const initialState: WatchlistState = {
  currentWatchlist: null,
};

export const watchlistSlice = createSlice({
  name: "watchlist",
  initialState,
  reducers: {
    setWatchlist: (state, action: PayloadAction<Watchlist>) => {
      state.currentWatchlist = action.payload;
    },
    clearWatchlist: (state) => {
      state.currentWatchlist = null;
    },
  },
});

export const { setWatchlist, clearWatchlist } = watchlistSlice.actions;
export default watchlistSlice.reducer;