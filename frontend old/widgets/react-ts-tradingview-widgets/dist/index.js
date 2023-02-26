

function ___$insertStyle(css) {
    if (!css || typeof window === 'undefined') {
        return;
    }
    const style = document.createElement('style');
    style.setAttribute('type', 'text/css');
    style.innerHTML = css;
    document.head.appendChild(style);
    return css;
}

Object.defineProperty(exports, '__esModule', { value: true });

var React = require('react');

function _interopDefaultLegacy (e) { return e && typeof e === 'object' && 'default' in e ? e : { 'default': e }; }

var React__default = /*#__PURE__*/_interopDefaultLegacy(React);

/*! *****************************************************************************
Copyright (c) Microsoft Corporation.

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
***************************************************************************** */

var __assign = function() {
    __assign = Object.assign || function __assign(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p)) t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};

function __rest(s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
}

var createId = function (length) {
    var result = "";
    var characters = "abcdef0123456789";
    var charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
};

var Copyright = function (_a) {
    var href = _a.href, spanText = _a.spanText, _b = _a.text, text = _b === void 0 ? "By TradingView" : _b, copyrightStyles = _a.copyrightStyles;
    var defaultStyles = {
        parent: {
            fontSize: "13px",
            lineHeight: "32px",
            textAlign: "center",
            verticalAlign: "center",
            fontFamily: "Trebuchet MS, Arial, sans-serif",
            color: "#9db2bd",
        },
        link: {
            textDecoration: "none",
            color: "#9db2bd",
        },
        span: {
            color: "#2962FF",
        },
    };
    return null 
};

var Widget = function (_a) {
    var scriptHTML = _a.scriptHTML, scriptSRC = _a.scriptSRC, containerId = _a.containerId, type = _a.type;
    var ref = React.createRef();
    React.useEffect(function () {
        var refValue;
        if (ref.current) {
            var script_1 = document.createElement("script");
            script_1.setAttribute("data-nscript", "afterInteractive");
            script_1.src = scriptSRC;
            script_1.async = true;
            script_1.type = "text/javascript";
            if (type === "Widget" || type === "MediumWidget") {
                script_1.onload = function () {
                    if (typeof TradingView !== undefined) {
                        script_1.innerHTML = JSON.stringify(type === "Widget"
                            ? new TradingView.widget(scriptHTML)
                            : type === "MediumWidget"
                                ? new TradingView.MediumWidget(scriptHTML)
                                : undefined);
                    }
                };
            }
            else {
                script_1.innerHTML = JSON.stringify(scriptHTML);
            }
            ref.current.appendChild(script_1);
            refValue = ref.current;
        }
        return function () {
            if (refValue) {
                while (refValue.firstChild) {
                    refValue.removeChild(refValue.firstChild);
                }
            }
        };
    }, [ref, scriptHTML, type, scriptSRC]);
    return React__default["default"].createElement("div", { ref: ref, id: containerId });
};

var AdvancedRealTimeChart = function (_a) {
    var _b = _a.width, width = _b === void 0 ? 980 : _b, _c = _a.height, height = _c === void 0 ? 610 : _c, _d = _a.autosize, autosize = _d === void 0 ? false : _d, _e = _a.symbol, symbol = _e === void 0 ? "NASDAQ:AAPL" : _e, _f = _a.interval, interval = _f === void 0 ? "1" : _f, _g = _a.range, range = _g === void 0 ? undefined : _g, _h = _a.timezone, timezone = _h === void 0 ? "UTC" : _h, _j = _a.theme, theme = _j === void 0 ? "light" : _j, _k = _a.style, style = _k === void 0 ? "1" : _k, _l = _a.locale, locale = _l === void 0 ? "en" : _l, _m = _a.toolbar_bg, toolbar_bg = _m === void 0 ? "#f1f3f6" : _m, _o = _a.enable_publishing, enable_publishing = _o === void 0 ? false : _o, _p = _a.hide_top_toolbar, hide_top_toolbar = _p === void 0 ? false : _p, _q = _a.hide_legend, hide_legend = _q === void 0 ? false : _q, _r = _a.withdateranges, withdateranges = _r === void 0 ? true : _r, _s = _a.hide_side_toolbar, hide_side_toolbar = _s === void 0 ? false : _s, _t = _a.allow_symbol_change, allow_symbol_change = _t === void 0 ? true : _t, _u = _a.save_image, save_image = _u === void 0 ? true : _u, _v = _a.details, details = _v === void 0 ? false : _v, _w = _a.hotlist, hotlist = _w === void 0 ? false : _w, _x = _a.calendar, calendar = _x === void 0 ? false : _x, _y = _a.show_popup_button, show_popup_button = _y === void 0 ? false : _y, _z = _a.popup_width, popup_width = _z === void 0 ? "600" : _z, _0 = _a.popup_height, popup_height = _0 === void 0 ? "400" : _0, _1 = _a.watchlist, watchlist = _1 === void 0 ? undefined : _1, _2 = _a.studies, studies = _2 === void 0 ? undefined : _2, _3 = _a.disabled_features, disabled_features = _3 === void 0 ? undefined : _3, _4 = _a.enabled_features, enabled_features = _4 === void 0 ? undefined : _4, _5 = _a.container_id, container_id = _5 === void 0 ? "tradingview_".concat(createId(5)) : _5, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["width", "height", "autosize", "symbol", "interval", "range", "timezone", "theme", "style", "locale", "toolbar_bg", "enable_publishing", "hide_top_toolbar", "hide_legend", "withdateranges", "hide_side_toolbar", "allow_symbol_change", "save_image", "details", "hotlist", "calendar", "show_popup_button", "popup_width", "popup_height", "watchlist", "studies", "disabled_features", "enabled_features", "container_id", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign(__assign(__assign(__assign(__assign(__assign({}, (!autosize ? { width: width } : { width: "100%" })), (!autosize ? { height: height } : { height: "100%" })), { autosize: autosize, symbol: symbol }), (!range ? { interval: interval } : { range: range })), { timezone: timezone, theme: theme, style: style, locale: locale, toolbar_bg: toolbar_bg, enable_publishing: enable_publishing, hide_top_toolbar: hide_top_toolbar, hide_legend: hide_legend, withdateranges: withdateranges, hide_side_toolbar: hide_side_toolbar, allow_symbol_change: allow_symbol_change, save_image: save_image, details: details, hotlist: hotlist, calendar: calendar }), (show_popup_button && {
                show_popup_button: show_popup_button,
                popup_width: popup_width,
                popup_height: popup_height,
            })), { watchlist: watchlist, studies: studies, disabled_features: disabled_features, enabled_features: enabled_features, container_id: container_id }), props), scriptSRC: "https://s3.tradingview.com/tv.js", containerId: container_id, type: "Widget" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/symbols/".concat(symbol), spanText: "".concat(symbol, " Chart") })));
};

