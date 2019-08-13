from selenium import webdriver


def test_saec_hello_ff():
    ff = webdriver.Firefox()
    ff.get('http://localhost:5000/')
    assert ff.find_element_by_id('texto').text == 'Olá SAEC'
    ff.quit()


def test_saec_hello_ch():
    ch = webdriver.Chrome()
    ch.get('http://localhost:5000/')
    assert ch.find_element_by_id('texto').text == 'Olá SAEC'
    ch.quit()
