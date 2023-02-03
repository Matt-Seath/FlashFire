import * as React from "react";
import Container from "@mui/material/Container";
import { Box } from "@mui/material";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { TableVirtuoso, TableComponents } from "react-virtuoso";

function Watchlists({ posts }: { posts: any }) {
  interface Data {
    id: number;
    open: number;
    close: number;
    date: string;
    high: number;
    low: number;
    volume: number;
  }

  interface ColumnData {
    dataKey: keyof Data;
    label: string;
    numeric?: boolean;
    width: number;
  }

  type Sample = [string, number, number, number, number, number];

  const sample: readonly Sample[] = posts[0].history;

  function createData(
    id: number,
    date: string,
    open: number,
    close: number,
    high: number,
    low: number,
    volume: number
  ): Data {
    return { id, date, open, close, high, low, volume };
  }

  const columns: ColumnData[] = [
    {
      width: 200,
      label: "Date",
      dataKey: "date",
    },
    {
      width: 120,
      label: "Open\u00A0(AUD)",
      dataKey: "open",
      numeric: true,
    },
    {
      width: 120,
      label: "Close\u00A0(AUD)",
      dataKey: "close",
      numeric: true,
    },
    {
      width: 120,
      label: "High\u00A0(AUD)",
      dataKey: "high",
      numeric: true,
    },
    {
      width: 120,
      label: "Low\u00A0(AUD)",
      dataKey: "low",
      numeric: true,
    },
    {
      width: 200,
      label: "Volume",
      dataKey: "volume",
    },
  ];

  const rows: Data[] = Array.from({ length: 200 }, (_, index) => {
    const randomSelection = sample[Math.floor(Math.random() * sample.length)];
    return createData(index, ...randomSelection);
  });

  const VirtuosoTableComponents: TableComponents<Data> = {
    Scroller: React.forwardRef<HTMLDivElement>((props, ref) => (
      <TableContainer component={Paper} {...props} ref={ref} />
    )),
    Table: (props) => (
      <Table {...props} style={{ borderCollapse: "separate" }} />
    ),
    TableHead,
    TableRow: ({ item: _item, ...props }) => <TableRow {...props} />,
    TableBody: React.forwardRef<HTMLTableSectionElement>((props, ref) => (
      <TableBody {...props} ref={ref} />
    )),
  };

  function fixedHeaderContent() {
    return (
      <TableRow>
        {columns.map((column) => (
          <TableCell
            key={column.dataKey}
            variant="head"
            align={column.numeric || false ? "right" : "left"}
            style={{ width: column.width }}
            sx={{
              backgroundColor: "background.paper",
            }}
          >
            {column.label}
          </TableCell>
        ))}
      </TableRow>
    );
  }

  function rowContent(_index: number, row: Data) {
    return (
      <React.Fragment>
        {columns.map((column) => (
          <TableCell
            key={column.dataKey}
            align={column.numeric || false ? "right" : "left"}
          >
            {row[column.dataKey]}
          </TableCell>
        ))}
      </React.Fragment>
    );
  }

  const rounded = (num: any) => (Math.round(num * 100) / 100).toFixed(2);

  return (
    <Container>
      <Paper style={{ height: 400, width: "100%" }}>
        <TableVirtuoso
          data={rows}
          components={VirtuosoTableComponents}
          fixedHeaderContent={fixedHeaderContent}
          itemContent={rowContent}
        />
      </Paper>

      <div>
        {posts.map((post: any) => (
          <div>
            <p>{post.symbol}</p>
            <p>{post.long_name}</p>
            <p>{post.sector}</p>
            <Box sx={{ display: "flex" }}>
              <p>Date: {post.history[0][0]}</p>
              {/* <p>Open: {rounded(hist[1])}</p>
              <p>Close: {rounded(hist[2])}</p>
              <p>High: {rounded(hist[3])}</p>
              <p>Low: {rounded(hist[4])}</p>
              <p>Volume: {rounded(hist[5])}</p> */}
            </Box>
          </div>
        ))}
      </div>
    </Container>
  );
}

export async function getStaticProps() {
  const res = await fetch("http://127.0.0.1:8000/api/");
  const posts = await res.json();
  console.log(posts);

  return {
    props: {
      posts,
    },
  };
}

export default Watchlists;