var CompanyProfile = function (_a) {
    var _b = _a.symbol, symbol = _b === void 0 ? "NASDAQ:AAPL" : _b, _c = _a.width, width = _c === void 0 ? 480 : _c, _d = _a.height, height = _d === void 0 ? 650 : _d, _e = _a.autosize, autosize = _e === void 0 ? false : _e, _f = _a.colorTheme, colorTheme = _f === void 0 ? "light" : _f, _g = _a.isTransparent, isTransparent = _g === void 0 ? false : _g, _h = _a.locale, locale = _h === void 0 ? "en" : _h, _j = _a.largeChartUrl, largeChartUrl = _j === void 0 ? undefined : _j, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["symbol", "width", "height", "autosize", "colorTheme", "isTransparent", "locale", "largeChartUrl", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign(__assign({}, (!autosize ? { width: width } : { width: "100%" })), (!autosize ? { height: height } : { height: "100%" })), { symbol: symbol, colorTheme: colorTheme, isTransparent: isTransparent, locale: locale, largeChartUrl: largeChartUrl }), props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-symbol-profile.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/symbols/".concat(symbol, "/"), spanText: "".concat(symbol, " Profile") })));
};

var CryptoCurrencyMarket = function (_a) {
    var _b = _a.width, width = _b === void 0 ? 1000 : _b, _c = _a.height, height = _c === void 0 ? 490 : _c, _d = _a.autosize, autosize = _d === void 0 ? false : _d, _e = _a.defaultColumn, defaultColumn = _e === void 0 ? "overview" : _e, _f = _a.screener_type, screener_type = _f === void 0 ? "crypto_mkt" : _f, _g = _a.displayCurrency, displayCurrency = _g === void 0 ? "USD" : _g, _h = _a.colorTheme, colorTheme = _h === void 0 ? "light" : _h, _j = _a.locale, locale = _j === void 0 ? "en" : _j, _k = _a.isTransparent, isTransparent = _k === void 0 ? false : _k, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["width", "height", "autosize", "defaultColumn", "screener_type", "displayCurrency", "colorTheme", "locale", "isTransparent", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign(__assign({}, (!autosize ? { width: width } : { width: "100%" })), (!autosize ? { height: height } : { height: "100%" })), { defaultColumn: defaultColumn, screener_type: screener_type, displayCurrency: displayCurrency, colorTheme: colorTheme, locale: locale, isTransparent: isTransparent }), props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-screener.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/markets/cryptocurrencies/prices-all/", spanText: "Cryptocurrency Markets" })));
};

var EconomicCalendar = function (_a) {
    var _b = _a.colorTheme, colorTheme = _b === void 0 ? "light" : _b, _c = _a.isTransparent, isTransparent = _c === void 0 ? false : _c, _d = _a.width, width = _d === void 0 ? 510 : _d, _e = _a.height, height = _e === void 0 ? 600 : _e, _f = _a.autosize, autosize = _f === void 0 ? false : _f, _g = _a.locale, locale = _g === void 0 ? "en" : _g, _h = _a.importanceFilter, importanceFilter = _h === void 0 ? "-1,0,1" : _h, _j = _a.currencyFilter, currencyFilter = _j === void 0 ? undefined : _j, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["colorTheme", "isTransparent", "width", "height", "autosize", "locale", "importanceFilter", "currencyFilter", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign(__assign({ colorTheme: colorTheme, isTransparent: isTransparent }, (!autosize ? { width: width } : { width: "100%" })), (!autosize ? { height: height } : { height: "100%" })), { locale: locale, importanceFilter: importanceFilter, currencyFilter: currencyFilter }), props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-events.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/markets/currencies/economic-calendar/", spanText: "Economic Calendar" })));
};

var defaultCurrencies$1 = [
    "EUR",
    "USD",
    "JPY",
    "GBP",
    "CHF",
    "AUD",
    "CAD",
    "NZD",
    "CNY",
];
var ForexCrossRates = function (_a) {
    var _b = _a.width, width = _b === void 0 ? 770 : _b, _c = _a.height, height = _c === void 0 ? 400 : _c, _d = _a.autosize, autosize = _d === void 0 ? false : _d, _e = _a.currencies, currencies = _e === void 0 ? defaultCurrencies$1 : _e, _f = _a.isTransparent, isTransparent = _f === void 0 ? false : _f, _g = _a.colorTheme, colorTheme = _g === void 0 ? "light" : _g, _h = _a.locale, locale = _h === void 0 ? "en" : _h, _j = _a.largeChartUrl, largeChartUrl = _j === void 0 ? undefined : _j, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["width", "height", "autosize", "currencies", "isTransparent", "colorTheme", "locale", "largeChartUrl", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign(__assign({}, (!autosize ? { width: width } : { width: "100%" })), (!autosize ? { height: height } : { height: "100%" })), { currencies: currencies, isTransparent: isTransparent, colorTheme: colorTheme, locale: locale, largeChartUrl: largeChartUrl }), props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-forex-cross-rates.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/markets/currencies/forex-cross-rates/", spanText: "Exchange Rates" })));
};

