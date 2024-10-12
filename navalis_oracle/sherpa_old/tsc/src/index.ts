import { spawn } from 'child_process';
import { processLabs } from './scrape_url.js';
import { fileURLToPath } from 'url';
import path from 'path';

// Convert the URL to a file path
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const parserPath = path.join(__dirname, '..', '..', 'parse_lab_jsons.py');

const runPythonScript = () => {
  const pythonProcess = spawn('python', [parserPath]);

  pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
      console.log(`child process exited with code ${code}`);
  });
};

processLabs();
// runPythonScript();