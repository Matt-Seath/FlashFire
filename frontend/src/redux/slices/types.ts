export type StatusRequest = 'idle' | 'pending' | 'succeeded' | 'failed';

export type ErrorRequest = null | string | undefined;

// ----------------------------------------------------------------------

export type Request = {
    status: StatusRequest;
    error: ErrorRequest;
}

type Stock = {
    symbol: string;
    sector: string;
    longName: string;
}

type WatchlistItem = {
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
    watchlists: Watchlist; 
}