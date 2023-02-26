import Box from "@mui/material/Box";
import { CssBaseline } from "@mui/material";
import { FC, ReactNode } from "react";
import FFNavigation from "../components/Navigation/Navigation";
import { DrawerHeader } from "../components/Navigation/Drawer";

// ----------------------------------------------------------------------

interface LayoutProps {
  children: ReactNode;
}

// ----------------------------------------------------------------------

const Layout: FC<LayoutProps> = ({ children }) => {
  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      <FFNavigation />
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <DrawerHeader />
        {children}
      </Box>
    </Box>
  );
};

export default Layout;
