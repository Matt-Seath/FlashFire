import * as React from "react";
import Button from "@mui/material/Button";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { Watchlist, WatchlistItem } from "redux/slices/types";
import { Box } from "@mui/material";
import { axiosNext } from "utils/axios";
import { useTypeDispatch } from "redux/store";
import { setWatchlists } from "redux/slices/watchlists";
import SearchBar from "components/Navigation/SearchBar";
import {
  MarketOverview,
  MarketData,
  MarketDataSymbol,
  MarketDataSymbolsGroup,
} from "widgets/react-ts-tradingview-widgets/dist";

interface Props {
  watchlists: Watchlist[];
  currentWatchlist: number;
}

export default function BasicTable({ watchlists, currentWatchlist }: Props) {
  const watchlistItems: MarketDataSymbol[] = watchlists[
    currentWatchlist
  ].items.map((item) => ({
    name: "ASX:" + item.stock.symbol.split(".")[0],
    displayName:
      typeof item.stock.long_name === "string"
        ? item.stock.symbol.split(".")[0] + " | " + item.stock.long_name
        : item.stock.symbol.split(".")[0],
  }));
  console.log(watchlists);
  const watchlistData: MarketDataSymbolsGroup[] = [
    {
      name: watchlists[currentWatchlist].name,
      originalName: watchlists[currentWatchlist].name,
      symbols: watchlistItems,
    },
  ];

  const [rows, updateRows] =
    React.useState<MarketDataSymbolsGroup[]>(watchlistData);
  const dispatch = useTypeDispatch();

  React.useEffect(() => {
    updateRows([...watchlistData]);
  }, [currentWatchlist, watchlists]);

  const removeWatchlistItem = ({
    watchlistId,
    itemId,
  }: {
    watchlistId: string;
    itemId: number;
  }) => {
    const updatedWatchlists = watchlists.map((watchlist) => {
      if (watchlist.id === watchlistId) {
        return {
          ...watchlist,
          items: watchlist.items.filter((item) => item.id !== itemId),
        };
      }
      return watchlist;
    });
    dispatch(setWatchlists(updatedWatchlists));
  };

  const addWatchlistItem = (
    watchlistId: string,
    stock: string,
    itemId: number
  ) => {
    const newItem: WatchlistItem = {
      id: itemId,
      stock: {
        symbol: stock + ".AX",
      },
    };

    const updatedWatchlists = watchlists.map((watchlist) => {
      if (watchlist.id === watchlistId) {
        return {
          ...watchlist,
          items: [...watchlist.items, newItem],
        };
      }
      return watchlist;
    });
    dispatch(setWatchlists(updatedWatchlists));
  };

  const handleDeleteItem = async (stock: number) => {
    const watchlistId = watchlists[currentWatchlist].id;
    try {
      await axiosNext.delete("api/watchlist/removeItem", {
        params: {
          watchlist_id: watchlistId,
          item_id: stock,
        },
      });
      removeWatchlistItem({ watchlistId, itemId: stock });
    } catch {
      console.log("Failed to delete:" + stock);
    }
  };

  const handleAddItem = async (stock: string) => {
    const watchlistId = watchlists[currentWatchlist].id;
    try {
      const response = await axiosNext.post(`api/watchlist/addItem`, {
        watchlist_id: watchlistId,
        stock: stock + ".AX",
      });
      addWatchlistItem(watchlistId, stock, response.data);
    } catch {
      console.log("Failed to add:" + stock);
    }
  };

  return (
    <Box width={"100%"} height={590} display={"flex"}>
      <Box width={"70%"}>
        <MarketData
          height={534}
          width={"100%"}
          colorTheme="dark"
          symbolsGroups={rows}
          copyrightStyles={undefined}
        />
        <Box width={"100%"} height={56}>
          <SearchBar
            placeHolder="Add stock to Watchlist"
            onSubmit={handleAddItem}
          />
        </Box>
      </Box>
      <Box width={"30%"}>
        <MarketOverview colorTheme="dark" height={590} width={"100%"} />
        <Box display={"flex"} width={"100%"} bgcolor={"#020409"} justifyContent={"right"}>
          <Button sx={{ color: "#3399ff", width: "50%" }}>
            Rename watchlist
          </Button>
          <Button sx={{ color: "#aa6699", width: "50%" }}>
            Delete watchlist
          </Button>
        </Box>
      </Box>
    </Box>
  );
}
