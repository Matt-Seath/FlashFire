import { Ticker, CopyrightStyles } from "react-ts-tradingview-widgets";

export const Example = () => {
  const styles: CopyrightStyles = {
    parent: {
      fontSize: "24px",
      color: "red",
    },
    link: {
      textDecoration: "line-trough",
    },
    span: {
      color: "darkblue",
    },
  };
  return <Ticker colorTheme="dark" copyrightStyles={styles} />;
};
