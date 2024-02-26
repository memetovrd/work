from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    LINK = ""

    def __init__(self, driver):
        self.driver = driver

    def get(self, url, timeout: int = 10) -> None:
        self.driver.get(url)
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def is_element_presented(self, *locator, time: int = 10) -> bool:
        try:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(*locator)
            )
            return True
        except TimeoutException:
            return False

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator) -> list:
        return self.driver.find_elements(*locator)
