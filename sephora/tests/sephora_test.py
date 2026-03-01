from sephora.pages.welcome_page import welcomePage


class TestSephoraTest():
    def test_search_test(self,setup_playwright_sephora):
        page = setup_playwright_sephora
        page.goto("https://www.sephora.com/")
        welcome_page =welcomePage(page)
        welcome_page.close_popup()
        welcome_page.close_popup_sign_in()
        welcome_page.search_item()
        welcome_page.click_new_tab()
        welcome_page.click_sale_tab()
        print("welcomePage")
        page.pause()




        # def test_search_item_test(self,setup_playwright_project):
    #     page=setup_playwright_project
    #     welcome_page=welcomePage(page)
    #     page.goto("https://www.sephora.com/")
