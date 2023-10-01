import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { Watchlist } from "./types";

interface WatchlistsState {
  watchlists: any | null;
}

const initialState: WatchlistsState = {
  watchlists: null,
};

export const watchlistsSlice = createSlice({
  name: "watchlists",
  initialState,
  reducers: {
    setWatchlists: (state, action: PayloadAction<Watchlist[]>) => {
      state.watchlists = action.payload;
    },
    clearWatchlists: (state) => {
      state.watchlists = null;
    },
  },
});

export const { setWatchlists, clearWatchlists } = watchlistsSlice.actions;
export default watchlistsSlice.reducer;