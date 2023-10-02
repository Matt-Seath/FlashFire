import * as React from "react";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import Layout from "layouts/Layout";
import EnhancedTable from "components/Tables/WatchlistTable";
import WatchlistTabs from "components/Tabs/WatchlistTabs";
import { Watchlist } from "redux/slices/types";
import { useTypedSelector } from "redux/store";
import { Button } from "@mui/material";

Watchlists.getLayout = function getLayout(page: any) {
  return <Layout>{page}</Layout>;
};

export default function Watchlists() {
  const watchlists: Watchlist[] = useTypedSelector(
    (state) => state.watchlists.watchlists
  );
  const watchlistNames: string[] = watchlists.map(
    (watchlist: Watchlist) => watchlist.name
  );

  const [currentWatchlist, setCurrentWatchlist] = React.useState<number>(0);

  return (
    <Container maxWidth="lg">
      <Box
        sx={{
          my: 4,
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Typography variant="h4" component="h1" gutterBottom>
          Watchlists
        </Typography>

        <WatchlistTabs
          selected={currentWatchlist}
          onSelect={setCurrentWatchlist}
          watchlists={watchlistNames}
        />
        <EnhancedTable
          currentWatchlist={currentWatchlist}
          watchlists={watchlists}
        />
      </Box>
      <Box sx={{display:"flex", justifyContent:"right"}}>
        <Button sx={{display:"flex-end", color: "#3399ff"}}>
          Rename watchlist
        </Button>
        <Button sx={{display:"flex-end", color: "#776699"}}>
          Delete watchlist
        </Button>
      </Box>
    </Container>
  );
}
