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

/***/ "./node_modules/@next/font/google/target.css?{\"path\":\"src/theme.ts\",\"import\":\"Roboto\",\"arguments\":[{\"weight\":[\"300\",\"400\",\"500\",\"700\"],\"subsets\":[\"latin\"],\"display\":\"swap\",\"fallback\":[\"Helvetica\",\"Arial\",\"sans-serif\"]}],\"variableName\":\"roboto\"}":
/*!***********************************************************************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/@next/font/google/target.css?{"path":"src/theme.ts","import":"Roboto","arguments":[{"weight":["300","400","500","700"],"subsets":["latin"],"display":"swap","fallback":["Helvetica","Arial","sans-serif"]}],"variableName":"roboto"} ***!
  \***********************************************************************************************************************************************************************************************************************************************************/
/***/ ((module) => {

eval("// Exports\nmodule.exports = {\n\t\"style\": {\"fontFamily\":\"'__Roboto_f65433', '__Roboto_Fallback_f65433', Helvetica, Arial, sans-serif\",\"fontStyle\":\"normal\"},\n\t\"className\": \"__className_f65433\"\n};\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9ub2RlX21vZHVsZXMvQG5leHQvZm9udC9nb29nbGUvdGFyZ2V0LmNzcz97XCJwYXRoXCI6XCJzcmMvdGhlbWUudHNcIixcImltcG9ydFwiOlwiUm9ib3RvXCIsXCJhcmd1bWVudHNcIjpbe1wid2VpZ2h0XCI6W1wiMzAwXCIsXCI0MDBcIixcIjUwMFwiLFwiNzAwXCJdLFwic3Vic2V0c1wiOltcImxhdGluXCJdLFwiZGlzcGxheVwiOlwic3dhcFwiLFwiZmFsbGJhY2tcIjpbXCJIZWx2ZXRpY2FcIixcIkFyaWFsXCIsXCJzYW5zLXNlcmlmXCJdfV0sXCJ2YXJpYWJsZU5hbWVcIjpcInJvYm90b1wifS5qcyIsIm1hcHBpbmdzIjoiQUFBQTtBQUNBO0FBQ0EsV0FBVyxnSEFBZ0g7QUFDM0g7QUFDQSIsInNvdXJjZXMiOlsid2VicGFjazovL2Zyb250ZW5kLy4vbm9kZV9tb2R1bGVzL0BuZXh0L2ZvbnQvZ29vZ2xlL3RhcmdldC5jc3M/MzIzYiJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBFeHBvcnRzXG5tb2R1bGUuZXhwb3J0cyA9IHtcblx0XCJzdHlsZVwiOiB7XCJmb250RmFtaWx5XCI6XCInX19Sb2JvdG9fZjY1NDMzJywgJ19fUm9ib3RvX0ZhbGxiYWNrX2Y2NTQzMycsIEhlbHZldGljYSwgQXJpYWwsIHNhbnMtc2VyaWZcIixcImZvbnRTdHlsZVwiOlwibm9ybWFsXCJ9LFxuXHRcImNsYXNzTmFtZVwiOiBcIl9fY2xhc3NOYW1lX2Y2NTQzM1wiXG59O1xuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./node_modules/@next/font/google/target.css?{\"path\":\"src/theme.ts\",\"import\":\"Roboto\",\"arguments\":[{\"weight\":[\"300\",\"400\",\"500\",\"700\"],\"subsets\":[\"latin\"],\"display\":\"swap\",\"fallback\":[\"Helvetica\",\"Arial\",\"sans-serif\"]}],\"variableName\":\"roboto\"}\n");

/***/ }),

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
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (/* binding */ MyApp)\n/* harmony export */ });\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-dev-runtime */ \"react/jsx-dev-runtime\");\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ \"react\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var next_head__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! next/head */ \"next/head\");\n/* harmony import */ var next_head__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(next_head__WEBPACK_IMPORTED_MODULE_2__);\n/* harmony import */ var _mui_material_styles__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @mui/material/styles */ \"@mui/material/styles\");\n/* harmony import */ var _mui_material_styles__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_mui_material_styles__WEBPACK_IMPORTED_MODULE_3__);\n/* harmony import */ var _mui_material_CssBaseline__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @mui/material/CssBaseline */ \"@mui/material/CssBaseline\");\n/* harmony import */ var _mui_material_CssBaseline__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_mui_material_CssBaseline__WEBPACK_IMPORTED_MODULE_4__);\n/* harmony import */ var _emotion_react__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @emotion/react */ \"@emotion/react\");\n/* harmony import */ var _emotion_react__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_emotion_react__WEBPACK_IMPORTED_MODULE_5__);\n/* harmony import */ var _theme__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ../theme */ \"./src/theme.ts\");\n/* harmony import */ var _createEmotionCache__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ../createEmotionCache */ \"./src/createEmotionCache.ts\");\n\n\n\n\n\n\n\n\n// Client-side cache, shared for the whole session of the user in the browser.\nconst clientSideEmotionCache = (0,_createEmotionCache__WEBPACK_IMPORTED_MODULE_7__[\"default\"])();\nfunction MyApp(props) {\n    const { Component , emotionCache =clientSideEmotionCache , pageProps  } = props;\n    return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_emotion_react__WEBPACK_IMPORTED_MODULE_5__.CacheProvider, {\n        value: emotionCache,\n        children: [\n            /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)((next_head__WEBPACK_IMPORTED_MODULE_2___default()), {\n                children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"meta\", {\n                    name: \"viewport\",\n                    content: \"initial-scale=1, width=device-width\"\n                }, void 0, false, {\n                    fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n                    lineNumber: 22,\n                    columnNumber: 9\n                }, this)\n            }, void 0, false, {\n                fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n                lineNumber: 21,\n                columnNumber: 7\n            }, this),\n            /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_mui_material_styles__WEBPACK_IMPORTED_MODULE_3__.ThemeProvider, {\n                theme: _theme__WEBPACK_IMPORTED_MODULE_6__[\"default\"],\n                children: [\n                    /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)((_mui_material_CssBaseline__WEBPACK_IMPORTED_MODULE_4___default()), {}, void 0, false, {\n                        fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n                        lineNumber: 26,\n                        columnNumber: 9\n                    }, this),\n                    /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(Component, {\n                        ...pageProps\n                    }, void 0, false, {\n                        fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n                        lineNumber: 27,\n                        columnNumber: 9\n                    }, this)\n                ]\n            }, void 0, true, {\n                fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n                lineNumber: 24,\n                columnNumber: 7\n            }, this)\n        ]\n    }, void 0, true, {\n        fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n        lineNumber: 20,\n        columnNumber: 5\n    }, this);\n}\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcGFnZXMvX2FwcC50c3guanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUErQjtBQUNGO0FBRXdCO0FBQ0Q7QUFDUztBQUNoQztBQUMwQjtBQUV2RCw4RUFBOEU7QUFDOUUsTUFBTU8seUJBQXlCRCwrREFBa0JBO0FBTWxDLFNBQVNFLE1BQU1DLEtBQWlCLEVBQUU7SUFDL0MsTUFBTSxFQUFFQyxVQUFTLEVBQUVDLGNBQWVKLHVCQUFzQixFQUFFSyxVQUFTLEVBQUUsR0FBR0g7SUFDeEUscUJBQ0UsOERBQUNMLHlEQUFhQTtRQUFDUyxPQUFPRjs7MEJBQ3BCLDhEQUFDVixrREFBSUE7MEJBQ0gsNEVBQUNhO29CQUFLQyxNQUFLO29CQUFXQyxTQUFROzs7Ozs7Ozs7OzswQkFFaEMsOERBQUNkLCtEQUFhQTtnQkFBQ0csT0FBT0EsOENBQUtBOztrQ0FFekIsOERBQUNGLGtFQUFXQTs7Ozs7a0NBQ1osOERBQUNPO3dCQUFXLEdBQUdFLFNBQVM7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUloQyxDQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vZnJvbnRlbmQvLi9zcmMvcGFnZXMvX2FwcC50c3g/ZjlkNiJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgKiBhcyBSZWFjdCBmcm9tIFwicmVhY3RcIjtcbmltcG9ydCBIZWFkIGZyb20gXCJuZXh0L2hlYWRcIjtcbmltcG9ydCB7IEFwcFByb3BzIH0gZnJvbSBcIm5leHQvYXBwXCI7XG5pbXBvcnQgeyBUaGVtZVByb3ZpZGVyIH0gZnJvbSBcIkBtdWkvbWF0ZXJpYWwvc3R5bGVzXCI7XG5pbXBvcnQgQ3NzQmFzZWxpbmUgZnJvbSBcIkBtdWkvbWF0ZXJpYWwvQ3NzQmFzZWxpbmVcIjtcbmltcG9ydCB7IENhY2hlUHJvdmlkZXIsIEVtb3Rpb25DYWNoZSB9IGZyb20gXCJAZW1vdGlvbi9yZWFjdFwiO1xuaW1wb3J0IHRoZW1lIGZyb20gXCIuLi90aGVtZVwiO1xuaW1wb3J0IGNyZWF0ZUVtb3Rpb25DYWNoZSBmcm9tIFwiLi4vY3JlYXRlRW1vdGlvbkNhY2hlXCI7XG5cbi8vIENsaWVudC1zaWRlIGNhY2hlLCBzaGFyZWQgZm9yIHRoZSB3aG9sZSBzZXNzaW9uIG9mIHRoZSB1c2VyIGluIHRoZSBicm93c2VyLlxuY29uc3QgY2xpZW50U2lkZUVtb3Rpb25DYWNoZSA9IGNyZWF0ZUVtb3Rpb25DYWNoZSgpO1xuXG5pbnRlcmZhY2UgTXlBcHBQcm9wcyBleHRlbmRzIEFwcFByb3BzIHtcbiAgZW1vdGlvbkNhY2hlPzogRW1vdGlvbkNhY2hlO1xufVxuXG5leHBvcnQgZGVmYXVsdCBmdW5jdGlvbiBNeUFwcChwcm9wczogTXlBcHBQcm9wcykge1xuICBjb25zdCB7IENvbXBvbmVudCwgZW1vdGlvbkNhY2hlID0gY2xpZW50U2lkZUVtb3Rpb25DYWNoZSwgcGFnZVByb3BzIH0gPSBwcm9wcztcbiAgcmV0dXJuIChcbiAgICA8Q2FjaGVQcm92aWRlciB2YWx1ZT17ZW1vdGlvbkNhY2hlfT5cbiAgICAgIDxIZWFkPlxuICAgICAgICA8bWV0YSBuYW1lPVwidmlld3BvcnRcIiBjb250ZW50PVwiaW5pdGlhbC1zY2FsZT0xLCB3aWR0aD1kZXZpY2Utd2lkdGhcIiAvPlxuICAgICAgPC9IZWFkPlxuICAgICAgPFRoZW1lUHJvdmlkZXIgdGhlbWU9e3RoZW1lfT5cbiAgICAgICAgey8qIENzc0Jhc2VsaW5lIGtpY2tzdGFydCBhbiBlbGVnYW50LCBjb25zaXN0ZW50LCBhbmQgc2ltcGxlIGJhc2VsaW5lIHRvIGJ1aWxkIHVwb24uICovfVxuICAgICAgICA8Q3NzQmFzZWxpbmUgLz5cbiAgICAgICAgPENvbXBvbmVudCB7Li4ucGFnZVByb3BzfSAvPlxuICAgICAgPC9UaGVtZVByb3ZpZGVyPlxuICAgIDwvQ2FjaGVQcm92aWRlcj5cbiAgKTtcbn1cbiJdLCJuYW1lcyI6WyJSZWFjdCIsIkhlYWQiLCJUaGVtZVByb3ZpZGVyIiwiQ3NzQmFzZWxpbmUiLCJDYWNoZVByb3ZpZGVyIiwidGhlbWUiLCJjcmVhdGVFbW90aW9uQ2FjaGUiLCJjbGllbnRTaWRlRW1vdGlvbkNhY2hlIiwiTXlBcHAiLCJwcm9wcyIsIkNvbXBvbmVudCIsImVtb3Rpb25DYWNoZSIsInBhZ2VQcm9wcyIsInZhbHVlIiwibWV0YSIsIm5hbWUiLCJjb250ZW50Il0sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./src/pages/_app.tsx\n");

