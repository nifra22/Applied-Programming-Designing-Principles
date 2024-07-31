from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your ChromeDriver
CHROMEDRIVER_PATH = 'path/to/chromedriver'

# URL of your running Dash application
DASH_APP_URL = 'http://127.0.0.1:8050/'

# Initialize the WebDriver
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)

try:
    # Open the Dash application
    driver.get(DASH_APP_URL)

    # Wait until the dropdown is present
    wait = WebDriverWait(driver, 10)
    dropdown = wait.until(EC.presence_of_element_located((By.ID, 'analysis-dropdown')))

    # Select "Best Selling Product" from the dropdown
    dropdown.click()
    best_selling_product_option = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="menuitem" and text()="Best Selling Product"]')))
    best_selling_product_option.click()

    # Wait for the graph to update
    time.sleep(2)

    # Take a screenshot of the graph
    graph = driver.find_element(By.ID, 'analysis-graph')
    graph.screenshot('best_selling_product.png')

    # You can add more interactions and assertions here

finally:
    # Close the browser
    driver.quit()
