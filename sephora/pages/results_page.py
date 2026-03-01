class ResultsPage:

    def __init__(self,page):
        self.page = page

    def get_text_from_results(self):
        elements = self.page.query_selector_all("[class='product__grid__title gt-p']")
        elements_short= elements[0:5]
        for element in elements_short:
            text = element.inner_text()
            print (text)
            assert "Makeup" in text
        # print ("test end")

        import re

            def __init__(self, page):
                self.page = page
                self.results_count_locator = page.locator(".results-count")

            def get_results_count_for_product(self, product_name):
                self.results_count_locator.wait_for(state="visible")
                text = self.results_count_locator.inner_text()
                match = re.search(r"\d+", text.replace(",", ""))
                total_results = int(match.group()) if match else 0
                print(f"{total_results} Results for “{product_name}”")

                return total_results
