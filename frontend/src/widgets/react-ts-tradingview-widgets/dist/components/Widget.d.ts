import React from "react";
interface WidgetProps {
    scriptHTML: any;
    scriptSRC: string;
    containerId?: string;
    type?: "Widget" | "MediumWidget";
}
declare const Widget: React.FC<WidgetProps>;
export default Widget;
