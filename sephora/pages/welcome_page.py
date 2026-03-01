from fileinput import close


class welcomePage():
    def __init__(self,page):
        self.page=page

    def search_item(self):
        print ("searching for item")
        search_menu=self.page.locator("[id='site_search_input']")
        search_menu.click()
        search_menu.fill("Revlon")
        self.page.keyboard.press("Enter")
        print ("aaa")


    def close_popup(self):
        close_btn = self.page.locator("[class='css-1kna575']")
        close_btn.click()

    def close_popup_sign_in(self):
        close_btn=self.page.locator("[class='css-191rupl e15t7owz0']")
        close_btn.click()
