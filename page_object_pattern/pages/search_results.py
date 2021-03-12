import logging
import allure
from allure_commons.types import AttachmentType


class SearchResultsPage:

    def __init__(self,driver):
        self.driver = driver
        self.hotel_names_xpath = "//h4[contains(@class,'list_title')]//b"
        self.hotel_prices_xpath = "//div[contains(@class,'price_tab')]//b"
        self.logger = logging.getLogger(__name__)

#Creating hotel name list with raport description
    @allure.step("Getting hotel names")
    def get_hotel_names(self):

        hotels = self.driver.find_elements_by_xpath(self.hotel_names_xpath)
        names =  [hotel.get_attribute("textContent") for hotel in hotels]
        self.logger.info("Available hotels are:")
        allure.attach(self.driver.get_screenshot_as_png(), name="Hotel names", attachment_type=AttachmentType.PNG)
        for name in names:
            self.logger.info(name)
        return names

#Creating hotel price list with raport description
    @allure.step("Getting hotel prices")
    def get_hotel_prices(self):
        prices = self.driver.find_elements_by_xpath(self.hotel_prices_xpath)
        hotel_prices =   [price.get_attribute("textContent") for price in prices]
        self.logger.info("Prices of available hotels are:")
        allure.attach(self.driver.get_screenshot_as_png(), name="Hotel prices", attachment_type=AttachmentType.PNG)
        for hotel in hotel_prices:
            self.logger.info(hotel)
        return hotel_prices