var defaultCurrencies = [
    "EUR",
    "USD",
    "JPY",
    "GBP",
    "CHF",
    "AUD",
    "CAD",
    "NZD",
    "CNY",
];
var ForexHeatMap = function (_a) {
    var _b = _a.width, width = _b === void 0 ? 700 : _b, _c = _a.height, height = _c === void 0 ? 400 : _c, _d = _a.autosize, autosize = _d === void 0 ? false : _d, _e = _a.currencies, currencies = _e === void 0 ? defaultCurrencies : _e, _f = _a.isTransparent, isTransparent = _f === void 0 ? false : _f, _g = _a.colorTheme, colorTheme = _g === void 0 ? "light" : _g, _h = _a.locale, locale = _h === void 0 ? "en" : _h, _j = _a.largeChartUrl, largeChartUrl = _j === void 0 ? undefined : _j, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["width", "height", "autosize", "currencies", "isTransparent", "colorTheme", "locale", "largeChartUrl", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign(__assign({}, (!autosize ? { width: width } : { width: "100%" })), (!autosize ? { height: height } : { height: "100%" })), { currencies: currencies, isTransparent: isTransparent, colorTheme: colorTheme, locale: locale, largeChartUrl: largeChartUrl }), props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-forex-heat-map.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/markets/currencies/forex-heat-map/", spanText: "Forex Heat Map" })));
};

var FundamentalData = function (_a) {
    var _b = _a.symbol, symbol = _b === void 0 ? "NASDAQ:AAPL" : _b, _c = _a.colorTheme, colorTheme = _c === void 0 ? "light" : _c, _d = _a.isTransparent, isTransparent = _d === void 0 ? false : _d, _e = _a.largeChartUrl, largeChartUrl = _e === void 0 ? undefined : _e, _f = _a.displayMode, displayMode = _f === void 0 ? "regular" : _f, _g = _a.width, width = _g === void 0 ? 480 : _g, _h = _a.height, height = _h === void 0 ? 830 : _h, _j = _a.autosize, autosize = _j === void 0 ? false : _j, _k = _a.locale, locale = _k === void 0 ? "en" : _k, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["symbol", "colorTheme", "isTransparent", "largeChartUrl", "displayMode", "width", "height", "autosize", "locale", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign(__assign({}, (!autosize ? { width: width } : { width: "100%" })), (!autosize ? { height: height } : { height: "100%" })), { symbol: symbol, colorTheme: colorTheme, isTransparent: isTransparent, largeChartUrl: largeChartUrl, displayMode: displayMode, locale: locale }), props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-financials.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/symbols/".concat(symbol.replace(":", "-"), "/financials-overview/"), spanText: "".concat(symbol, " Fundamental Data") })));
};

var defaultSymbolGroup = [
    {
        name: "Indices",
        originalName: "Indices",
        symbols: [
            {
                name: "FOREXCOM:SPXUSD",
                displayName: "S&P 500",
            },
            {
                name: "FOREXCOM:NSXUSD",
                displayName: "Nasdaq 100",
            },
            {
                name: "FOREXCOM:DJI",
                displayName: "Dow 30",
            },
            {
                name: "INDEX:NKY",
                displayName: "Nikkei 225",
            },
            {
                name: "INDEX:DEU30",
                displayName: "DAX Index",
            },
            {
                name: "FOREXCOM:UKXGBP",
                displayName: "UK 100",
            },
        ],
    },
    {
        name: "Commodities",
        originalName: "Commodities",
        symbols: [
            {
                name: "CME_MINI:ES1!",
                displayName: "S&P 500",
            },
            {
                name: "CME:6E1!",
                displayName: "Euro",
            },
            {
                name: "COMEX:GC1!",
                displayName: "Gold",
            },
            {
                name: "NYMEX:CL1!",
                displayName: "Crude Oil",
            },
            {
                name: "NYMEX:NG1!",
                displayName: "Natural Gas",
            },
            {
                name: "CBOT:ZC1!",
                displayName: "Corn",
            },
        ],
    },
    {
        name: "Bonds",
        originalName: "Bonds",
        symbols: [
            {
                name: "CME:GE1!",
                displayName: "Eurodollar",
            },
            {
                name: "CBOT:ZB1!",
                displayName: "T-Bond",
            },
            {
                name: "CBOT:UB1!",
                displayName: "Ultra T-Bond",
            },
            {
                name: "EUREX:FGBL1!",
                displayName: "Euro Bund",
            },
            {
                name: "EUREX:FBTP1!",
                displayName: "Euro BTP",
            },
            {
                name: "EUREX:FGBM1!",
                displayName: "Euro BOBL",
            },
        ],
    },
    {
        name: "Forex",
        originalName: "Forex",
        symbols: [
            {
                name: "FX:EURUSD",
            },
            {
                name: "FX:GBPUSD",
            },
            {
                name: "FX:USDJPY",
            },
            {
                name: "FX:USDCHF",
            },
            {
                name: "FX:AUDUSD",
            },
            {
                name: "FX:USDCAD",
            },
        ],
    },
];
var MarketData = function (_a) {
    var _b = _a.width, width = _b === void 0 ? 770 : _b, _c = _a.height, height = _c === void 0 ? 450 : _c, _d = _a.autosize, autosize = _d === void 0 ? false : _d, _e = _a.symbolsGroups, symbolsGroups = _e === void 0 ? defaultSymbolGroup : _e, _f = _a.showSymbolLogo, showSymbolLogo = _f === void 0 ? true : _f, _g = _a.colorTheme, colorTheme = _g === void 0 ? "light" : _g, _h = _a.isTransparent, isTransparent = _h === void 0 ? false : _h, _j = _a.locale, locale = _j === void 0 ? "en" : _j, _k = _a.largeChartUrl, largeChartUrl = _k === void 0 ? undefined : _k, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["width", "height", "autosize", "symbolsGroups", "showSymbolLogo", "colorTheme", "isTransparent", "locale", "largeChartUrl", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign(__assign({}, (!autosize ? { width: width } : { width: "100%" })), (!autosize ? { height: height } : { height: "100%" })), { symbolsGroups: symbolsGroups, showSymbolLogo: showSymbolLogo, colorTheme: colorTheme, isTransparent: isTransparent, locale: locale, largeChartUrl: largeChartUrl }), props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-market-quotes.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, spanText: "Financial Markets", href: "https://www.tradingview.com/markets/" })));
};

