#syncronous scipts

from playwright.sync_api import sync_playwright

#use import with alais p
with sync_playwright() as p:
    #setup which browser to use and headless false to see the browser
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    #the page url we want to go to
    page.goto("https://whatsmyuseragent.org/")
    #name of the screenshot
    page.screenshot(path="demo_sync.png")
    browser.close()
