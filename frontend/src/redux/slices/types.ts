export type StatusRequest = 'idle' | 'pending' | 'succeeded' | 'failed';

export type ErrorRequest = null | string | undefined;

// ----------------------------------------------------------------------

export type Request = {
    status: StatusRequest;
    error: ErrorRequest;
}

type Stock = {
    symbol: string;
    sector?: string;
    long_name?: string;
}

export type WatchlistItem = {
    id: number;
    stock: Stock;
}

export type Watchlist = {
    id: string;
    user: number;
    name: string;
    items: WatchlistItem[];
}

export type User = {
    email: string;
    watchlists: Watchlist[]; 
}