var defaultTabs = [
    {
        title: "Indices",
        symbols: [
            {
                s: "FOREXCOM:SPXUSD",
                d: "S&P 500",
            },
            {
                s: "FOREXCOM:NSXUSD",
                d: "Nasdaq 100",
            },
            {
                s: "FOREXCOM:DJI",
                d: "Dow 30",
            },
            {
                s: "INDEX:NKY",
                d: "Nikkei 225",
            },
            {
                s: "INDEX:DEU30",
                d: "DAX Index",
            },
            {
                s: "FOREXCOM:UKXGBP",
                d: "UK 100",
            },
        ],
        originalTitle: "Indices",
    },
    {
        title: "Commodities",
        symbols: [
            {
                s: "CME_MINI:ES1!",
                d: "S&P 500",
            },
            {
                s: "CME:6E1!",
                d: "Euro",
            },
            {
                s: "COMEX:GC1!",
                d: "Gold",
            },
            {
                s: "NYMEX:CL1!",
                d: "Crude Oil",
            },
            {
                s: "NYMEX:NG1!",
                d: "Natural Gas",
            },
            {
                s: "CBOT:ZC1!",
                d: "Corn",
            },
        ],
        originalTitle: "Commodities",
    },
    {
        title: "Bonds",
        symbols: [
            {
                s: "CME:GE1!",
                d: "Eurodollar",
            },
            {
                s: "CBOT:ZB1!",
                d: "T-Bond",
            },
            {
                s: "CBOT:UB1!",
                d: "Ultra T-Bond",
            },
            {
                s: "EUREX:FGBL1!",
                d: "Euro Bund",
            },
            {
                s: "EUREX:FBTP1!",
                d: "Euro BTP",
            },
            {
                s: "EUREX:FGBM1!",
                d: "Euro BOBL",
            },
        ],
        originalTitle: "Bonds",
    },
    {
        title: "Forex",
        symbols: [
            {
                s: "FX:EURUSD",
            },
            {
                s: "FX:GBPUSD",
            },
            {
                s: "FX:USDJPY",
            },
            {
                s: "FX:USDCHF",
            },
            {
                s: "FX:AUDUSD",
            },
            {
                s: "FX:USDCAD",
            },
        ],
        originalTitle: "Forex",
    },
];
var MarketOverview = function (_a) {
    var _b = _a.colorTheme, colorTheme = _b === void 0 ? "light" : _b, _c = _a.dateRange, dateRange = _c === void 0 ? "12M" : _c, _d = _a.showChart, showChart = _d === void 0 ? true : _d, _e = _a.locale, locale = _e === void 0 ? "en" : _e, _f = _a.largeChartUrl, largeChartUrl = _f === void 0 ? undefined : _f, _g = _a.isTransparent, isTransparent = _g === void 0 ? false : _g, _h = _a.showSymbolLogo, showSymbolLogo = _h === void 0 ? true : _h, _j = _a.showFloatingTooltip, showFloatingTooltip = _j === void 0 ? false : _j, _k = _a.width, width = _k === void 0 ? 400 : _k, _l = _a.height, height = _l === void 0 ? 660 : _l, _m = _a.autosize, autosize = _m === void 0 ? false : _m, _o = _a.plotLineColorGrowing, plotLineColorGrowing = _o === void 0 ? "rgba(33, 150, 243, 1)" : _o, _p = _a.plotLineColorFalling, plotLineColorFalling = _p === void 0 ? "rgba(33, 150, 243, 1)" : _p, _q = _a.gridLineColor, gridLineColor = _q === void 0 ? "rgba(240, 243, 250, 1)" : _q, _r = _a.scaleFontColor, scaleFontColor = _r === void 0 ? "rgba(120, 123, 134, 1)" : _r, _s = _a.belowLineFillColorGrowing, belowLineFillColorGrowing = _s === void 0 ? "rgba(33, 150, 243, 0.12)" : _s, _t = _a.belowLineFillColorFalling, belowLineFillColorFalling = _t === void 0 ? "rgba(33, 150, 243, 0.12)" : _t, _u = _a.belowLineFillColorGrowingBottom, belowLineFillColorGrowingBottom = _u === void 0 ? "rgba(41, 98, 255, 0)" : _u, _v = _a.belowLineFillColorFallingBottom, belowLineFillColorFallingBottom = _v === void 0 ? "rgba(41, 98, 255, 0)" : _v, _w = _a.symbolActiveColor, symbolActiveColor = _w === void 0 ? "rgba(33, 150, 243, 0.12)" : _w, _x = _a.tabs, tabs = _x === void 0 ? defaultTabs : _x, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["colorTheme", "dateRange", "showChart", "locale", "largeChartUrl", "isTransparent", "showSymbolLogo", "showFloatingTooltip", "width", "height", "autosize", "plotLineColorGrowing", "plotLineColorFalling", "gridLineColor", "scaleFontColor", "belowLineFillColorGrowing", "belowLineFillColorFalling", "belowLineFillColorGrowingBottom", "belowLineFillColorFallingBottom", "symbolActiveColor", "tabs", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign(__assign(__assign({ colorTheme: colorTheme, dateRange: dateRange, showChart: showChart, locale: locale, largeChartUrl: largeChartUrl, isTransparent: isTransparent, showSymbolLogo: showSymbolLogo, showFloatingTooltip: showFloatingTooltip }, (!autosize ? { width: width } : { width: "100%" })), (!autosize ? { height: height } : { height: "100%" })), (showChart && {
                plotLineColorGrowing: plotLineColorGrowing,
                plotLineColorFalling: plotLineColorFalling,
                gridLineColor: gridLineColor,
                scaleFontColor: scaleFontColor,
                belowLineFillColorGrowing: belowLineFillColorGrowing,
                belowLineFillColorFalling: belowLineFillColorFalling,
                belowLineFillColorGrowingBottom: belowLineFillColorGrowingBottom,
                belowLineFillColorFallingBottom: belowLineFillColorFallingBottom,
                symbolActiveColor: symbolActiveColor,
            })), { tabs: tabs }), props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, spanText: "Financial Markets", href: "https://www.tradingview.com/markets/" })));
};

