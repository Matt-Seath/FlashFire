import * as React from "react";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Box from "@mui/material/Box";

interface Props {
  watchlists: string[];
  selected: number;
  onSelect: (list: number) => void;
}

export default function WatchlistTabs({
  watchlists,
  onSelect,
  selected,
}: Props) {
  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    onSelect(newValue);
  };
  return (
    <Box sx={{ maxWidth: { xs: 320, sm: 480 }, bgcolor: "background.paper" }}>
      <Tabs
        value={selected}
        onChange={handleChange}
        variant="scrollable"
        scrollButtons="auto"
        aria-label="scrollable auto tabs example"
      >
        {watchlists.map((item, index) => (
          <Tab key={index} label={item} />
        ))}
      </Tabs>
    </Box>
  );
}
