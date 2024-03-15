#asyncronous scipts

#main import to execute the method that is defined async
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless = False)
        page = await browser.new_page()
        await page.goto("https://numpy.org/doc/stable/user/absolute_beginners.html")
        await page.screenshot(path="demo_async.png")

        print(await page.title())
        await browser.close()

#calling the main function here
asyncio.run(main())