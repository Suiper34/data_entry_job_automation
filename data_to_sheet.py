from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdbm7IggqaNt3Xb3UbdfRot8O-64-OZtdu8Fex11RSAJ3MPww/viewform?usp=header'


class UploadData:
    def __init__(self):
        options = ChromeOptions()
        options.add_experimental_option('detach', True)
        self.FORM_URL = FORM_URL
        self.upload_data_driver = webdriver.Chrome(
            options)

    def house_data_upload(self, address: str, price: float, link: str):
        # enforcing price type check
        if not isinstance(price, (float, int)):
            print('Price should be a number.')
            return

        try:
            self.upload_data_driver.get(self.FORM_URL)

        except TimeoutException as te:
            print('Page could not load:', te)
            self.upload_data_driver.get(self.FORM_URL)

        else:
            try:
                # upload property's address
                property_addr = WebDriverWait(self.upload_data_driver, 20).until(
                    expected_conditions.presence_of_element_located(
                        (By.XPATH,
                         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
                         )
                    )
                )
                property_addr.send_keys(address)

                # upload rent price per month
                price_per_month = WebDriverWait(self.upload_data_driver, 2).until(
                    expected_conditions.presence_of_element_located(
                        (By.XPATH,
                         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
                         )
                    )
                )
                price_per_month.send_keys(f'${price}')

                # upload address link
                addr_link = WebDriverWait(self.upload_data_driver, 2).until(
                    expected_conditions.presence_of_element_located(
                        (By.XPATH,
                         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
                         )
                    )
                )
                addr_link.send_keys(link)

                # submit data
                submit = WebDriverWait(self.upload_data_driver, 2).until(
                    expected_conditions.element_to_be_clickable(
                        (By.CSS_SELECTOR,
                         'div[aria-label="Submit"]'
                         )
                    )
                )
                submit.click()

            except (Exception, NoSuchElementException, TimeoutException) as e:
                print('Element not found or not accessible:', e)

    # close tab after completion
    def close_tab(self):
        self.upload_data_driver.close()
