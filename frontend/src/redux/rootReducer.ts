import {combineReducers} from '@reduxjs/toolkit'
import user from "./slices/user";
import watchlists from './slices/watchlists';

// ----------------------------------------------------------------------

const rootReducer = combineReducers({
    user,
    watchlists,
})

export default rootReducer;