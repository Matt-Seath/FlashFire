/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(() => {
var exports = {};
exports.id = "pages/_app";
exports.ids = ["pages/_app"];
exports.modules = {

/***/ "./src/createEmotionCache.ts":
/*!***********************************!*\
  !*** ./src/createEmotionCache.ts ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (/* binding */ createEmotionCache)\n/* harmony export */ });\n/* harmony import */ var _emotion_cache__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @emotion/cache */ \"@emotion/cache\");\n/* harmony import */ var _emotion_cache__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_emotion_cache__WEBPACK_IMPORTED_MODULE_0__);\n\nconst isBrowser = typeof document !== \"undefined\";\n// On the client side, Create a meta tag at the top of the <head> and set it as insertionPoint.\n// This assures that MUI styles are loaded first.\n// It allows developers to easily override MUI styles with other styling solutions, like CSS modules.\nfunction createEmotionCache() {\n    let insertionPoint;\n    if (isBrowser) {\n        const emotionInsertionPoint = document.querySelector('meta[name=\"emotion-insertion-point\"]');\n        insertionPoint = emotionInsertionPoint ?? undefined;\n    }\n    return _emotion_cache__WEBPACK_IMPORTED_MODULE_0___default()({\n        key: \"mui-style\",\n        insertionPoint\n    });\n}\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvY3JlYXRlRW1vdGlvbkNhY2hlLnRzLmpzIiwibWFwcGluZ3MiOiI7Ozs7OztBQUF5QztBQUV6QyxNQUFNQyxZQUFZLE9BQU9DLGFBQWE7QUFFdEMsK0ZBQStGO0FBQy9GLGlEQUFpRDtBQUNqRCxxR0FBcUc7QUFDdEYsU0FBU0MscUJBQXFCO0lBQzNDLElBQUlDO0lBRUosSUFBSUgsV0FBVztRQUNiLE1BQU1JLHdCQUF3QkgsU0FBU0ksYUFBYSxDQUNsRDtRQUVGRixpQkFBaUJDLHlCQUF5QkU7SUFDNUMsQ0FBQztJQUVELE9BQU9QLHFEQUFXQSxDQUFDO1FBQUVRLEtBQUs7UUFBYUo7SUFBZTtBQUN4RCxDQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vZnJvbnRlbmQvLi9zcmMvY3JlYXRlRW1vdGlvbkNhY2hlLnRzPzkxMjciXSwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IGNyZWF0ZUNhY2hlIGZyb20gJ0BlbW90aW9uL2NhY2hlJztcblxuY29uc3QgaXNCcm93c2VyID0gdHlwZW9mIGRvY3VtZW50ICE9PSAndW5kZWZpbmVkJztcblxuLy8gT24gdGhlIGNsaWVudCBzaWRlLCBDcmVhdGUgYSBtZXRhIHRhZyBhdCB0aGUgdG9wIG9mIHRoZSA8aGVhZD4gYW5kIHNldCBpdCBhcyBpbnNlcnRpb25Qb2ludC5cbi8vIFRoaXMgYXNzdXJlcyB0aGF0IE1VSSBzdHlsZXMgYXJlIGxvYWRlZCBmaXJzdC5cbi8vIEl0IGFsbG93cyBkZXZlbG9wZXJzIHRvIGVhc2lseSBvdmVycmlkZSBNVUkgc3R5bGVzIHdpdGggb3RoZXIgc3R5bGluZyBzb2x1dGlvbnMsIGxpa2UgQ1NTIG1vZHVsZXMuXG5leHBvcnQgZGVmYXVsdCBmdW5jdGlvbiBjcmVhdGVFbW90aW9uQ2FjaGUoKSB7XG4gIGxldCBpbnNlcnRpb25Qb2ludDtcblxuICBpZiAoaXNCcm93c2VyKSB7XG4gICAgY29uc3QgZW1vdGlvbkluc2VydGlvblBvaW50ID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcjxIVE1MTWV0YUVsZW1lbnQ+KFxuICAgICAgJ21ldGFbbmFtZT1cImVtb3Rpb24taW5zZXJ0aW9uLXBvaW50XCJdJyxcbiAgICApO1xuICAgIGluc2VydGlvblBvaW50ID0gZW1vdGlvbkluc2VydGlvblBvaW50ID8/IHVuZGVmaW5lZDtcbiAgfVxuXG4gIHJldHVybiBjcmVhdGVDYWNoZSh7IGtleTogJ211aS1zdHlsZScsIGluc2VydGlvblBvaW50IH0pO1xufVxuIl0sIm5hbWVzIjpbImNyZWF0ZUNhY2hlIiwiaXNCcm93c2VyIiwiZG9jdW1lbnQiLCJjcmVhdGVFbW90aW9uQ2FjaGUiLCJpbnNlcnRpb25Qb2ludCIsImVtb3Rpb25JbnNlcnRpb25Qb2ludCIsInF1ZXJ5U2VsZWN0b3IiLCJ1bmRlZmluZWQiLCJrZXkiXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./src/createEmotionCache.ts\n");

