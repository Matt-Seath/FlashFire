import React from "react";
import { ColorTheme, CopyrightStyles, Locales } from "../index";
export type SingleTickerProps = {
    symbol?: string;
    width?: string | number;
    autosize?: boolean;
    colorTheme?: ColorTheme;
    isTransparent?: boolean;
    locale?: Locales;
    largeChartUrl?: string;
    children?: never;
    copyrightStyles?: CopyrightStyles;
};
declare const SingleTicker: React.FC<SingleTickerProps>;
export default SingleTicker;
