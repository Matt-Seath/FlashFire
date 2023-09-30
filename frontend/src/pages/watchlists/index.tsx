import * as React from "react";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import Layout from "layouts/Layout";
import EnhancedTable from "components/Tables/WatchlistTable";
import WatchlistTabs from "components/Tabs/WatchlistTabs";
import { getWatchlists } from "utils/utils";
import { Watchlist } from "redux/slices/types";

Watchlists.getLayout = function getLayout(page: any) {
  return <Layout>{page}</Layout>;
};

export default function Watchlists() {
  const { watchlists }: { watchlists: Watchlist[] } = getWatchlists();

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
    </Container>
  );
}
