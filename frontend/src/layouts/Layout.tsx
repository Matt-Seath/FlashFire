import Box from "@mui/material/Box";
import { CssBaseline } from "@mui/material";
import { FC, ReactNode } from "react";
import FFNavigation from "../components/Navigation/Navigation";
import { DrawerHeader } from "../components/Navigation/Drawer";
import Footer from "components/Footer/Footer";

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
      <Box component="main" sx={{ flexGrow: 1, p: 0.5 }}>
        <DrawerHeader />
        {children}
      </Box>
      <Footer />
    </Box>
  );
};

export default Layout;
