import React from "react";
import { ColorTheme, DateRange, CopyrightStyles, Locales } from "../index";
export type MarketOverviewSymbol = {
    s: string;
    d?: string;
};
export type MarketOverviewTab = {
    title: string;
    symbols: MarketOverviewSymbol[];
    originalTitle: string;
};
export type MarketOverviewProps = {
    colorTheme?: ColorTheme;
    dateRange?: DateRange;
    showChart?: boolean;
    locale?: Locales;
    largeChartUrl?: string;
    isTransparent?: boolean;
    showSymbolLogo?: boolean;
    showFloatingTooltip?: boolean;
    width?: string | number;
    height?: string | number;
    autosize?: boolean;
    plotLineColorGrowing?: string;
    plotLineColorFalling?: string;
    gridLineColor?: string;
    scaleFontColor?: string;
    belowLineFillColorGrowing?: string;
    belowLineFillColorFalling?: string;
    belowLineFillColorGrowingBottom?: string;
    belowLineFillColorFallingBottom?: string;
    symbolActiveColor?: string;
    tabs?: MarketOverviewTab[];
    children?: never;
    copyrightStyles?: CopyrightStyles;
};
declare const MarketOverview: React.FC<MarketOverviewProps>;
export default MarketOverview;
