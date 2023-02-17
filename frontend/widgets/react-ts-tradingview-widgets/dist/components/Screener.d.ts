import React from "react";
import { ColorTheme, CopyrightStyles, Locales } from "../index";
type DefaultColumnForexOrCrypto = "overview" | "performance" | "oscillators" | "moving_averages";
type DefaultColumnCountries = "overview" | "performance" | "valuation" | "dividends" | "margins" | "income_statement" | "balance_sheet" | "oscillators" | "moving_averages";
type DefaultScreenForexOrCrypto = "general" | "top_gainers" | "top_losers" | "ath" | "atl" | "above_52wk_high" | "below_52wk_low" | "monthly_high" | "monthly_low" | "most_volatile" | "overbought" | "oversold" | "outperforming_SMA50" | "underperforming_SMA50";
type DefaultScreenCountries = "most_capitalized" | "volume_leaders" | "top_gainers" | "top_losers" | "ath" | "atl" | "high_dividend" | "above_52wk_high" | "below_52wk_low" | "monthly_high" | "monthly_low" | "most_volatile" | "unusual_volume" | "overbought" | "oversold" | "outperforming_SMA50" | "underperforming_SMA50" | "earnings_this_week";
type MarketCountries = "america" | "australia" | "canada" | "egypt" | "germany" | "india" | "israel" | "italy" | "luxembourg" | "philippines" | "poland" | "korea" | "sweden" | "taiwan" | "turkey" | "uk" | "vietnam";
type MarketForexOrCrypto = "forex" | "crypto";
type ConditionalScreenerProps = {
    market?: MarketForexOrCrypto;
    defaultColumn?: DefaultColumnForexOrCrypto;
    defaultScreen?: DefaultScreenForexOrCrypto;
} | {
    market?: MarketCountries;
    defaultColumn?: DefaultColumnCountries;
    defaultScreen?: DefaultScreenCountries;
};
export type ScreenerProps = {
    width?: string | number;
    height?: string | number;
    autosize?: boolean;
    showToolbar?: boolean;
    colorTheme?: ColorTheme;
    locale?: Locales;
    isTransparent?: boolean;
    largeChartUrl?: string;
    children?: never;
    copyrightStyles?: CopyrightStyles;
} & ConditionalScreenerProps;
declare const Screener: React.FC<ScreenerProps>;
export default Screener;
