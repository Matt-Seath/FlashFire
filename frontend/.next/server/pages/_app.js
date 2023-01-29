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
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (/* binding */ MyApp)\n/* harmony export */ });\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-dev-runtime */ \"react/jsx-dev-runtime\");\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ \"react\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var next_head__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! next/head */ \"next/head\");\n/* harmony import */ var next_head__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(next_head__WEBPACK_IMPORTED_MODULE_2__);\n/* harmony import */ var _mui_material_styles__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @mui/material/styles */ \"@mui/material/styles\");\n/* harmony import */ var _mui_material_styles__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_mui_material_styles__WEBPACK_IMPORTED_MODULE_3__);\n/* harmony import */ var _mui_material_CssBaseline__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @mui/material/CssBaseline */ \"@mui/material/CssBaseline\");\n/* harmony import */ var _mui_material_CssBaseline__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_mui_material_CssBaseline__WEBPACK_IMPORTED_MODULE_4__);\n/* harmony import */ var _emotion_react__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @emotion/react */ \"@emotion/react\");\n/* harmony import */ var _emotion_react__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_emotion_react__WEBPACK_IMPORTED_MODULE_5__);\n/* harmony import */ var _createEmotionCache__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ../createEmotionCache */ \"./src/createEmotionCache.ts\");\n/* harmony import */ var _styles_globals_css__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ../styles/globals.css */ \"./src/styles/globals.css\");\n/* harmony import */ var _styles_globals_css__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_styles_globals_css__WEBPACK_IMPORTED_MODULE_7__);\n\n\n\n\n\n\n\n\n\nconst lightTheme = (0,_mui_material_styles__WEBPACK_IMPORTED_MODULE_3__.createTheme)({\n    palette: {\n        mode: \"light\"\n    }\n});\nconst darkTheme = (0,_mui_material_styles__WEBPACK_IMPORTED_MODULE_3__.createTheme)({\n    palette: {\n        mode: \"dark\"\n    }\n});\nfunction getActiveTheme(themeMode) {\n    return themeMode === \"light\" ? lightTheme : darkTheme;\n}\n// Client-side cache, shared for the whole session of the user in the browser.\nconst clientSideEmotionCache = (0,_createEmotionCache__WEBPACK_IMPORTED_MODULE_6__[\"default\"])();\nfunction MyApp(props) {\n    const { Component , emotionCache =clientSideEmotionCache , pageProps  } = props;\n    const [activeTheme, setActiveTheme] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(lightTheme);\n    const [selectedTheme, setSelectedTheme] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(\"light\");\n    const toggleTheme = ()=>{\n        const desiredTheme = selectedTheme === \"light\" ? \"dark\" : \"light\";\n        setSelectedTheme(desiredTheme);\n    };\n    (0,react__WEBPACK_IMPORTED_MODULE_1__.useEffect)(()=>{\n        setActiveTheme(getActiveTheme(selectedTheme));\n    }, [\n        selectedTheme\n    ]);\n    return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_emotion_react__WEBPACK_IMPORTED_MODULE_5__.CacheProvider, {\n        value: emotionCache,\n        children: [\n            /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)((next_head__WEBPACK_IMPORTED_MODULE_2___default()), {\n                children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"meta\", {\n                    name: \"viewport\",\n                    content: \"initial-scale=1, width=device-width\"\n                }, void 0, false, {\n                    fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n                    lineNumber: 52,\n                    columnNumber: 9\n                }, this)\n            }, void 0, false, {\n                fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n                lineNumber: 51,\n                columnNumber: 7\n            }, this),\n            /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_mui_material_styles__WEBPACK_IMPORTED_MODULE_3__.ThemeProvider, {\n                theme: darkTheme,\n                children: [\n                    /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)((_mui_material_CssBaseline__WEBPACK_IMPORTED_MODULE_4___default()), {}, void 0, false, {\n                        fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n                        lineNumber: 55,\n                        columnNumber: 9\n                    }, this),\n                    /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(Component, {\n                        ...pageProps,\n                        toggleTheme: toggleTheme\n                    }, void 0, false, {\n                        fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n                        lineNumber: 56,\n                        columnNumber: 9\n                    }, this)\n                ]\n            }, void 0, true, {\n                fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n                lineNumber: 54,\n                columnNumber: 7\n            }, this)\n        ]\n    }, void 0, true, {\n        fileName: \"/home/seath/Projects/FlashFire/frontend/src/pages/_app.tsx\",\n        lineNumber: 50,\n        columnNumber: 5\n    }, this);\n}\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcGFnZXMvX2FwcC50c3guanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBK0I7QUFDYTtBQUNmO0FBRXFDO0FBQ2Q7QUFDUztBQUVOO0FBQ3hCO0FBRS9CLE1BQU1TLGFBQWFKLGlFQUFXQSxDQUFDO0lBQzdCSyxTQUFTO1FBQ1BDLE1BQU07SUFDUjtBQUNGO0FBRUEsTUFBTUMsWUFBWVAsaUVBQVdBLENBQUM7SUFDNUJLLFNBQVM7UUFDUEMsTUFBTTtJQUNSO0FBQ0Y7QUFFQSxTQUFTRSxlQUFlQyxTQUEyQixFQUFFO0lBQ25ELE9BQU9BLGNBQWMsVUFBVUwsYUFBYUcsU0FBUztBQUN2RDtBQUVBLDhFQUE4RTtBQUM5RSxNQUFNRyx5QkFBeUJQLCtEQUFrQkE7QUFNbEMsU0FBU1EsTUFBTUMsS0FBaUIsRUFBRTtJQUMvQyxNQUFNLEVBQUVDLFVBQVMsRUFBRUMsY0FBZUosdUJBQXNCLEVBQUVLLFVBQVMsRUFBRSxHQUFHSDtJQUN4RSxNQUFNLENBQUNJLGFBQWFDLGVBQWUsR0FBR3BCLCtDQUFRQSxDQUFDTztJQUMvQyxNQUFNLENBQUNjLGVBQWVDLGlCQUFpQixHQUFHdEIsK0NBQVFBLENBQW1CO0lBRXJFLE1BQU11QixjQUEwRCxJQUFNO1FBQ3BFLE1BQU1DLGVBQWVILGtCQUFrQixVQUFVLFNBQVMsT0FBTztRQUVqRUMsaUJBQWlCRTtJQUNuQjtJQUVBekIsZ0RBQVNBLENBQUMsSUFBTTtRQUNkcUIsZUFBZVQsZUFBZVU7SUFDaEMsR0FBRztRQUFDQTtLQUFjO0lBQ2xCLHFCQUNFLDhEQUFDaEIseURBQWFBO1FBQUNvQixPQUFPUjs7MEJBQ3BCLDhEQUFDaEIsa0RBQUlBOzBCQUNILDRFQUFDeUI7b0JBQUtDLE1BQUs7b0JBQVdDLFNBQVE7Ozs7Ozs7Ozs7OzBCQUVoQyw4REFBQzFCLCtEQUFhQTtnQkFBQzJCLE9BQU9uQjs7a0NBQ3BCLDhEQUFDTixrRUFBV0E7Ozs7O2tDQUNaLDhEQUFDWTt3QkFBVyxHQUFHRSxTQUFTO3dCQUFFSyxhQUFhQTs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBTS9DLENBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9mcm9udGVuZC8uL3NyYy9wYWdlcy9fYXBwLnRzeD9mOWQ2Il0sInNvdXJjZXNDb250ZW50IjpbImltcG9ydCAqIGFzIFJlYWN0IGZyb20gXCJyZWFjdFwiO1xuaW1wb3J0IHsgdXNlRWZmZWN0LCB1c2VTdGF0ZSB9IGZyb20gXCJyZWFjdFwiO1xuaW1wb3J0IEhlYWQgZnJvbSBcIm5leHQvaGVhZFwiO1xuaW1wb3J0IHsgQXBwUHJvcHMgfSBmcm9tIFwibmV4dC9hcHBcIjtcbmltcG9ydCB7IFRoZW1lUHJvdmlkZXIsIGNyZWF0ZVRoZW1lIH0gZnJvbSBcIkBtdWkvbWF0ZXJpYWwvc3R5bGVzXCI7XG5pbXBvcnQgQ3NzQmFzZWxpbmUgZnJvbSBcIkBtdWkvbWF0ZXJpYWwvQ3NzQmFzZWxpbmVcIjtcbmltcG9ydCB7IENhY2hlUHJvdmlkZXIsIEVtb3Rpb25DYWNoZSB9IGZyb20gXCJAZW1vdGlvbi9yZWFjdFwiO1xuaW1wb3J0IHRoZW1lIGZyb20gXCIuLi90aGVtZVwiO1xuaW1wb3J0IGNyZWF0ZUVtb3Rpb25DYWNoZSBmcm9tIFwiLi4vY3JlYXRlRW1vdGlvbkNhY2hlXCI7XG5pbXBvcnQgXCIuLi9zdHlsZXMvZ2xvYmFscy5jc3NcIjtcblxuY29uc3QgbGlnaHRUaGVtZSA9IGNyZWF0ZVRoZW1lKHtcbiAgcGFsZXR0ZToge1xuICAgIG1vZGU6IFwibGlnaHRcIixcbiAgfSxcbn0pO1xuXG5jb25zdCBkYXJrVGhlbWUgPSBjcmVhdGVUaGVtZSh7XG4gIHBhbGV0dGU6IHtcbiAgICBtb2RlOiBcImRhcmtcIixcbiAgfSxcbn0pO1xuXG5mdW5jdGlvbiBnZXRBY3RpdmVUaGVtZSh0aGVtZU1vZGU6IFwibGlnaHRcIiB8IFwiZGFya1wiKSB7XG4gIHJldHVybiB0aGVtZU1vZGUgPT09IFwibGlnaHRcIiA/IGxpZ2h0VGhlbWUgOiBkYXJrVGhlbWU7XG59XG5cbi8vIENsaWVudC1zaWRlIGNhY2hlLCBzaGFyZWQgZm9yIHRoZSB3aG9sZSBzZXNzaW9uIG9mIHRoZSB1c2VyIGluIHRoZSBicm93c2VyLlxuY29uc3QgY2xpZW50U2lkZUVtb3Rpb25DYWNoZSA9IGNyZWF0ZUVtb3Rpb25DYWNoZSgpO1xuXG5pbnRlcmZhY2UgTXlBcHBQcm9wcyBleHRlbmRzIEFwcFByb3BzIHtcbiAgZW1vdGlvbkNhY2hlPzogRW1vdGlvbkNhY2hlO1xufVxuXG5leHBvcnQgZGVmYXVsdCBmdW5jdGlvbiBNeUFwcChwcm9wczogTXlBcHBQcm9wcykge1xuICBjb25zdCB7IENvbXBvbmVudCwgZW1vdGlvbkNhY2hlID0gY2xpZW50U2lkZUVtb3Rpb25DYWNoZSwgcGFnZVByb3BzIH0gPSBwcm9wcztcbiAgY29uc3QgW2FjdGl2ZVRoZW1lLCBzZXRBY3RpdmVUaGVtZV0gPSB1c2VTdGF0ZShsaWdodFRoZW1lKTtcbiAgY29uc3QgW3NlbGVjdGVkVGhlbWUsIHNldFNlbGVjdGVkVGhlbWVdID0gdXNlU3RhdGU8XCJsaWdodFwiIHwgXCJkYXJrXCI+KFwibGlnaHRcIik7XG5cbiAgY29uc3QgdG9nZ2xlVGhlbWU6IFJlYWN0Lk1vdXNlRXZlbnRIYW5kbGVyPEhUTUxBbmNob3JFbGVtZW50PiA9ICgpID0+IHtcbiAgICBjb25zdCBkZXNpcmVkVGhlbWUgPSBzZWxlY3RlZFRoZW1lID09PSBcImxpZ2h0XCIgPyBcImRhcmtcIiA6IFwibGlnaHRcIjtcblxuICAgIHNldFNlbGVjdGVkVGhlbWUoZGVzaXJlZFRoZW1lKTtcbiAgfTtcblxuICB1c2VFZmZlY3QoKCkgPT4ge1xuICAgIHNldEFjdGl2ZVRoZW1lKGdldEFjdGl2ZVRoZW1lKHNlbGVjdGVkVGhlbWUpKTtcbiAgfSwgW3NlbGVjdGVkVGhlbWVdKTtcbiAgcmV0dXJuIChcbiAgICA8Q2FjaGVQcm92aWRlciB2YWx1ZT17ZW1vdGlvbkNhY2hlfT5cbiAgICAgIDxIZWFkPlxuICAgICAgICA8bWV0YSBuYW1lPVwidmlld3BvcnRcIiBjb250ZW50PVwiaW5pdGlhbC1zY2FsZT0xLCB3aWR0aD1kZXZpY2Utd2lkdGhcIiAvPlxuICAgICAgPC9IZWFkPlxuICAgICAgPFRoZW1lUHJvdmlkZXIgdGhlbWU9e2RhcmtUaGVtZX0+XG4gICAgICAgIDxDc3NCYXNlbGluZSAvPlxuICAgICAgICA8Q29tcG9uZW50IHsuLi5wYWdlUHJvcHN9IHRvZ2dsZVRoZW1lPXt0b2dnbGVUaGVtZX0gLz5cblxuICAgICAgICB7LyogQ3NzQmFzZWxpbmUga2lja3N0YXJ0IGFuIGVsZWdhbnQsIGNvbnNpc3RlbnQsIGFuZCBzaW1wbGUgYmFzZWxpbmUgdG8gYnVpbGQgdXBvbi4gKi99XG4gICAgICA8L1RoZW1lUHJvdmlkZXI+XG4gICAgPC9DYWNoZVByb3ZpZGVyPlxuICApO1xufVxuIl0sIm5hbWVzIjpbIlJlYWN0IiwidXNlRWZmZWN0IiwidXNlU3RhdGUiLCJIZWFkIiwiVGhlbWVQcm92aWRlciIsImNyZWF0ZVRoZW1lIiwiQ3NzQmFzZWxpbmUiLCJDYWNoZVByb3ZpZGVyIiwiY3JlYXRlRW1vdGlvbkNhY2hlIiwibGlnaHRUaGVtZSIsInBhbGV0dGUiLCJtb2RlIiwiZGFya1RoZW1lIiwiZ2V0QWN0aXZlVGhlbWUiLCJ0aGVtZU1vZGUiLCJjbGllbnRTaWRlRW1vdGlvbkNhY2hlIiwiTXlBcHAiLCJwcm9wcyIsIkNvbXBvbmVudCIsImVtb3Rpb25DYWNoZSIsInBhZ2VQcm9wcyIsImFjdGl2ZVRoZW1lIiwic2V0QWN0aXZlVGhlbWUiLCJzZWxlY3RlZFRoZW1lIiwic2V0U2VsZWN0ZWRUaGVtZSIsInRvZ2dsZVRoZW1lIiwiZGVzaXJlZFRoZW1lIiwidmFsdWUiLCJtZXRhIiwibmFtZSIsImNvbnRlbnQiLCJ0aGVtZSJdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./src/pages/_app.tsx\n");

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