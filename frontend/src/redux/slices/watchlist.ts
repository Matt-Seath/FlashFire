import { createSlice } from '@reduxjs/toolkit';
import { Watchlist } from './types';
import { getWatchlists } from 'utils/utils';

const initialState : Watchlist[] = []

// const watchlistSlice = createSlice({
//   name: 'watchlist',
//   initialState,
//   reducers: {
//     addToWatchlist: (state, action) => {
//       state.symbols.push(action.payload);
//     },
//     removeFromWatchlist: (state, action) => {
//       state.symbols = state.symbols.filter(symbol => symbol !== action.payload);
//     },
//   },
// });

// export const { addToWatchlist, removeFromWatchlist } = watchlistSlice.actions;
// export default watchlistSlice.reducer;