from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

chromePath = r"C:\Users\paragk1\PycharmProjects\Git_SW\chromedriver.exe"

driver = Chrome(executable_path=chromePath)
driver.get('https://www.google.com')
driver.find_element_by_xpath("//*[@title = 'Search']").send_keys('Appzen labs'+ Keys.RETURN)

@pytest.mark.parametrize(PHRASE,['abc','123'])
    def test_search(phrase,driver):
    driver.find_element_by_xpath().get()
