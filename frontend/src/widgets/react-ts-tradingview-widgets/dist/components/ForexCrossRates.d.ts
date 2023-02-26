import React from "react";
import { ColorTheme, Currencies, CopyrightStyles, Locales } from "../index";
export type ForexCrossRatesProps = {
    width?: number | string;
    height?: number | string;
    autosize?: boolean;
    currencies?: Currencies[];
    isTransparent?: boolean;
    colorTheme?: ColorTheme;
    locale?: Locales;
    largeChartUrl?: string;
    children?: never;
    copyrightStyles?: CopyrightStyles;
};
declare const ForexCrossRates: React.FC<ForexCrossRatesProps>;
export default ForexCrossRates;