/***/ }),

/***/ "./src/pages/_app.tsx":
/*!****************************!*\
  !*** ./src/pages/_app.tsx ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (/* binding */ MyApp)\n/* harmony export */ });\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-dev-runtime */ \"react/jsx-dev-runtime\");\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ \"react\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var next_head__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! next/head */ \"next/head\");\n/* harmony import */ var next_head__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(next_head__WEBPACK_IMPORTED_MODULE_2__);\n/* harmony import */ var _mui_material_styles__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @mui/material/styles */ \"@mui/material/styles\");\n/* harmony import */ var _mui_material_styles__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_mui_material_styles__WEBPACK_IMPORTED_MODULE_3__);\n/* harmony import */ var _mui_material_CssBaseline__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @mui/material/CssBaseline */ \"@mui/material/CssBaseline\");\n/* harmony import */ var _mui_material_CssBaseline__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_mui_material_CssBaseline__WEBPACK_IMPORTED_MODULE_4__);\n/* harmony import */ var _emotion_react__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @emotion/react */ \"@emotion/react\");\n/* harmony import */ var _emotion_react__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_emotion_react__WEBPACK_IMPORTED_MODULE_5__);\n/* harmony import */ var _createEmotionCache__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ../createEmotionCache */ \"./src/createEmotionCache.ts\");\n/* harmony import */ var _styles_globals_css__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ../styles/globals.css */ \"./src/styles/globals.css\");\n/* harmony import */ var _styles_globals_css__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_styles_globals_css__WEBPACK_IMPORTED_MODULE_7__);\n\n\n\n\n\n\n\n\nconst lightTheme = (0,_mui_material_styles__WEBPACK_IMPORTED_MODULE_3__.createTheme)({\n    palette: {\n        mode: \"light\"\n    }\n});\nconst darkTheme = (0,_mui_material_styles__WEBPACK_IMPORTED_MODULE_3__.createTheme)({\n    palette: {\n        mode: \"dark\"\n    }\n});\n// Client-side cache, shared for the whole session of the user in the browser.\nconst clientSideEmotionCache = (0,_createEmotionCache__WEBPACK_IMPORTED_MODULE_6__[\"default\"])();\nfunction MyApp(props) {\n    const { Component , emotionCache =clientSideEmotionCache , pageProps  } = props;\n    return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_emotion_react__WEBPACK_IMPORTED_MODULE_5__.CacheProvider, {\n        value: emotionCache,\n        children: [\n            /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)((next_head__WEBPACK_IMPORTED_MODULE_2___default()), {\n                children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"meta\", {\n                    name: \"viewport\",\n                    content: \"initial-scale=1, width=device-width\"\n                }, void 0, false, {\n                    fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n                    lineNumber: 35,\n                    columnNumber: 9\n                }, this)\n            }, void 0, false, {\n                fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n                lineNumber: 34,\n                columnNumber: 7\n            }, this),\n            /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_mui_material_styles__WEBPACK_IMPORTED_MODULE_3__.ThemeProvider, {\n                theme: darkTheme,\n                children: [\n                    /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)((_mui_material_CssBaseline__WEBPACK_IMPORTED_MODULE_4___default()), {}, void 0, false, {\n                        fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n                        lineNumber: 39,\n                        columnNumber: 9\n                    }, this),\n                    /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(Component, {\n                        ...pageProps\n                    }, void 0, false, {\n                        fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n                        lineNumber: 40,\n                        columnNumber: 9\n                    }, this)\n                ]\n            }, void 0, true, {\n                fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n                lineNumber: 37,\n                columnNumber: 7\n            }, this)\n        ]\n    }, void 0, true, {\n        fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n        lineNumber: 33,\n        columnNumber: 5\n    }, this);\n}\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcGFnZXMvX2FwcC50c3guanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBK0I7QUFDRjtBQUVxQztBQUNkO0FBQ1M7QUFFTjtBQUN4QjtBQUUvQixNQUFNTyxhQUFhSixpRUFBV0EsQ0FBQztJQUM3QkssU0FBUztRQUNQQyxNQUFNO0lBQ1I7QUFDRjtBQUVBLE1BQU1DLFlBQVlQLGlFQUFXQSxDQUFDO0lBQzVCSyxTQUFTO1FBQ1BDLE1BQU07SUFDUjtBQUNGO0FBRUEsOEVBQThFO0FBQzlFLE1BQU1FLHlCQUF5QkwsK0RBQWtCQTtBQU1sQyxTQUFTTSxNQUFNQyxLQUFpQixFQUFFO0lBQy9DLE1BQU0sRUFBRUMsVUFBUyxFQUFFQyxjQUFlSix1QkFBc0IsRUFBRUssVUFBUyxFQUFFLEdBQUdIO0lBQ3hFLHFCQUNFLDhEQUFDUix5REFBYUE7UUFBQ1ksT0FBT0Y7OzBCQUNwQiw4REFBQ2Qsa0RBQUlBOzBCQUNILDRFQUFDaUI7b0JBQUtDLE1BQUs7b0JBQVdDLFNBQVE7Ozs7Ozs7Ozs7OzBCQUVoQyw4REFBQ2xCLCtEQUFhQTtnQkFBQ21CLE9BQU9YOztrQ0FFcEIsOERBQUNOLGtFQUFXQTs7Ozs7a0NBQ1osOERBQUNVO3dCQUFXLEdBQUdFLFNBQVM7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUloQyxDQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vZnJvbnRlbmQvLi9zcmMvcGFnZXMvX2FwcC50c3g/ZjlkNiJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgKiBhcyBSZWFjdCBmcm9tIFwicmVhY3RcIjtcbmltcG9ydCBIZWFkIGZyb20gXCJuZXh0L2hlYWRcIjtcbmltcG9ydCB7IEFwcFByb3BzIH0gZnJvbSBcIm5leHQvYXBwXCI7XG5pbXBvcnQgeyBUaGVtZVByb3ZpZGVyLCBjcmVhdGVUaGVtZSB9IGZyb20gXCJAbXVpL21hdGVyaWFsL3N0eWxlc1wiO1xuaW1wb3J0IENzc0Jhc2VsaW5lIGZyb20gXCJAbXVpL21hdGVyaWFsL0Nzc0Jhc2VsaW5lXCI7XG5pbXBvcnQgeyBDYWNoZVByb3ZpZGVyLCBFbW90aW9uQ2FjaGUgfSBmcm9tIFwiQGVtb3Rpb24vcmVhY3RcIjtcbmltcG9ydCB0aGVtZSBmcm9tIFwiLi4vdGhlbWVcIjtcbmltcG9ydCBjcmVhdGVFbW90aW9uQ2FjaGUgZnJvbSBcIi4uL2NyZWF0ZUVtb3Rpb25DYWNoZVwiO1xuaW1wb3J0IFwiLi4vc3R5bGVzL2dsb2JhbHMuY3NzXCI7XG5cbmNvbnN0IGxpZ2h0VGhlbWUgPSBjcmVhdGVUaGVtZSh7XG4gIHBhbGV0dGU6IHtcbiAgICBtb2RlOiBcImxpZ2h0XCIsXG4gIH0sXG59KTtcblxuY29uc3QgZGFya1RoZW1lID0gY3JlYXRlVGhlbWUoe1xuICBwYWxldHRlOiB7XG4gICAgbW9kZTogXCJkYXJrXCIsXG4gIH0sXG59KTtcblxuLy8gQ2xpZW50LXNpZGUgY2FjaGUsIHNoYXJlZCBmb3IgdGhlIHdob2xlIHNlc3Npb24gb2YgdGhlIHVzZXIgaW4gdGhlIGJyb3dzZXIuXG5jb25zdCBjbGllbnRTaWRlRW1vdGlvbkNhY2hlID0gY3JlYXRlRW1vdGlvbkNhY2hlKCk7XG5cbmludGVyZmFjZSBNeUFwcFByb3BzIGV4dGVuZHMgQXBwUHJvcHMge1xuICBlbW90aW9uQ2FjaGU/OiBFbW90aW9uQ2FjaGU7XG59XG5cbmV4cG9ydCBkZWZhdWx0IGZ1bmN0aW9uIE15QXBwKHByb3BzOiBNeUFwcFByb3BzKSB7XG4gIGNvbnN0IHsgQ29tcG9uZW50LCBlbW90aW9uQ2FjaGUgPSBjbGllbnRTaWRlRW1vdGlvbkNhY2hlLCBwYWdlUHJvcHMgfSA9IHByb3BzO1xuICByZXR1cm4gKFxuICAgIDxDYWNoZVByb3ZpZGVyIHZhbHVlPXtlbW90aW9uQ2FjaGV9PlxuICAgICAgPEhlYWQ+XG4gICAgICAgIDxtZXRhIG5hbWU9XCJ2aWV3cG9ydFwiIGNvbnRlbnQ9XCJpbml0aWFsLXNjYWxlPTEsIHdpZHRoPWRldmljZS13aWR0aFwiIC8+XG4gICAgICA8L0hlYWQ+XG4gICAgICA8VGhlbWVQcm92aWRlciB0aGVtZT17ZGFya1RoZW1lfT5cbiAgICAgICAgey8qIENzc0Jhc2VsaW5lIGtpY2tzdGFydCBhbiBlbGVnYW50LCBjb25zaXN0ZW50LCBhbmQgc2ltcGxlIGJhc2VsaW5lIHRvIGJ1aWxkIHVwb24uICovfVxuICAgICAgICA8Q3NzQmFzZWxpbmUgLz5cbiAgICAgICAgPENvbXBvbmVudCB7Li4ucGFnZVByb3BzfSAvPlxuICAgICAgPC9UaGVtZVByb3ZpZGVyPlxuICAgIDwvQ2FjaGVQcm92aWRlcj5cbiAgKTtcbn1cbiJdLCJuYW1lcyI6WyJSZWFjdCIsIkhlYWQiLCJUaGVtZVByb3ZpZGVyIiwiY3JlYXRlVGhlbWUiLCJDc3NCYXNlbGluZSIsIkNhY2hlUHJvdmlkZXIiLCJjcmVhdGVFbW90aW9uQ2FjaGUiLCJsaWdodFRoZW1lIiwicGFsZXR0ZSIsIm1vZGUiLCJkYXJrVGhlbWUiLCJjbGllbnRTaWRlRW1vdGlvbkNhY2hlIiwiTXlBcHAiLCJwcm9wcyIsIkNvbXBvbmVudCIsImVtb3Rpb25DYWNoZSIsInBhZ2VQcm9wcyIsInZhbHVlIiwibWV0YSIsIm5hbWUiLCJjb250ZW50IiwidGhlbWUiXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./src/pages/_app.tsx\n");