var MiniChart = function (_a) {
    var _b = _a.symbol, symbol = _b === void 0 ? "FX:EURUSD" : _b, _c = _a.width, width = _c === void 0 ? 350 : _c, _d = _a.height, height = _d === void 0 ? 220 : _d, _e = _a.locale, locale = _e === void 0 ? "en" : _e, _f = _a.dateRange, dateRange = _f === void 0 ? "12M" : _f, _g = _a.colorTheme, colorTheme = _g === void 0 ? "light" : _g, _h = _a.trendLineColor, trendLineColor = _h === void 0 ? "rgba(41, 98, 255, 1)" : _h, _j = _a.underLineColor, underLineColor = _j === void 0 ? "rgba(41, 98, 255, 0.3)" : _j; _a.underLineBottomColor; var _l = _a.isTransparent, isTransparent = _l === void 0 ? false : _l, _m = _a.autosize, autosize = _m === void 0 ? false : _m, _o = _a.largeChartUrl, largeChartUrl = _o === void 0 ? undefined : _o, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["symbol", "width", "height", "locale", "dateRange", "colorTheme", "trendLineColor", "underLineColor", "underLineBottomColor", "isTransparent", "autosize", "largeChartUrl", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign(__assign({ symbol: symbol }, (!autosize ? { width: width } : { width: "100%" })), (!autosize ? { height: height } : { height: "100%" })), { locale: locale, dateRange: dateRange, colorTheme: colorTheme, trendLineColor: trendLineColor, underLineColor: underLineColor, isTransparent: isTransparent, autosize: autosize, largeChartUrl: largeChartUrl }), props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/symbols/".concat(symbol, "/"), spanText: "".concat(symbol, " Rates") })));
};

var Screener = function (_a) {
    var _b = _a.width, width = _b === void 0 ? 1100 : _b, _c = _a.height, height = _c === void 0 ? 512 : _c, _d = _a.autosize, autosize = _d === void 0 ? false : _d, _e = _a.defaultColumn, defaultColumn = _e === void 0 ? "overview" : _e, _f = _a.defaultScreen, defaultScreen = _f === void 0 ? "general" : _f, _g = _a.market, market = _g === void 0 ? "forex" : _g, _h = _a.showToolbar, showToolbar = _h === void 0 ? true : _h, _j = _a.colorTheme, colorTheme = _j === void 0 ? "light" : _j, _k = _a.locale, locale = _k === void 0 ? "en" : _k, _l = _a.isTransparent, isTransparent = _l === void 0 ? false : _l, _m = _a.largeChartUrl, largeChartUrl = _m === void 0 ? undefined : _m, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["width", "height", "autosize", "defaultColumn", "defaultScreen", "market", "showToolbar", "colorTheme", "locale", "isTransparent", "largeChartUrl", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign(__assign({}, (!autosize ? { width: width } : { width: "100%" })), (!autosize ? { height: height } : { height: "100%" })), { defaultColumn: defaultColumn, defaultScreen: defaultScreen, market: market, showToolbar: showToolbar, colorTheme: colorTheme, locale: locale, isTransparent: isTransparent, largeChartUrl: largeChartUrl }), props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-screener.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/forex-screener/", spanText: "Forex Screener" })));
};

var SingleTicker = function (_a) {
    var _b = _a.symbol, symbol = _b === void 0 ? "FX:EURUSD" : _b, _c = _a.width, width = _c === void 0 ? 350 : _c, _d = _a.autosize, autosize = _d === void 0 ? false : _d, _e = _a.colorTheme, colorTheme = _e === void 0 ? "light" : _e, _f = _a.isTransparent, isTransparent = _f === void 0 ? false : _f, _g = _a.locale, locale = _g === void 0 ? "en" : _g, _h = _a.largeChartUrl, largeChartUrl = _h === void 0 ? undefined : _h, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["symbol", "width", "autosize", "colorTheme", "isTransparent", "locale", "largeChartUrl", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign({ symbol: symbol }, (!autosize ? { width: width } : { width: "100%" })), { colorTheme: colorTheme, isTransparent: isTransparent, locale: locale, largeChartUrl: largeChartUrl }), props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/symbols/".concat(symbol, "/"), spanText: "".concat(symbol, " Rates") })));
};

