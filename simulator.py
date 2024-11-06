import json
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def load_json(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def save_json(data, json_file):
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

def select_option(driver, element_id, value):
    select = Select(driver.find_element(element_id))
    select.select_by_value(str(value))

def automate_dropdowns(json_input_file, json_output_file, driver_path):
    # Load the input JSON data
    data = load_json(json_input_file)

    # Configure Chrome to use the remote debugging port
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")

    # Initialize the Selenium WebDriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
                          
    driver.get('https://complaint.pmc.gov.in/newComplaint')  # Replace with your target URL
    

    # Store progress data
    progress_data = []

    for entry in data:
        category_id = entry.get('categoryId')
        category_detail_id = entry.get('grievanceSubDeptDetailId')

        result = entry.copy()  # Copy the original entry for result tracking

        try:
            # Select the categoryId
            select1 = Select(driver.find_element(By.ID, "categoryId"))
            select1.select_by_value(str(category_id))
            time.sleep(1)  # Wait for the second dropdown to update

            # Select the categoryDetailId
            select2 = Select(driver.find_element(By.ID, "categoryDetailId"))
            select2.select_by_value(str(category_detail_id))

            result['status'] = 'success'
        except Exception as e:
            result['status'] = 'failure'
            result['error'] = str(e)

        progress_data.append(result)

    # Save the progress data
    save_json(progress_data, json_output_file)

    # Close the browser
    driver.quit()
    print(f"Automation completed. Progress saved to {json_output_file}")

# Example usage

chrome_driver_path = "C:\\chromium\\driver\\chromedriver.exe"

automate_dropdowns('json/output/final.json', 'json/output/checked.json', chrome_driver_path)
