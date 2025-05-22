import pytest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Read test data from CSV
data = pd.read_csv(r"C:\Users\PMLS\Desktop\SCaD_Working\Selenium\Form_Validation\test_data.csv")

@pytest.mark.parametrize("name,cnic,expected_result", data.values)
def test_form_validation(name, cnic, expected_result):
    # Setup Edge options
    edge_options = Options()
    edge_options.add_argument('--headless')  # Run in headless mode
    edge_options.add_argument('--inprivate')  # Run in InPrivate mode
    
    driver = webdriver.Edge(options=edge_options)

    try:
        # Convert backslashes to forward slashes and add file protocol
        file_path = "file:///" + r"D:\SCaD_Working\Selenium\index.html".replace("\\", "/")
        driver.get(file_path)
        
        # Wait for elements with explicit wait
        wait = WebDriverWait(driver, 10)
        name_field = wait.until(EC.presence_of_element_located((By.ID, "name")))
        cnic_field = wait.until(EC.presence_of_element_located((By.ID, "cnic")))

        # Input values
        name_field.clear()
        cnic_field.clear()
        name_field.send_keys(str(name))
        cnic_field.send_keys(str(cnic))

        # Validate fields
        name_valid = driver.execute_script("return document.getElementById('name').checkValidity();")
        cnic_valid = driver.execute_script("return document.getElementById('cnic').checkValidity();")
        
        # Debug information
        print(f"\nTesting: name='{name}', cnic='{cnic}'")
        print(f"Name valid: {name_valid}, CNIC valid: {cnic_valid}")
        print(f"Expected result: {expected_result}")
        
        actual_result = "pass" if name_valid and cnic_valid else "fail"
        assert actual_result == expected_result, \
            f"Validation failed: Expected '{expected_result}' but got '{actual_result}' for name='{name}', cnic='{cnic}'"

    except Exception as e:
        pytest.fail(f"Test error: {str(e)}")
        
    finally:
        driver.quit()