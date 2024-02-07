import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


users = ['user1@gmail.com','user2@gmail.com','user3@gmail.com']
passw = ['aaaaaaa', 'bbbbbbb', 'ccccccc']

def generate_pairs():
    pairs = []
    for user in users:
        for passw in passws:
            pairs.append((user, passw))
    return pairs

# @pytest.mark.parametrize('creds',
#                          [
#     pytest.param(('user1@gmail.com', 'aaaaaaa'), id='user1@gmail.com, aaaaaaa'),
#     pytest.param(('user2@gmail.com', 'bbbbbbb'), id='user2@gmail.com, bbbbbbb'),
#     pytest.param(('user3@gmail.com', 'ccccccc'), id='user3@gmail.com, ccccccc')
#                          ])

@pytest.mark.skip
@pytest.mark.parametrize('creds', generate_pairs())
def test_login(creds):
    login, passw = creds
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
    driver.get('https://magento.softwaretestingboard.com/customer/account/login/')
    driver.find_element(By.ID, 'email').send_keys(login)
    driver.find_element(By.ID, 'pass').send_keys(passw)
    driver.find_element(By.ID, 'send2').click()
    error_text = driver.find_element(By.CSS_SELECTOR, '[data-ui-id="message-error"]').text
    assert ('The account sign-in was incorrect or your account is disabled temporarily. '
            'Please wait and try again later.'
            == error_text)


@pytest.fixture()
def page(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
    param = request.param
    if param == 'wats_new':
        driver.get('https://magento.softwaretestingboard.com/what-is-new.html')
    elif param == 'sale':
        driver.get('https://magento.softwaretestingboard.com/sale.html')
    return driver

@pytest.mark.parametrize('page', ['wats_new'], indirect=True)
def test_whats_new(pege):
    title = page.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == "What's New"

@pytest.mark.parametrize('page', ['sale'], indirect=True)
def test_sale(pege):
    title = page.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == "Sale"