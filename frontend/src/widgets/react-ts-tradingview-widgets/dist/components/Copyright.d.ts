import React from "react";
import { CopyrightStyles } from "..";
export type CopyrightProps = {
    copyrightStyles?: CopyrightStyles;
    href?: string;
    spanText?: string;
    text?: string;
    children?: never;
};
declare const Copyright: React.FC<CopyrightProps>;
export default Copyright;
