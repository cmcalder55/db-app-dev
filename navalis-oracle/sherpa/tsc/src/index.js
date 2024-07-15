"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var child_process_1 = require("child_process");
var scrape_url_js_1 = require("./scrape_url.js");
var url_1 = require("url");
var path_1 = require("path");
// Convert the URL to a file path
var __filename = (0, url_1.fileURLToPath)(import.meta.url);
var __dirname = path_1.default.dirname(__filename);
var parserPath = path_1.default.join(__dirname, '..', '..', 'parse_lab_jsons.py');
var runPythonScript = function () {
    var pythonProcess = (0, child_process_1.spawn)('python', [parserPath]);
    pythonProcess.stdout.on('data', function (data) {
        console.log("stdout: ".concat(data));
    });
    pythonProcess.stderr.on('data', function (data) {
        console.error("stderr: ".concat(data));
    });
    pythonProcess.on('close', function (code) {
        console.log("child process exited with code ".concat(code));
    });
};
(0, scrape_url_js_1.processLabs)();
// runPythonScript();
