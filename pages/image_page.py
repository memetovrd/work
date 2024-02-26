from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ImagesPage(BasePage):
    IMAGES_SELECTOR = (By.CLASS_NAME, "rg_i.Q4LuWd")
    OPENNED_IMAGE_SELECTOR = (By.CLASS_NAME, 'sFlh5c.pT0Scc.iPVvYb')
    NEXT_IMAGE_SELECTOR = (By.CSS_SELECTOR, 'button[aria-label="Следующее изображение"]')
    PREVIOUS_IMAGE_SELECTOR = (By.CSS_SELECTOR, 'button[aria-label="Предыдущее изображение"]')
    VIEW_IMAGE_SELECTOR = (By.CSS_SELECTOR, 'div[jsname="CGzTgf"]')

    def get_images_links(self) -> list:
        return [
            link for link in self.find_elements(*ImagesPage.IMAGES_SELECTOR)
        ]

    def next_image(self) -> None:
        self.find_elements(*ImagesPage.NEXT_IMAGE_SELECTOR)[1].click()

    def previous_image(self) -> None:
        self.find_elements(*ImagesPage.PREVIOUS_IMAGE_SELECTOR)[1].click()

    def get_view_image_data(self) -> str:
        return self.find(*ImagesPage.VIEW_IMAGE_SELECTOR).get_attribute('data-tbnid')
