from selenium.webdriver.common.by import By

## ============= Locators ================= ##

from_field = (By.ID, 'from')
to_field = (By.ID, 'to')
taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
comfort_tariff = (By.CSS_SELECTOR,'[alt="Comfort"]')

## ============ PHONE ATTRIBUTES ============ ##

phone_container = (By.CLASS_NAME,'np-button')
phone_modal = (By.CLASS_NAME,'modal')
phone_field_modal = (By.CLASS_NAME,'input-container')
phone_input = (By.ID, 'phone')
phone_submit_button = (By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
code_modal = (By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/form')
code_modal_container = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[1]')
code_modal_field = (By.XPATH,'//*[@id="code"]')
confirm_code = (By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
phone_check = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')

## ============== PAYMENT ATTRIBUTES ========= ##

payment_method = (By.CLASS_NAME,'pp-text')
add_card_button = (By.XPATH, '//div[text()="Agregar tarjeta"]')
card_form = (By.CLASS_NAME, 'card-wrapper')
card_number_field = (By.NAME,'number')
card_number_code_field = (By.NAME,'code')
confirm_card_button = (By.XPATH, '//button[text()="Agregar"]')
close_card_modal = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/button')

## ============= COMMENT ATTRIBUTES =============###

comment_selector = (By.XPATH,'//div[@class="input-container"]/label[text()="Mensaje para el conductor..."]')
comment_placer = (By.NAME,'comment')

## ============= Ride Parameters =============###

comodidades = (By.XPATH, '//div[text()="Manta y pañuelos"]')
radio_button = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
confirm_button = (By.CLASS_NAME,"smart-button")
ice_cream_counter = (By.CLASS_NAME,'counter-value')
tasty_ice_cream = (By.CLASS_NAME,'counter-plus')

## ============= RIDE MODAL ================== ##
order_modal = (By.CLASS_NAME, 'order-body')
order_header = (By.CLASS_NAME,"order-header")
order_header_title = (By.CLASS_NAME,"order-header-title")
driver_icon = (By.XPATH,'//img[@alt="Car"]')
