import React from "react";
import { ColorTheme, CopyrightStyles, Locales } from "../index";
export type TechnicalAnalysisProps = {
    interval?: "1m" | "5m" | "15m" | "30m" | "1h" | "2h" | "4h" | "1D" | "1W" | "1M";
    width?: number | string;
    height?: number | string;
    autosize?: boolean;
    isTransparent?: boolean;
    symbol?: string;
    showIntervalTabs?: boolean;
    locale?: Locales;
    colorTheme?: ColorTheme;
    largeChartUrl?: string;
    children?: never;
    copyrightStyles?: CopyrightStyles;
};
declare const TechnicalAnalysis: React.FC<TechnicalAnalysisProps>;
export default TechnicalAnalysis;
