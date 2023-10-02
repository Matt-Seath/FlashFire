import React from "react";
import { ColorTheme, CopyrightStyles, Locales } from "../index";

export interface MarketDataSymbol {
    name: string;
    displayName?: string;
}
export interface MarketDataSymbolsGroup {
    name: string;
    originalName: string;
    symbols: MarketDataSymbol[];
}
export interface MarketDataProps {
    width?: number | string;
    height?: number | string;
    autosize?: boolean;
    symbolsGroups?: MarketDataSymbolsGroup[];
    showSymbolLogo?: boolean;
    colorTheme?: ColorTheme;
    isTransparent?: boolean;
    locale?: Locales;
    largeChartUrl?: string;
    children?: never;
    copyrightStyles?: CopyrightStyles;
}
declare const MarketData: React.FC<MarketDataProps>;
export default MarketData;
