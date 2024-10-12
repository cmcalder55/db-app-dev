"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.processLabs = void 0;
var node_fetch_1 = require("node-fetch");
var jsdom_1 = require("jsdom");
var fs_1 = require("fs");
function getUTC() {
    var now = new Date();
    // Build a detailed UTC date and time string manually
    var year = now.getUTCFullYear();
    var month = String(now.getUTCMonth() + 1).padStart(2, '0'); // returns 0-11
    var day = String(now.getUTCDate()).padStart(2, '0');
    var hours = String(now.getUTCHours()).padStart(2, '0');
    var minutes = String(now.getUTCMinutes()).padStart(2, '0');
    var seconds = String(now.getUTCSeconds()).padStart(2, '0');
    return "".concat(year, "-").concat(month, "-").concat(day, " ").concat(hours, ":").concat(minutes, ":").concat(seconds);
}
function scrapeSubmenuData(url, selectors) {
    return __awaiter(this, void 0, void 0, function () {
        var data, _i, _a, _b, labType, selector, response, html, dom, document_1, submenu, links, error_1;
        return __generator(this, function (_c) {
            switch (_c.label) {
                case 0:
                    data = {};
                    _i = 0, _a = Object.entries(selectors);
                    _c.label = 1;
                case 1:
                    if (!(_i < _a.length)) return [3 /*break*/, 7];
                    _b = _a[_i], labType = _b[0], selector = _b[1];
                    _c.label = 2;
                case 2:
                    _c.trys.push([2, 5, , 6]);
                    return [4 /*yield*/, (0, node_fetch_1.default)(url)];
                case 3:
                    response = _c.sent();
                    return [4 /*yield*/, response.text()];
                case 4:
                    html = _c.sent();
                    dom = new jsdom_1.JSDOM(html);
                    document_1 = dom.window.document;
                    submenu = document_1.querySelector(selector);
                    if (!submenu) {
                        throw new Error("Submenu with selector ".concat(selector, " not found"));
                    }
                    links = Array.from(submenu.querySelectorAll('a'))
                        .map(function (a) { return a.getAttribute('href'); })
                        .filter(function (href) { return href !== null; });
                    data[labType] = links;
                    return [3 /*break*/, 6];
                case 5:
                    error_1 = _c.sent();
                    console.error("Error while processing ".concat(labType, ":"), error_1);
                    return [3 /*break*/, 6];
                case 6:
                    _i++;
                    return [3 /*break*/, 1];
                case 7: return [2 /*return*/, data];
            }
        });
    });
}
function scrapeCompassData() {
    var _a;
    return __awaiter(this, void 0, void 0, function () {
        var url, selector, selectors, data, labUrls, _i, _b, _c, labType, urls, _d, urls_1, url_1, response, html, dom, document_2, submenu, paragraphLinks, _e, paragraphLinks_1, link, res, jsonData, error_2, error_3, error_4;
        return __generator(this, function (_f) {
            switch (_f.label) {
                case 0:
                    url = 'https://www.poelab.com/everything-labyrinth/';
                    selector = 'p#compassFile';
                    selectors = {
                        Normal: '.menu-item-26909',
                        Cruel: '.menu-item-26910',
                        Merciless: '.menu-item-26911',
                        Uber: '.menu-item-26912'
                    };
                    data = {};
                    // get utc date for deciding when to scrape
                    data["date"] = getUTC();
                    _f.label = 1;
                case 1:
                    _f.trys.push([1, 22, , 23]);
                    return [4 /*yield*/, scrapeSubmenuData(url, selectors)];
                case 2:
                    labUrls = _f.sent();
                    _i = 0, _b = Object.entries(labUrls);
                    _f.label = 3;
                case 3:
                    if (!(_i < _b.length)) return [3 /*break*/, 21];
                    _c = _b[_i], labType = _c[0], urls = _c[1];
                    _d = 0, urls_1 = urls;
                    _f.label = 4;
                case 4:
                    if (!(_d < urls_1.length)) return [3 /*break*/, 19];
                    url_1 = urls_1[_d];
                    _f.label = 5;
                case 5:
                    _f.trys.push([5, 17, , 18]);
                    return [4 /*yield*/, (0, node_fetch_1.default)(url_1)];
                case 6:
                    response = _f.sent();
                    return [4 /*yield*/, response.text()];
                case 7:
                    html = _f.sent();
                    dom = new jsdom_1.JSDOM(html);
                    document_2 = dom.window.document;
                    submenu = document_2.querySelector(selector);
                    if (!submenu) {
                        console.error("Submenu with selector ".concat(selector, " not found"));
                        return [2 /*return*/];
                    }
                    paragraphLinks = Array.from(submenu.querySelectorAll('a'))
                        .map(function (a) { return a.getAttribute('href'); })
                        .filter(function (href) { return href !== null; });
                    _e = 0, paragraphLinks_1 = paragraphLinks;
                    _f.label = 8;
                case 8:
                    if (!(_e < paragraphLinks_1.length)) return [3 /*break*/, 16];
                    link = paragraphLinks_1[_e];
                    _f.label = 9;
                case 9:
                    _f.trys.push([9, 14, , 15]);
                    return [4 /*yield*/, (0, node_fetch_1.default)(link)];
                case 10:
                    res = _f.sent();
                    if (!(res.ok && ((_a = res.headers.get("content-type")) === null || _a === void 0 ? void 0 : _a.includes("application/json")))) return [3 /*break*/, 12];
                    return [4 /*yield*/, res.json()];
                case 11:
                    jsonData = _f.sent();
                    data[labType] = jsonData;
                    return [3 /*break*/, 13];
                case 12:
                    console.error("Non-JSON response from ".concat(link, ":"), res.status, res.statusText);
                    _f.label = 13;
                case 13: return [3 /*break*/, 15];
                case 14:
                    error_2 = _f.sent();
                    console.error("Error fetching JSON from ".concat(link, ":"), error_2);
                    return [3 /*break*/, 15];
                case 15:
                    _e++;
                    return [3 /*break*/, 8];
                case 16: return [3 /*break*/, 18];
                case 17:
                    error_3 = _f.sent();
                    console.error("Error while fetching the main URL: ".concat(url_1), error_3);
                    return [3 /*break*/, 18];
                case 18:
                    _d++;
                    return [3 /*break*/, 4];
                case 19:
                    ;
                    _f.label = 20;
                case 20:
                    _i++;
                    return [3 /*break*/, 3];
                case 21:
                    ;
                    return [2 /*return*/, data];
                case 22:
                    error_4 = _f.sent();
                    console.error('Error during processing:', error_4);
                    return [3 /*break*/, 23];
                case 23: return [2 /*return*/];
            }
        });
    });
}
function writeToJson(data) {
    return __awaiter(this, void 0, void 0, function () {
        var outputFilePath, dir;
        return __generator(this, function (_a) {
            outputFilePath = "./out/compass.json";
            dir = outputFilePath.substring(0, outputFilePath.lastIndexOf('/'));
            if (!(0, fs_1.existsSync)(dir)) {
                (0, fs_1.mkdirSync)(dir, { recursive: true });
            }
            // Write the collected data to the file
            (0, fs_1.writeFileSync)(outputFilePath, JSON.stringify(data, null, 2));
            console.log("Data written to ".concat(outputFilePath));
            return [2 /*return*/];
        });
    });
}
function processLabs() {
    return __awaiter(this, void 0, void 0, function () {
        var data, error_5;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    _a.trys.push([0, 3, , 4]);
                    return [4 /*yield*/, scrapeCompassData()];
                case 1:
                    data = _a.sent();
                    return [4 /*yield*/, writeToJson(data)];
                case 2:
                    _a.sent();
                    return [3 /*break*/, 4];
                case 3:
                    error_5 = _a.sent();
                    console.error('Error during processing:', error_5);
                    return [3 /*break*/, 4];
                case 4: return [2 /*return*/];
            }
        });
    });
}
exports.processLabs = processLabs;
