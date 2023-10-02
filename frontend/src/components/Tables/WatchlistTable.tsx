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

interface Data {
  id: number;
  symbol: string;
  high: number;
  low: number;
  open: number;
  change: string;
}

interface Props {
  watchlists: Watchlist[];
  currentWatchlist: number;
}

function createData(
  id: number,
  symbol: string,
  high: number,
  low: number,
  open: number,
  change: string
): Data {
  return {
    id,
    symbol,
    high,
    low,
    open,
    change,
  };
}

export default function BasicTable({ watchlists, currentWatchlist }: Props) {
  const watchlistRows: Data[] = watchlists[currentWatchlist].items.map((item) =>
    createData(
      item.id,
      item.stock.symbol.split(".")[0],
      45,
      currentWatchlist,
      44,
      "5%"
    )
  );
  const [rows, updateRows] = React.useState<Data[]>(watchlistRows);
  const dispatch = useTypeDispatch();

  React.useEffect(() => {
    updateRows([...watchlistRows]);
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

  const addWatchlistItem = (watchlistId: string, stock: string) => {
    const newItem: WatchlistItem = {
      id: 122,
      stock: {
        symbol: stock + ".AX",
      },
    };
    console.log(newItem);

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
      await axiosNext.post(`api/watchlist/addItem`, {
        watchlist_id: watchlistId,
        stock: stock + ".AX",
      });
      addWatchlistItem(watchlistId, stock);
    } catch {
      console.log("Failed to add:" + stock);
    }
  };

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>SYMBOL</TableCell>
            <TableCell align="right">CHANGE (%)</TableCell>
            <TableCell align="right">PRICE</TableCell>
            <TableCell align="right">HIGH</TableCell>
            <TableCell align="right">LOW</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row, index) => (
            <TableRow
              key={row.symbol}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.symbol}
              </TableCell>
              <TableCell align="right">{row.open}</TableCell>
              <TableCell align="right">{row.high}</TableCell>
              <TableCell align="right">{row.low}</TableCell>
              <TableCell align="right">{row.change}</TableCell>
              <TableCell align="right">
                <Box display={"flex"} justifyContent={"flex-end"}>
                  <Button
                    id={String(index)}
                    onClick={() => handleDeleteItem(row.id)}
                    sx={{
                      color: "white",
                      background: "red",
                      minWidth: 10,
                      height: 20,
                      width: 20,
                      paddingTop: 1,
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    ✖
                  </Button>
                </Box>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <Box width={"100%"} height={56} bgcolor={"#433255"}>
        <SearchBar
          placeHolder="Add stock to Watchlist"
          onSubmit={handleAddItem}
        />
      </Box>
    </TableContainer>
  );
}
