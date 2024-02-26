from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    LINK = "https://www.google.com/"
    SEARCH_BOX_SELECTOR = (By.CSS_SELECTOR, 'textarea[title="Поиск"]')
    SUBMIT_QUERY_BUTTON_SELECTOR = (By.CSS_SELECTOR, "div.FPdoLc.lJ9FBc > center > input.gNO89b")
    SUGGESTIONS_ALL_SELECTOR = (By.CSS_SELECTOR, 'ul[role="listbox"] li')
    SUGGESTIONS_NO_ADD_SELECTOR = (By.CSS_SELECTOR, 'ul[role="listbox"] li:not(.sbre)')

    def enter_query(self, text: str) -> None:
        self.find(*SearchPage.SEARCH_BOX_SELECTOR).send_keys(text)

    def submit_query_by_button(self) -> None:
        self.find(*SearchPage.SUBMIT_QUERY_BUTTON_SELECTOR).click()

    def submit_query_by_enter(self) -> None:
        search_box = self.find(*SearchPage.SEARCH_BOX_SELECTOR)

        search_box.send_keys('\n')

    def get_suggestions(
            self,
            no_add: bool = False,
    ) -> list:
        return [
            suggestion.text
            for suggestion in self.find_elements(
                *(
                    SearchPage.SUGGESTIONS_ALL_SELECTOR
                    if not no_add
                    else SearchPage.SUGGESTIONS_NO_ADD_SELECTOR
                )
            )
        ]
