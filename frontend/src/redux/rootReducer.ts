import {combineReducers} from '@reduxjs/toolkit'
import user from "./slices/user";
import watchlist from './slices/watchlist';

// ----------------------------------------------------------------------

const rootReducer = combineReducers({
    user,
    watchlist,
})

export default rootReducer;