/***/ }),

/***/ "./src/styles/globals.css":
/*!********************************!*\
  !*** ./src/styles/globals.css ***!
  \********************************/
/***/ (() => {



/***/ }),

/***/ "@emotion/cache":
/*!*********************************!*\
  !*** external "@emotion/cache" ***!
  \*********************************/
/***/ ((module) => {

"use strict";
module.exports = require("@emotion/cache");

/***/ }),

/***/ "@emotion/react":
/*!*********************************!*\
  !*** external "@emotion/react" ***!
  \*********************************/
/***/ ((module) => {

"use strict";
module.exports = require("@emotion/react");

/***/ }),

/***/ "@mui/material/CssBaseline":
/*!********************************************!*\
  !*** external "@mui/material/CssBaseline" ***!
  \********************************************/
/***/ ((module) => {

"use strict";
module.exports = require("@mui/material/CssBaseline");

/***/ }),

/***/ "@mui/material/styles":
/*!***************************************!*\
  !*** external "@mui/material/styles" ***!
  \***************************************/
/***/ ((module) => {

"use strict";
module.exports = require("@mui/material/styles");

/***/ }),

/***/ "next/head":
/*!****************************!*\
  !*** external "next/head" ***!
  \****************************/
/***/ ((module) => {

"use strict";
module.exports = require("next/head");

/***/ }),

/***/ "react":
/*!************************!*\
  !*** external "react" ***!
  \************************/
/***/ ((module) => {

"use strict";
module.exports = require("react");

/***/ }),

/***/ "react/jsx-dev-runtime":
/*!****************************************!*\
  !*** external "react/jsx-dev-runtime" ***!
  \****************************************/
/***/ ((module) => {

"use strict";
module.exports = require("react/jsx-dev-runtime");

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../webpack-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = (__webpack_exec__("./src/pages/_app.tsx"));
module.exports = __webpack_exports__;

})();