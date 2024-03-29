import React from "react";
import { ChartType, ColorTheme, CopyrightStyles, DateFormat, Locales, ScaleMode, ScalePosition } from "../index";
export type SymbolOverviewProps = {
    symbols?: string[][];
    chartOnly?: boolean;
    width?: string | number;
    height?: string | number;
    locale?: Locales;
    colorTheme?: ColorTheme;
    isTransparent?: boolean;
    showFloatingTooltip?: boolean;
    scalePosition?: ScalePosition;
    scaleMode?: ScaleMode;
    fontFamily?: "Trebuchet MS, sans-serif" | "Arial, sans-serif" | "Times, Times New Roman, serif" | "Andale Mono, monospace" | "Courier New, monospace" | "Comic Sans MS, Comic Sans, cursive" | "Trattatello, fantasy";
    fontSize?: "10" | "11" | "12" | "13" | "14" | "16" | "18" | "20" | "22" | "24" | "28";
    fontColor?: string;
    noTimeScale?: boolean;
    hideDateRanges?: boolean;
    hideMarketStatus?: boolean;
    valuesTracking?: "0" | "1" | "2" | "3";
    lineWidth?: 1 | 2 | 3 | 4;
    showVolume?: boolean;
    volumeUpColor?: string;
    volumeDownColor?: string;
    dateFormat: DateFormat;
    timeHoursFormat?: "12-hours" | "24-hours";
    chartType?: ChartType;
    lineColor?: string;
    bottomColor?: string;
    topColor?: string;
    upColor?: string;
    downColor?: string;
    borderUpColor?: string;
    borderDownColor?: string;
    wickUpColor?: string;
    wickDownColor?: string;
    backGroundColor?: string;
    gridLineColor?: string;
    widgetFontColor?: string;
    autosize?: boolean;
    container_id?: string;
    children?: never;
    copyrightStyles?: CopyrightStyles;
};
declare const SymbolOverview: React.FC<SymbolOverviewProps>;
export default SymbolOverview;
