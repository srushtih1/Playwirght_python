#page lib used to 
from playwright.sync_api import Page
import pytest

#always use test before every function
#@pytest.mark.skip_browser("chromium")
def test_title(page: Page):
    page.goto("/")
    #assert is from pyTest 
    assert page.title() == "Swag Labs"

@pytest.mark.only_browser("chromium")
def test_inventory_site(page: Page):
    page.goto("/inventory.html")
    #assert is from pyTest 
    assert page.inner_text("h3") == "Epic sadface: You can only access '/inventory.html' when you are logged in."


