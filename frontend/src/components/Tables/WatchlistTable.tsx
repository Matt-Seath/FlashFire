import * as React from "react";
import Button from "@mui/material/Button";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { Watchlist } from "redux/slices/types";
import { Box } from "@mui/material";
import { axiosNext } from "utils/axios";

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
      item.id,
      currentWatchlist,
      44,
      "5%"
    )
  );
  const [rows, updateRows] = React.useState<Data[]>(watchlistRows);

  React.useEffect(() => {
    updateRows([...watchlistRows]);
  }, [currentWatchlist]);

  const handleDeleteItem = async (stock: number) => {
    try {
      const response = await axiosNext.delete("api/watchlist/removeItem", {
        params: {
          watchlist_id: watchlists[currentWatchlist].id,
          item_id: stock,
        },
      });
      updateRows((rows) => rows.filter((row) => row.id !== stock));
    } catch {
      console.log("nope");
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
      <Box width={"100%"} height={50} bgcolor={"green"} />
    </TableContainer>
  );
}
