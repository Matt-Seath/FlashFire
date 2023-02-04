import * as React from "react";
import FFDrawer from "./drawer";
import FFAppBar from "./appbar";

export default function FFNavigation() {
  const [open, setOpen] = React.useState(true);

  return (
    <div>
      <FFAppBar open={open} setOpen={setOpen} />
      <FFDrawer open={open} />
    </div>
  );
}
