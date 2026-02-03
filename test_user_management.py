from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_user_management_e2e():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)
        admin = AdminPage(page)

        login.login("Admin", "admin123")
        admin.navigate_admin()
        admin.add_user("testuser01")

        browser.close()