var StockMarket = function (_a) {
    var _b = _a.colorTheme, colorTheme = _b === void 0 ? "light" : _b, _c = _a.dateRange, dateRange = _c === void 0 ? "12M" : _c, _d = _a.exchange, exchange = _d === void 0 ? "US" : _d, _e = _a.showChart, showChart = _e === void 0 ? true : _e, _f = _a.locale, locale = _f === void 0 ? "en" : _f, _g = _a.largeChartUrl, largeChartUrl = _g === void 0 ? undefined : _g, _h = _a.isTransparent, isTransparent = _h === void 0 ? false : _h, _j = _a.showSymbolLogo, showSymbolLogo = _j === void 0 ? true : _j; _a.showFloatingTooltip; var _l = _a.width, width = _l === void 0 ? 400 : _l, _m = _a.height, height = _m === void 0 ? 600 : _m, _o = _a.autosize, autosize = _o === void 0 ? false : _o, _p = _a.plotLineColorGrowing, plotLineColorGrowing = _p === void 0 ? "rgba(33, 150, 243, 1)" : _p, _q = _a.plotLineColorFalling, plotLineColorFalling = _q === void 0 ? "rgba(33, 150, 243, 1)" : _q, _r = _a.gridLineColor, gridLineColor = _r === void 0 ? "rgba(240, 243, 250, 1)" : _r, _s = _a.scaleFontColor, scaleFontColor = _s === void 0 ? "rgba(120, 123, 134, 1)" : _s, _t = _a.belowLineFillColorGrowing, belowLineFillColorGrowing = _t === void 0 ? "rgba(33, 150, 243, 0.12)" : _t, _u = _a.belowLineFillColorFalling, belowLineFillColorFalling = _u === void 0 ? "rgba(33, 150, 243, 0.12)" : _u, _v = _a.belowLineFillColorGrowingBottom, belowLineFillColorGrowingBottom = _v === void 0 ? "rgba(41, 98, 255, 0)" : _v, _w = _a.belowLineFillColorFallingBottom, belowLineFillColorFallingBottom = _w === void 0 ? "rgba(41, 98, 255, 0)" : _w, _x = _a.symbolActiveColor, symbolActiveColor = _x === void 0 ? "rgba(33, 150, 243, 0.12)" : _x, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["colorTheme", "dateRange", "exchange", "showChart", "locale", "largeChartUrl", "isTransparent", "showSymbolLogo", "showFloatingTooltip", "width", "height", "autosize", "plotLineColorGrowing", "plotLineColorFalling", "gridLineColor", "scaleFontColor", "belowLineFillColorGrowing", "belowLineFillColorFalling", "belowLineFillColorGrowingBottom", "belowLineFillColorFallingBottom", "symbolActiveColor", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign(__assign({ colorTheme: colorTheme, dateRange: dateRange, exchange: exchange, showChart: showChart, locale: locale, largeChartUrl: largeChartUrl, isTransparent: isTransparent, showSymbolLogo: showSymbolLogo }, (!autosize ? { width: width } : { width: "100%" })), (!autosize ? { height: height } : { height: "100%" })), (showChart && {
                plotLineColorGrowing: plotLineColorGrowing,
                plotLineColorFalling: plotLineColorFalling,
                gridLineColor: gridLineColor,
                scaleFontColor: scaleFontColor,
                belowLineFillColorGrowing: belowLineFillColorGrowing,
                belowLineFillColorFalling: belowLineFillColorFalling,
                belowLineFillColorGrowingBottom: belowLineFillColorGrowingBottom,
                belowLineFillColorFallingBottom: belowLineFillColorFallingBottom,
                symbolActiveColor: symbolActiveColor,
            })), props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-hotlists.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/markets/stocks-usa/", spanText: "Stock market Today" })));
};

var SymbolInfo = function (_a) {
    var _b = _a.symbol, symbol = _b === void 0 ? "NASDAQ:AAPL" : _b, _c = _a.width, width = _c === void 0 ? 1000 : _c, _d = _a.autosize, autosize = _d === void 0 ? false : _d, _e = _a.locale, locale = _e === void 0 ? "en" : _e, _f = _a.colorTheme, colorTheme = _f === void 0 ? "light" : _f, _g = _a.isTransparent, isTransparent = _g === void 0 ? false : _g, _h = _a.largeChartUrl, largeChartUrl = _h === void 0 ? undefined : _h, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["symbol", "width", "autosize", "locale", "colorTheme", "isTransparent", "largeChartUrl", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign({ symbol: symbol }, (!autosize ? { width: width } : { width: "100%" })), { locale: locale, colorTheme: colorTheme, isTransparent: isTransparent, largeChartUrl: largeChartUrl }), props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/symbols/".concat(symbol, "/"), spanText: "".concat(symbol, " Price Today") })));
};

