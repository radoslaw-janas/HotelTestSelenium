import logging
import allure
from allure_commons.types import AttachmentType

#Defining locators

class SearchHotelPage:
    def __init__(self,driver):
        self.driver = driver
        self.search_hotel_span_xpath = "//a/span[text()='Search by Hotel or City Name']"
        self.search_hotel_input_xpath = "//div[@id='select2-drop']//input"
        self.location_match_xpath = "//li/div/span[text()='Dubai']"
        self.check_in_input_name =  "checkin"
        self.check_out_input_name = "checkout"
        self.travellers_input_id = "travellersInput"
        self.adult_input_id = "adultInput"
        self.child_input_id = "childInput"
        self.search_button_xpath = "//button[text()=' Search']"
        self.logger = logging.getLogger(__name__)

#Setting city with raport description
#Taking a screen shot if test fails
    @allure.step("Setting city '{1}'")
    def set_city(self,city):
        self.logger.info("Setting city {}".format(city))
        self.driver.find_element_by_xpath(self.search_hotel_span_xpath).click()
        self.driver.find_element_by_xpath(self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element_by_xpath(self.location_match_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="setting city", attachment_type=AttachmentType.PNG)

#Setting check in and check out date with raport description

    @allure.step("Setting check in date '{1}', setting check out date'{2}'")
    def set_date_range(self,check_in,check_out):
        self.logger.info("Setting check in {checkin} and checkout {checkout} dates".format(checkin=check_in,checkout=check_out))
        self.driver.find_element_by_name(self.check_in_input_name).send_keys(check_in)
        self.driver.find_element_by_name(self.check_out_input_name).send_keys(check_out)
        allure.attach(self.driver.get_screenshot_as_png(), name="setting date range", attachment_type=AttachmentType.PNG)

#Setting the number of adult and child travellers with raport description
#Taking a screen shot if test fails

    @allure.step("Setting adult travelers '{1}', and setting child travellers'{2}'")
    def set_travelers(self,adult,child):
        self.logger.info("Setting adult travellers {adults} and setting child travelers {children}".format(adults=adult, children=child))
        self.driver.find_element_by_id(self.travellers_input_id).click()
        self.driver.find_element_by_id(self.adult_input_id).clear()
        self.driver.find_element_by_id(self.adult_input_id).send_keys(adult)
        self.driver.find_element_by_id(self.child_input_id).clear()
        self.driver.find_element_by_id(self.child_input_id).send_keys(child)
        allure.attach(self.driver.get_screenshot_as_png(), name="setting travellers ", attachment_type=AttachmentType.PNG)

#Performing search with raport description

    @allure.step("Performing search")
    def perform_search(self):
        self.logger.info("Performing search")
        self.driver.find_element_by_xpath(self.search_button_xpath).click()















