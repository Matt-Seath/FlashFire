import * as React from "react";
import Container from "@mui/material/Container";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import TVStockMarket from "@/components/TradingView/StockMarket";
import TVScreener from "@/components/TradingView/Screener";
import AccountSummary from "@/components/Account/AccountSummary";

const rounded = (num: any) => (Math.round(num * 100) / 100).toFixed(2);

function Home({ posts }: { posts: any }) {
  return (
    <React.Fragment>
      <Box
        sx={{
          display: "flex",
          height: 510,
        }}
      >
        <ul>
          <li>Account No: {posts[0].id}</li>
          <li>Account Type: {posts[0].account_type}</li>
          <li>Accrued Cash: {posts[0].accrued_cash}</li>
          <li>Available Funds: {posts[0].available_funds}</li>
          <li>Buying Power: {posts[0].buying_power}</li>
          <li>Excess Liquidity: {posts[0].excess_liquidity}</li>
          <li>Full Available Funds: {posts[0].full_available_funds}</li>
          <li>Full Excess Liquidity: {posts[0].full_excess_liquidity}</li>
          <li>Gross Position Value: {posts[0].gross_position_value}</li>
          <li>Net Liquidation : {posts[0].net_liquidation}</li>
          <li>Total Cash Value: {posts[0].total_cash_value}</li>
          <li>Last Updated: {posts[0].last_updated}</li>
        </ul>
        {/* <AccountSummary /> */}
      </Box>
      <Box
        sx={{
          display: "flex",
          height: 510,
        }}
      >
        <TVStockMarket />
        <TVScreener />
      </Box>
    </React.Fragment>
  );
}

export async function getStaticProps() {
  const res = await fetch("http://127.0.0.1:8000/api/account");
  const posts = await res.json();
  return {
    props: {
      posts,
    },
    // Next.js will attempt to re-generate the page:
    // - When a request comes in
    // - At most once every 10 seconds
    revalidate: 10, // In seconds
  };
}

export default Home;