/***/ }),

/***/ "./src/theme.ts":
/*!**********************!*\
  !*** ./src/theme.ts ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__),\n/* harmony export */   \"roboto\": () => (/* reexport default from dynamic */ _next_font_google_target_css_path_src_theme_ts_import_Roboto_arguments_weight_300_400_500_700_subsets_latin_display_swap_fallback_Helvetica_Arial_sans_serif_variableName_roboto___WEBPACK_IMPORTED_MODULE_2___default.a)\n/* harmony export */ });\n/* harmony import */ var _next_font_google_target_css_path_src_theme_ts_import_Roboto_arguments_weight_300_400_500_700_subsets_latin_display_swap_fallback_Helvetica_Arial_sans_serif_variableName_roboto___WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @next/font/google/target.css?{\"path\":\"src/theme.ts\",\"import\":\"Roboto\",\"arguments\":[{\"weight\":[\"300\",\"400\",\"500\",\"700\"],\"subsets\":[\"latin\"],\"display\":\"swap\",\"fallback\":[\"Helvetica\",\"Arial\",\"sans-serif\"]}],\"variableName\":\"roboto\"} */ \"./node_modules/@next/font/google/target.css?{\\\"path\\\":\\\"src/theme.ts\\\",\\\"import\\\":\\\"Roboto\\\",\\\"arguments\\\":[{\\\"weight\\\":[\\\"300\\\",\\\"400\\\",\\\"500\\\",\\\"700\\\"],\\\"subsets\\\":[\\\"latin\\\"],\\\"display\\\":\\\"swap\\\",\\\"fallback\\\":[\\\"Helvetica\\\",\\\"Arial\\\",\\\"sans-serif\\\"]}],\\\"variableName\\\":\\\"roboto\\\"}\");\n/* harmony import */ var _next_font_google_target_css_path_src_theme_ts_import_Roboto_arguments_weight_300_400_500_700_subsets_latin_display_swap_fallback_Helvetica_Arial_sans_serif_variableName_roboto___WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_next_font_google_target_css_path_src_theme_ts_import_Roboto_arguments_weight_300_400_500_700_subsets_latin_display_swap_fallback_Helvetica_Arial_sans_serif_variableName_roboto___WEBPACK_IMPORTED_MODULE_2__);\n/* harmony import */ var _mui_material_styles__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @mui/material/styles */ \"@mui/material/styles\");\n/* harmony import */ var _mui_material_styles__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_mui_material_styles__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var _mui_material_colors__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @mui/material/colors */ \"@mui/material/colors\");\n/* harmony import */ var _mui_material_colors__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_mui_material_colors__WEBPACK_IMPORTED_MODULE_1__);\n\n\n\n// Create a theme instance.\nconst theme = (0,_mui_material_styles__WEBPACK_IMPORTED_MODULE_0__.createTheme)({\n    palette: {\n        primary: {\n            main: \"#556cd6\"\n        },\n        secondary: {\n            main: \"#19857b\"\n        },\n        error: {\n            main: _mui_material_colors__WEBPACK_IMPORTED_MODULE_1__.red.A400\n        }\n    },\n    typography: {\n        fontFamily: (_next_font_google_target_css_path_src_theme_ts_import_Roboto_arguments_weight_300_400_500_700_subsets_latin_display_swap_fallback_Helvetica_Arial_sans_serif_variableName_roboto___WEBPACK_IMPORTED_MODULE_2___default().style.fontFamily)\n    }\n});\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (theme);\n\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvdGhlbWUudHMuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7QUFJYUE7QUFIc0M7QUFDUjtBQVMzQywyQkFBMkI7QUFDM0IsTUFBTUcsUUFBUUYsaUVBQVdBLENBQUM7SUFDeEJHLFNBQVM7UUFDUEMsU0FBUztZQUNQQyxNQUFNO1FBQ1I7UUFDQUMsV0FBVztZQUNURCxNQUFNO1FBQ1I7UUFDQUUsT0FBTztZQUNMRixNQUFNSiwwREFBUTtRQUNoQjtJQUNGO0lBQ0FRLFlBQVk7UUFDVkMsWUFBWVgsMk9BQXVCO0lBQ3JDO0FBQ0Y7QUFFQSxpRUFBZUcsS0FBS0EsRUFBQztBQXpCUkgiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9mcm9udGVuZC8uL3NyYy90aGVtZS50cz9kYzlhIl0sInNvdXJjZXNDb250ZW50IjpbImltcG9ydCB7IFJvYm90byB9IGZyb20gJ0BuZXh0L2ZvbnQvZ29vZ2xlJztcbmltcG9ydCB7IGNyZWF0ZVRoZW1lIH0gZnJvbSAnQG11aS9tYXRlcmlhbC9zdHlsZXMnO1xuaW1wb3J0IHsgcmVkIH0gZnJvbSAnQG11aS9tYXRlcmlhbC9jb2xvcnMnO1xuXG5leHBvcnQgY29uc3Qgcm9ib3RvID0gUm9ib3RvKHtcbiAgd2VpZ2h0OiBbJzMwMCcsICc0MDAnLCAnNTAwJywgJzcwMCddLFxuICBzdWJzZXRzOiBbJ2xhdGluJ10sXG4gIGRpc3BsYXk6ICdzd2FwJyxcbiAgZmFsbGJhY2s6IFsnSGVsdmV0aWNhJywgJ0FyaWFsJywgJ3NhbnMtc2VyaWYnXSxcbn0pO1xuXG4vLyBDcmVhdGUgYSB0aGVtZSBpbnN0YW5jZS5cbmNvbnN0IHRoZW1lID0gY3JlYXRlVGhlbWUoe1xuICBwYWxldHRlOiB7XG4gICAgcHJpbWFyeToge1xuICAgICAgbWFpbjogJyM1NTZjZDYnLFxuICAgIH0sXG4gICAgc2Vjb25kYXJ5OiB7XG4gICAgICBtYWluOiAnIzE5ODU3YicsXG4gICAgfSxcbiAgICBlcnJvcjoge1xuICAgICAgbWFpbjogcmVkLkE0MDAsXG4gICAgfSxcbiAgfSxcbiAgdHlwb2dyYXBoeToge1xuICAgIGZvbnRGYW1pbHk6IHJvYm90by5zdHlsZS5mb250RmFtaWx5LFxuICB9LFxufSk7XG5cbmV4cG9ydCBkZWZhdWx0IHRoZW1lO1xuIl0sIm5hbWVzIjpbInJvYm90byIsImNyZWF0ZVRoZW1lIiwicmVkIiwidGhlbWUiLCJwYWxldHRlIiwicHJpbWFyeSIsIm1haW4iLCJzZWNvbmRhcnkiLCJlcnJvciIsIkE0MDAiLCJ0eXBvZ3JhcGh5IiwiZm9udEZhbWlseSIsInN0eWxlIl0sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./src/theme.ts\n");

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

/***/ "@mui/material/colors":
/*!***************************************!*\
  !*** external "@mui/material/colors" ***!
  \***************************************/
/***/ ((module) => {

"use strict";
module.exports = require("@mui/material/colors");

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