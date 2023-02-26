import React from "react";
import { ColorTheme, CopyrightStyles, Locales } from "../index";
export type CompanyProfileProps = {
    symbol?: string;
    width?: string | number;
    height?: string | number;
    autosize?: boolean;
    colorTheme?: ColorTheme;
    isTransparent?: boolean;
    locale?: Locales;
    largeChartUrl?: string;
    children?: never;
    copyrightStyles?: CopyrightStyles;
};
declare const CompanyProfile: React.FC<CompanyProfileProps>;
export default CompanyProfile;
