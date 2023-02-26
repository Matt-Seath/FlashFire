import * as React from "react";
import FFDrawer from "./Drawer";
import FFAppBar from "./AppBar";


export default function Navigation() {
  const [open, setOpen] = React.useState(true);

  return (
    <div>
      <FFAppBar open={open} setOpen={setOpen} />
      <FFDrawer open={open} />
    </div>
  );
}
