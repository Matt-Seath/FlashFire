import React from "react";
import { ColorTheme, CopyrightStyles, Locales } from "../index";
export type CryptoCurrencyMarketProps = {
    width?: string | number;
    height?: string | number;
    autosize?: boolean;
    defaultColumn?: "overview" | "performance" | "oscillators" | "moving_averages";
    screener_type?: "crypto_mkt";
    displayCurrency?: "USD" | "BTC";
    colorTheme?: ColorTheme;
    locale?: Locales;
    isTransparent?: boolean;
    children?: never;
    copyrightStyles?: CopyrightStyles;
};
declare const CryptoCurrencyMarket: React.FC<CryptoCurrencyMarketProps>;
export default CryptoCurrencyMarket;