var defaultSymbols$2 = [
    ["Apple", "AAPL"],
    ["Google", "GOOGL"],
    ["Microsoft", "MSFT"],
];
var SymbolOverview = function (_a) {
    var _b = _a.symbols, symbols = _b === void 0 ? defaultSymbols$2 : _b, _c = _a.chartOnly, chartOnly = _c === void 0 ? false : _c, _d = _a.width, width = _d === void 0 ? 1000 : _d, _e = _a.height, height = _e === void 0 ? 400 : _e, _f = _a.locale, locale = _f === void 0 ? "en" : _f, _g = _a.colorTheme, colorTheme = _g === void 0 ? "light" : _g, _h = _a.fontColor, fontColor = _h === void 0 ? "#787B86" : _h, _j = _a.fontSize, fontSize = _j === void 0 ? "10" : _j, _k = _a.isTransparent, isTransparent = _k === void 0 ? false : _k, _l = _a.showFloatingTooltip, showFloatingTooltip = _l === void 0 ? true : _l, _m = _a.scalePosition, scalePosition = _m === void 0 ? "no" : _m, _o = _a.scaleMode, scaleMode = _o === void 0 ? "Normal" : _o, _p = _a.fontFamily, fontFamily = _p === void 0 ? "Trebuchet MS, sans-serif" : _p, _q = _a.noTimeScale, noTimeScale = _q === void 0 ? false : _q, _r = _a.valuesTracking, valuesTracking = _r === void 0 ? "1" : _r, _s = _a.lineWidth, lineWidth = _s === void 0 ? 3 : _s, _t = _a.showVolume, showVolume = _t === void 0 ? false : _t, _u = _a.volumeUpColor, volumeUpColor = _u === void 0 ? "rgba(34, 171, 148, 0.5)" : _u, _v = _a.volumeDownColor, volumeDownColor = _v === void 0 ? "rgba(247, 82, 95, 0.5)" : _v, _w = _a.dateFormat, dateFormat = _w === void 0 ? "dd MMM 'yy" : _w, _x = _a.timeHoursFormat, timeHoursFormat = _x === void 0 ? "24-hours" : _x, _y = _a.hideMarketStatus, hideMarketStatus = _y === void 0 ? false : _y, _z = _a.hideDateRanges, hideDateRanges = _z === void 0 ? false : _z, _0 = _a.chartType, chartType = _0 === void 0 ? "area" : _0, 
    //area
    _1 = _a.lineColor, 
    //area
    lineColor = _1 === void 0 ? "#2962FF" : _1, _2 = _a.bottomColor, bottomColor = _2 === void 0 ? "rgba(41, 98, 255, 0)" : _2, _3 = _a.topColor, topColor = _3 === void 0 ? "rgba(41, 98, 255, 0.3)" : _3, 
    //bars & candles
    _4 = _a.upColor, 
    //bars & candles
    upColor = _4 === void 0 ? "#26a69a" : _4, _5 = _a.downColor, downColor = _5 === void 0 ? "#ef5350" : _5, 
    //candles
    _6 = _a.borderUpColor, 
    //candles
    borderUpColor = _6 === void 0 ? "#26a69a" : _6, _7 = _a.borderDownColor, borderDownColor = _7 === void 0 ? "#ef5350" : _7, _8 = _a.wickUpColor, wickUpColor = _8 === void 0 ? "#26a69a" : _8, _9 = _a.wickDownColor, wickDownColor = _9 === void 0 ? "#ef5350" : _9, _10 = _a.backGroundColor, backGroundColor = _10 === void 0 ? "rgba(19, 23, 34, 0)" : _10, _11 = _a.gridLineColor, gridLineColor = _11 === void 0 ? "rgba(42, 46, 57, 0)" : _11, _12 = _a.widgetFontColor, widgetFontColor = _12 === void 0 ? "rgba(216, 216, 216, 1)" : _12, _13 = _a.autosize, autosize = _13 === void 0 ? false : _13, _14 = _a.container_id, container_id = _14 === void 0 ? "tradingview_".concat(createId(5)) : _14, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["symbols", "chartOnly", "width", "height", "locale", "colorTheme", "fontColor", "fontSize", "isTransparent", "showFloatingTooltip", "scalePosition", "scaleMode", "fontFamily", "noTimeScale", "valuesTracking", "lineWidth", "showVolume", "volumeUpColor", "volumeDownColor", "dateFormat", "timeHoursFormat", "hideMarketStatus", "hideDateRanges", "chartType", "lineColor", "bottomColor", "topColor", "upColor", "downColor", "borderUpColor", "borderDownColor", "wickUpColor", "wickDownColor", "backGroundColor", "gridLineColor", "widgetFontColor", "autosize", "container_id", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign(__assign(__assign(__assign(__assign(__assign(__assign(__assign(__assign({ symbols: symbols, chartOnly: chartOnly }, (!autosize ? { width: width } : { width: "100%" })), (!autosize ? { height: height } : { height: "100%" })), { locale: locale, colorTheme: colorTheme, fontColor: fontColor, fontSize: fontSize, isTransparent: isTransparent, showFloatingTooltip: showFloatingTooltip, scalePosition: scalePosition, scaleMode: scaleMode, fontFamily: fontFamily, noTimeScale: noTimeScale, hideDateRanges: hideDateRanges, hideMarketStatus: hideMarketStatus, valuesTracking: valuesTracking, lineWidth: lineWidth, showVolume: showVolume }), (showVolume && { volumeUpColor: volumeUpColor, volumeDownColor: volumeDownColor })), { dateFormat: dateFormat, timeHoursFormat: timeHoursFormat, chartType: chartType }), (chartType === "line" && { lineColor: lineColor })), (chartType === "area" && { lineColor: lineColor, bottomColor: bottomColor, topColor: topColor })), ((chartType === "bars" || chartType === "candlesticks") && {
                upColor: upColor,
                downColor: downColor,
            })), (chartType === "candlesticks" && {
                upColor: upColor,
                downColor: downColor,
                borderUpColor: borderUpColor,
                borderDownColor: borderDownColor,
                wickUpColor: wickUpColor,
                wickDownColor: wickDownColor,
            })), { backGroundColor: backGroundColor, widgetFontColor: widgetFontColor, gridLineColor: gridLineColor, autosize: autosize, container_id: container_id }), props), scriptSRC: "https://s3.tradingview.com/tv.js", containerId: container_id, type: "MediumWidget" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/symbols/".concat(symbols[0][1]), spanText: "".concat(symbols[0][1]) })));
};

var TechnicalAnalysis = function (_a) {
    var _b = _a.interval, interval = _b === void 0 ? "1m" : _b, _c = _a.width, width = _c === void 0 ? 425 : _c, _d = _a.height, height = _d === void 0 ? 450 : _d, _e = _a.autosize, autosize = _e === void 0 ? false : _e, _f = _a.isTransparent, isTransparent = _f === void 0 ? false : _f, _g = _a.symbol, symbol = _g === void 0 ? "NASDAQ:AAPL" : _g, _h = _a.showIntervalTabs, showIntervalTabs = _h === void 0 ? true : _h, _j = _a.locale, locale = _j === void 0 ? "en" : _j, _k = _a.colorTheme, colorTheme = _k === void 0 ? "light" : _k, _l = _a.largeChartUrl, largeChartUrl = _l === void 0 ? undefined : _l, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["interval", "width", "height", "autosize", "isTransparent", "symbol", "showIntervalTabs", "locale", "colorTheme", "largeChartUrl", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign(__assign({ interval: interval }, (!autosize ? { width: width } : { width: "100%" })), (!autosize ? { height: height } : { height: "100%" })), { isTransparent: isTransparent, symbol: symbol, showIntervalTabs: showIntervalTabs, locale: locale, colorTheme: colorTheme, largeChartUrl: largeChartUrl }), props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/symbols/".concat(symbol.replace(":", "-"), "/technicals/"), spanText: "Technical Analysis for ".concat(symbol) })));
};

