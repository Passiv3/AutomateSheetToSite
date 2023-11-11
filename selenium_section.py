from selenium import webdriver

mileage_url = "https://app.informedk12.com/link_campaigns/morgan-hill-travel-reimbursement-claim-electronic-form?token=fgtwSdEWCn8npWkHbYDbjfQH"


#first 48829198
#last 48829359


def entrypoint():
    driver = webdriver.Chrome()
    driver.get(mileage_url)


entrypoint()
