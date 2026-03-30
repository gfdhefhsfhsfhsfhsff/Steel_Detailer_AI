@echo off
echo Installing SDS2 Documentation Scraper dependencies...
call npm install
echo Installing Playwright Chromium browser...
npx playwright install chromium
echo.
echo Setup complete. Run "node scraper.js" to start the scraper.
pause
