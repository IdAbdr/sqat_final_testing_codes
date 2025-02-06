from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class SauceDemoRegressionTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")

    def test_login(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        self.assertIn("https://www.saucedemo.com/inventory.html", driver.current_url)

    def test_add_to_cart(self):
        self.test_login()  

        driver = self.driver
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_badge.text, "1")

    def test_sorting_functionality(self):
        self.test_login()  

        driver = self.driver
        driver.find_element(By.CLASS_NAME, "product_sort_container").click()
        driver.find_element(By.XPATH, "//option[@value='lohi']").click()
        
        items = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = [float(item.text[1:]) for item in items]  
        self.assertEqual(prices, sorted(prices))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
