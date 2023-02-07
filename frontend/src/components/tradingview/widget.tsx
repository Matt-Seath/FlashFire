import dynamic from "next/dynamic";

const SymbolOverviewNoSSR = dynamic(
  () => import("react-ts-tradingview-widgets").then((w) => w.SymbolOverview),
  {
    ssr: false,
  }
);
