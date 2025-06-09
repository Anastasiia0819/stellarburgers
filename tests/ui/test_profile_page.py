import pytest
from selenium import webdriver
from config.config import Config
import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage


class TestMainPage:

    @allure.title("Переход на страницу Конструктор (главная)")
    def test_open_constructor_page(self, driver, create_and_delete_user, login):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        feed_page.wait_title()
        assert feed_page.get_current_url() == Config.order_feed_url
        feed_page.click_constructor_button()
        main_page.wait_burgers_page()
        assert main_page.get_current_url() == Config.URL

    @allure.title("Переход на страницу Лента заказов")
    def test_open_constructor_page(self, driver, create_and_delete_user, login):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.wait_burgers_page()
        main_page.click_order_feed_button()
        feed_page.wait_title()
        assert feed_page.get_current_url() == Config.order_feed_url
