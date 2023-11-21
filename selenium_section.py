from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

mileage_url = "https://app.informedk12.com/link_campaigns/morgan-hill-travel-reimbursement-claim-electronic-form?token=fgtwSdEWCn8npWkHbYDbjfQH"


# first 48829198
# last 48829359


def entrypoint(user_info, list_of_rows):
    options = Options()
    options.add_experimental_option("detach", True)
    main_driver = webdriver.Chrome(options=options)

    main_driver.get(mileage_url)

    fill_name(main_driver, user_info)
    fill_sheet(main_driver, list_of_rows)


def fill_name(driver, user_info):
    """Waits for about 4 seconds for webpage elements to load
    Locates elements and enters name and email"""
    driver.implicitly_wait(4)
    driver.find_element(By.ID, "recipient_name").send_keys(user_info['name'])
    driver.find_element(By.ID, "recipient_email").send_keys(user_info['email'])
    driver.find_element(By.NAME, "commit").click()
    return


def fill_sheet(driver, data):
    # Locate first element
    driver.implicitly_wait(4)
    current_id = 48829198
    type_counter = 0
    types = ["input", "textarea", "textarea", "select", "textarea", "textarea"]
    for row in data:
        type_counter = 0
        for value in row:
            xpath = f"//{types[type_counter]}[@data-field-id={current_id}]"
            driver.find_element(By.XPATH, xpath).send_keys(value)
            type_counter += 1
            current_id += 1
    return
