export type StatusRequest = 'idle' | 'pending' | 'succeeded' | 'failed';

export type ErrorRequest = null | string | undefined;

// ----------------------------------------------------------------------

export type Request = {
    status: StatusRequest;
    error: ErrorRequest;
}

type Stock = {
    id: number;
    symbol: string;
    sector: string;
    longName: string;
}

type WatchlistItem = {
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
    watchlists: Watchlist; 
}