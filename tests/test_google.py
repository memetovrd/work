from pages.search_page import SearchPage
from pages.search_result_page import SearchResultPage
from pages.images_page import ImagesPage


class TestGoogleSearch:

    @staticmethod
    def test_suggestions(driver, search_word: str = "Совкомбанк") -> None:
        search_page = SearchPage(driver)

        search_page.get(search_page.LINK)

        search_box_presence = search_page.is_element_presented(
            search_page.SEARCH_BOX_SELECTOR
        )

        assert search_box_presence, "Поле поиска отсутствует"

        search_page.enter_query(search_word)

        assert search_page.is_element_presented(
            SearchPage.SUGGESTIONS_ALL_SELECTOR
        ), "Таблица с подсказками отсутствует"

        suggestions = search_page.get_suggestions(no_add=True)

        for suggestion in suggestions:
            if search_word.lower() in suggestion:
                assert True
                break
            else:
                assert False, f"{search_word} отсутствует в подсказках"

    @staticmethod
    def test_search_by_enter(
        driver,
        search_word: str = "Совкомбанк",
        search_url: str = "https://sovcombank.ru",
    ) -> None:
        search_page = SearchPage(driver)

        search_page.get(search_page.LINK)

        search_page.enter_query(search_word)

        search_page.submit_query_by_enter()

        result_page = SearchResultPage(driver)

        result_table_presented = result_page.is_element_presented(
            result_page.RESULT_TABLE_SELECTOR
        )

        assert result_table_presented, "Отсутствует таблица результатов"

        result_urls = result_page.get_result_links()

        assert (
            search_url in result_urls
        ), f"В результатах отсутствует ссылка {search_url}"

    @staticmethod
    def test_search_by_button(
        driver,
        search_word: str = "Совкомбанк",
        search_url: str = "https://sovcombank.ru",
    ) -> None:
        search_page = SearchPage(driver)

        search_page.get(search_page.LINK)

        search_page.enter_query(search_word)

        search_page.submit_query_by_button()

        result_page = SearchResultPage(driver)

        result_table_presented = result_page.is_element_presented(
            result_page.RESULT_TABLE_SELECTOR
        )

        assert result_table_presented, "Отсутствует таблица результатов"

        result_urls = result_page.get_result_links()

        assert (
            search_url in result_urls
        ), f"В результатах отсутствует ссылка {search_url}"


class TestGoogleImages:

    @staticmethod
    def test_images(driver, search_word: str = "Совкомбанк"):
        search_page = SearchPage(driver)

        search_page.get(search_page.LINK)

        search_page.enter_query(search_word)

        search_page.submit_query_by_button()

        search_result_page = SearchResultPage(driver)

        images_button_presented = search_result_page.is_element_presented(
            SearchResultPage.IMAGES_BUTTON_SELECTOR
        )

        assert images_button_presented, 'На странице отсутствует кнопка "Картинки"'

        search_result_page.open_images()

        image_page = ImagesPage(driver)

        images_list = image_page.get_images_links()

        images_list[1].click()

        image_openned = image_page.is_element_presented(
            image_page.OPENNED_IMAGE_SELECTOR
        )

        assert image_openned, "Картинка не открылась"

        first_view_data = image_page.get_view_image_data()

        image_page.next_image()

        second_view_data = image_page.get_view_image_data()

        assert first_view_data != second_view_data, "Картинка не сменилась"

        image_page.previous_image()

        third_image_data = image_page.get_view_image_data()

        assert first_view_data == third_image_data, "Картинка не сменилась"
