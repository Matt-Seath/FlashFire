import * as React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { Watchlist } from "redux/slices/user";

interface Data {
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
  symbol: string,
  high: number,
  low: number,
  open: number,
  change: string
): Data {
  return {
    symbol,
    high,
    low,
    open,
    change,
  };
}

export default function BasicTable({ watchlists, currentWatchlist }: Props) {
  const watchlistRows: Data[] = watchlists[currentWatchlist].items.map((item) =>
    createData(item, 22, currentWatchlist, 44, "5%")
  );
  const [rows, updateRows] = React.useState<Data[]>(watchlistRows);

  React.useEffect(() => {
    updateRows([...watchlistRows]);
  }, [currentWatchlist]);

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
          {rows.map((row) => (
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
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
