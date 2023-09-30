import * as React from "react";
import Button from "@mui/material/Button";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { Watchlist } from "redux/slices/user";
import { Box } from "@mui/material";

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
    createData(item.stock.symbol.split(".")[0], 22, currentWatchlist, 44, "5%")
  );
  const [rows, updateRows] = React.useState<Data[]>(watchlistRows);

  React.useEffect(() => {
    updateRows([...watchlistRows]);
  }, [currentWatchlist]);

  const handleClick = (stock: string) => {
    console.log(stock);
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
                    onClick={() => handleClick(row.symbol)}
                    sx={{
                      color: "white",
                      background: "red",
                      minWidth: 10,
                      height: 20,
                      width: 20,
                      paddingTop: 1.2,
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