var defaultSymbols$1 = [
    {
        proName: "FOREXCOM:SPXUSD",
        title: "S&P 500",
    },
    {
        proName: "FOREXCOM:NSXUSD",
        title: "Nasdaq 100",
    },
    {
        proName: "FX_IDC:EURUSD",
        title: "EUR/USD",
    },
    {
        proName: "BITSTAMP:BTCUSD",
        title: "BTC/USD",
    },
    {
        proName: "BITSTAMP:ETHUSD",
        title: "ETH/USD",
    },
];
var Ticker = function (_a) {
    var _b = _a.colorTheme, colorTheme = _b === void 0 ? "light" : _b, _c = _a.isTransparent, isTransparent = _c === void 0 ? false : _c, _d = _a.showSymbolLogo, showSymbolLogo = _d === void 0 ? true : _d, _e = _a.locale, locale = _e === void 0 ? "en" : _e, _f = _a.symbols, symbols = _f === void 0 ? defaultSymbols$1 : _f, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["colorTheme", "isTransparent", "showSymbolLogo", "locale", "symbols", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign({ colorTheme: colorTheme, isTransparent: isTransparent, showSymbolLogo: showSymbolLogo, locale: locale, symbols: symbols }, props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-tickers.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/", spanText: "Qoutes" })));
};

var defaultSymbols = [
    {
        proName: "FOREXCOM:SPXUSD",
        title: "S&P 500",
    },
    {
        proName: "FOREXCOM:NSXUSD",
        title: "Nasdaq 100",
    },
    {
        proName: "FX_IDC:EURUSD",
        title: "EUR/USD",
    },
    {
        proName: "BITSTAMP:BTCUSD",
        title: "BTC/USD",
    },
    {
        proName: "BITSTAMP:ETHUSD",
        title: "ETH/USD",
    },
];
var TickerTape = function (_a) {
    var _b = _a.symbols, symbols = _b === void 0 ? defaultSymbols : _b, _c = _a.showSymbolLogo, showSymbolLogo = _c === void 0 ? true : _c, _d = _a.colorTheme, colorTheme = _d === void 0 ? "light" : _d, _e = _a.isTransparent, isTransparent = _e === void 0 ? false : _e, _f = _a.largeChartUrl, largeChartUrl = _f === void 0 ? undefined : _f, _g = _a.displayMode, displayMode = _g === void 0 ? "adaptive" : _g, _h = _a.locale, locale = _h === void 0 ? "en" : _h, copyrightStyles = _a.copyrightStyles, props = __rest(_a, ["symbols", "showSymbolLogo", "colorTheme", "isTransparent", "largeChartUrl", "displayMode", "locale", "copyrightStyles"]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign({ symbols: symbols, showSymbolLogo: showSymbolLogo, colorTheme: colorTheme, isTransparent: isTransparent, largeChartUrl: largeChartUrl, displayMode: displayMode, locale: locale }, props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/markets/", spanText: "Markets" })));
};

var Timeline = function (_a) {
    var _b = _a.feedMode, feedMode = _b === void 0 ? "all_symbols" : _b, _c = _a.colorTheme, colorTheme = _c === void 0 ? "light" : _c, _d = _a.isTransparent, isTransparent = _d === void 0 ? false : _d, _e = _a.displayMode, displayMode = _e === void 0 ? "regular" : _e, _f = _a.width, width = _f === void 0 ? 480 : _f, _g = _a.height, height = _g === void 0 ? 830 : _g, _h = _a.autosize, autosize = _h === void 0 ? false : _h, _j = _a.locale, locale = _j === void 0 ? "en" : _j, _k = _a.largeChartUrl, largeChartUrl = _k === void 0 ? undefined : _k, copyrightStyles = _a.copyrightStyles, _l = _a.symbol, symbol = _l === void 0 ? "BTCUSD" : _l, _m = _a.market, market = _m === void 0 ? "crypto" : _m, props = __rest(_a, ["feedMode", "colorTheme", "isTransparent", "displayMode", "width", "height", "autosize", "locale", "largeChartUrl", "copyrightStyles", "symbol", "market"]);
    var _o = React.useState(""), href = _o[0], sethref = _o[1];
    var _p = React.useState(""), spanText = _p[0], setspanText = _p[1];
    React.useEffect(function () {
        if (feedMode == "all_symbols") {
            sethref("key_events");
            setspanText("Daily news roundup");
        }
        else if (feedMode == "market") {
            switch (market) {
                case "crypto":
                    sethref("markets/cryptocurrencies/key-events/");
                    setspanText("Daily cryptocurrency news");
                    break;
                case "forex":
                    sethref("markets/currencies/key-events/");
                    setspanText("Daily currency news");
                    break;
                case "stock":
                    sethref("markets/stocks-usa/key-events/");
                    setspanText("Daily stock news");
                    break;
                case "index":
                    sethref("markets/indices/key-events/");
                    setspanText("Daily index news");
                    break;
                case "futures":
                    sethref("markets/futures/key-events/");
                    setspanText("Daily futures news");
                    break;
                case "cfd":
                    sethref("markets/bonds/key-events/");
                    setspanText("Daily bonds news");
                    break;
            }
        }
        else if (feedMode == "symbol") {
            sethref("symbols/".concat(symbol, "/history-timeline/"));
            setspanText("".concat(symbol, " History"));
        }
    }, [feedMode, symbol, market]);
    return (React__default["default"].createElement("div", { id: "tradingview_widget_wrapper" },
        React__default["default"].createElement(Widget, { scriptHTML: __assign(__assign(__assign(__assign(__assign(__assign({}, (!autosize ? { width: width } : { width: "100%" })), (!autosize ? { height: height } : { height: "100%" })), { feedMode: feedMode }), (feedMode == "market"
                ? { market: market }
                : feedMode == "symbol"
                    ? { symbol: symbol }
                    : {})), { colorTheme: colorTheme, isTransparent: isTransparent, displayMode: displayMode, locale: locale, largeChartUrl: largeChartUrl }), props), scriptSRC: "https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" }),
        React__default["default"].createElement(Copyright, { copyrightStyles: copyrightStyles, href: "https://www.tradingview.com/".concat(href), spanText: spanText })));
};

exports.AdvancedRealTimeChart = AdvancedRealTimeChart;
exports.CompanyProfile = CompanyProfile;
exports.CryptoCurrencyMarket = CryptoCurrencyMarket;
exports.EconomicCalendar = EconomicCalendar;
exports.ForexCrossRates = ForexCrossRates;
exports.ForexHeatMap = ForexHeatMap;
exports.FundamentalData = FundamentalData;
exports.MarketData = MarketData;
exports.MarketOverview = MarketOverview;
exports.MiniChart = MiniChart;
exports.Screener = Screener;
exports.SingleTicker = SingleTicker;
exports.StockMarket = StockMarket;
exports.SymbolInfo = SymbolInfo;
exports.SymbolOverview = SymbolOverview;
exports.TechnicalAnalysis = TechnicalAnalysis;
exports.Ticker = Ticker;
exports.TickerTape = TickerTape;
exports.Timeline = Timeline;
//# sourceMappingURL=index.js.map
