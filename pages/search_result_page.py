import re
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchResultPage(BasePage):
    RESULT_TABLE_SELECTOR = (By.CSS_SELECTOR, 'div[role="main"]')
    RESULT_LINKS_SELECTOR = (By.CSS_SELECTOR, "cite")
    IMAGES_BUTTON_SELECTOR = (By.XPATH, '//span[contains(text(),"Картинки")]')

    def get_result_links(self) -> list:
        return [
            link.text
            for link in self.find_elements(*SearchResultPage.RESULT_LINKS_SELECTOR)
            if SearchResultPage.is_url(link.text)
        ]

    @staticmethod
    def is_url(url) -> bool:
        pattern = r"^(http|https):\/\/([\w.-]+)(\.[\w.-]+)+([\/\w\.-]*)*\/?$"
        return bool(re.match(pattern, url))

    def open_images(self) -> None:
        images_button = self.find(*SearchResultPage.IMAGES_BUTTON_SELECTOR)
        images_button.click()
