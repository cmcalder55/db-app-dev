import fetch from 'node-fetch';
import { JSDOM } from 'jsdom';
import { writeFileSync, mkdirSync, existsSync } from 'fs';
function getUTC() {
    const now = new Date();
    // Build a detailed UTC date and time string manually
    const year = now.getUTCFullYear();
    const month = String(now.getUTCMonth() + 1).padStart(2, '0'); // returns 0-11
    const day = String(now.getUTCDate()).padStart(2, '0');
    const hours = String(now.getUTCHours()).padStart(2, '0');
    const minutes = String(now.getUTCMinutes()).padStart(2, '0');
    const seconds = String(now.getUTCSeconds()).padStart(2, '0');
    return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}
async function scrapeSubmenuData(url, selectors) {
    // Initialize data with an explicit type
    const data = {};
    for (const [labType, selector] of Object.entries(selectors)) {
        try {
            const response = await fetch(url);
            const html = await response.text();
            const dom = new JSDOM(html);
            const document = dom.window.document;
            const submenu = document.querySelector(selector);
            if (!submenu) {
                throw new Error(`Submenu with selector ${selector} not found`);
            }
            const links = Array.from(submenu.querySelectorAll('a'))
                .map(a => a.getAttribute('href'))
                .filter((href) => href !== null);
            data[labType] = links;
        }
        catch (error) {
            console.error(`Error while processing ${labType}:`, error);
        }
    }
    return data;
}
async function scrapeCompassData() {
    const url = 'https://www.poelab.com/everything-labyrinth/';
    const selector = 'p#compassFile';
    const selectors = {
        Normal: '.menu-item-26909',
        Cruel: '.menu-item-26910',
        Merciless: '.menu-item-26911',
        Uber: '.menu-item-26912'
    };
    // Initialize data with an explicit type
    let data = {};
    // get utc date for deciding when to scrape
    data["date"] = getUTC();
    try {
        // get html for each lab type's page
        const labUrls = await scrapeSubmenuData(url, selectors);
        for (const [labType, urls] of Object.entries(labUrls)) {
            for (const url of urls) {
                try {
                    const response = await fetch(url);
                    const html = await response.text();
                    const dom = new JSDOM(html);
                    const document = dom.window.document;
                    // get submenu data
                    const submenu = document.querySelector(selector);
                    if (!submenu) {
                        console.error(`Submenu with selector ${selector} not found`);
                        return;
                    }
                    // Extract links from the submenu
                    const paragraphLinks = Array.from(submenu.querySelectorAll('a'))
                        .map(a => a.getAttribute('href'))
                        .filter((href) => href !== null);
                    // Fetch and store JSON data from each link
                    for (const link of paragraphLinks) {
                        try {
                            const res = await fetch(link);
                            // Check if the response is OK and the content type is JSON
                            if (res.ok && res.headers.get("content-type")?.includes("application/json")) {
                                const jsonData = await res.json();
                                data[labType] = jsonData;
                            }
                            else {
                                console.error(`Non-JSON response from ${link}:`, res.status, res.statusText);
                                // Optionally log res.text() here to see the HTML response
                            }
                        }
                        catch (error) {
                            console.error(`Error fetching JSON from ${link}:`, error);
                        }
                    }
                }
                catch (error) {
                    console.error(`Error while fetching the main URL: ${url}`, error);
                }
            }
            ;
        }
        ;
        return data;
    }
    catch (error) {
        console.error('Error during processing:', error);
    }
}
async function writeToJson(data) {
    const outputFilePath = `./out/compass.json`;
    // Ensure the output directory exists
    const dir = outputFilePath.substring(0, outputFilePath.lastIndexOf('/'));
    if (!existsSync(dir)) {
        mkdirSync(dir, { recursive: true });
    }
    // Write the collected data to the file
    writeFileSync(outputFilePath, JSON.stringify(data, null, 2));
    console.log(`Data written to ${outputFilePath}`);
}
async function processLabs() {
    try {
        // write lab data to json 
        const data = await scrapeCompassData();
        await writeToJson(data);
    }
    catch (error) {
        console.error('Error during processing:', error);
    }
}
export { processLabs };
//# sourceMappingURL=scrape_url.js.map