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
    locate_first_cell(main_driver)


def fill_name(driver, user_info):
    """Waits for about 4 seconds for webpage elements to load
    Locates elements and enters name and email"""
    driver.implicitly_wait(4)
    driver.find_element(By.ID, "recipient_name").send_keys(user_info['name'])
    driver.find_element(By.ID, "recipient_email").send_keys(user_info['email'])
    driver.find_element(By.NAME, "commit").click()
    return


def locate_first_cell(driver):
    driver.implicitly_wait(4)
    return driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div[4]/div[1]/div[2]/div/span[14]/span/input[2]")


def fill_row():
    pass


entrypoint({'name': 'Danny Chung', 'email': 'chungdanny56@gmail.com'}, [['11/12/2023', 'District Office', 'Britton', 'RT', 'Fix Technology', '5.2'], ['11/12/2023', 'District Office', 'Sobrato', 'OW', 'Fix Technology', '10.5']])
