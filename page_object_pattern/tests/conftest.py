import allure
import pytest
from allure_commons.types import AttachmentType


from page_object_pattern.utils.driver_factory import driverFactory

#Setting browser properties
@pytest.fixture()
def setup(request):
    driver = driverFactory.get_driver("firefox")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(),name="Test failed",attachment_type=AttachmentType.PNG)
    driver.quit()