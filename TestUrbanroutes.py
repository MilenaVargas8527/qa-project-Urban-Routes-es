from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from selenium import webdriver
import locators
from main import UrbanRoutes

## === Test Class ====##

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        from_address = data.address_from
        to_address = data.address_to
        UrbanRoutes(self.driver).set_route(from_address,to_address)
        # Aserción de que el botón "Pedir un taxi" está habilitado.
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locators.taxi_button))
        assert UrbanRoutes(self.driver).get_from() == from_address
        assert UrbanRoutes(self.driver).get_to() == to_address
        assert self.driver.find_element(*locators.taxi_button).is_enabled()
        UrbanRoutes(self.driver).ask_for_taxi_button()

    def test_set_comfort_fare(self):
        # Aserción de que el botón "Tarifa Comfort" está habilitado.
        assert self.driver.find_element(*locators.comfort_tariff).is_enabled()
        UrbanRoutes(self.driver).set_comfort_fare()

    def test_fill_phone_code(self):
        UrbanRoutes(self.driver).phone_modal_info()
        # Se asegura que aparezca el modal de telefono:
        assert WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locators.phone_modal))
        UrbanRoutes(self.driver).fill_phone_requirements()
        #Se asegura de que aparezca el modal para introducir el código de telefono.
        assert WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(locators.code_modal))
        #Se modificó el test para resumir la aserción del contenido del campo de telefono.
        UrbanRoutes(self.driver).fill_phone_code()
        expected_value = UrbanRoutes(self.driver).assure_phone_number_after_code()
        assert expected_value == data.phone_number

    def test_fill_payment_info(self):
        # Se asegura que el boton de informacion de pago este habilitado.
        assert self.driver.find_element(*locators.payment_method).is_enabled()
        UrbanRoutes(self.driver).select_payment_info()
        # Se asegura que el boton "Agregar tarjeta" aparece y es visible para el usuario:
        assert self.driver.find_element(*locators.add_card_button).is_displayed()
        self.driver.find_element(*locators.add_card_button).click()
        # Se asegura que el formulario de tarjeta es visible para el usuario:
        assert WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locators.card_form)).is_displayed()
        UrbanRoutes(self.driver).fill_payment_info()

    def test_comment_for_driver(self):
        # Se asegura de que los datos en los campos de tarjeta coincidan con los ingresados por el usuario.
        card_value = UrbanRoutes(self.driver).get_card_number()
        card_code_value = int(UrbanRoutes(self.driver).return_card_code())  # Convertir a entero
        UrbanRoutes(self.driver).comment_for_driver()
        comment = UrbanRoutes(self.driver).check_driver_comment()
        assert card_value == data.card_number
        assert card_code_value == data.card_code
        assert comment == data.message_for_driver

    def test_define_ride_comodidades(self):
        # Se asegura que se muestran las opciones "Comodidades" y su selector.
        assert self.driver.find_element(*locators.comodidades).is_displayed()
        UrbanRoutes(self.driver).define_ride_settings()
        assert self.driver.find_element(*locators.radio_button).is_displayed()
        UrbanRoutes(self.driver).click_on_radio_button()

    def test_ice_cream_for_rider(self):
        # Agregué este assert para que confirme que esta disponible el contador de helado
        assert self.driver.find_element(*locators.tasty_ice_cream).is_enabled()
        # El contador esta en cero:
        counter_status = UrbanRoutes(self.driver).is_ice_cream_counter_zeroed()
        assert counter_status == '0'
        #Agregar helado y asegurar que coincide con la eleccion del usuario:
        UrbanRoutes(self.driver).add_tasty_ice_cream()
        counter_status = UrbanRoutes(self.driver).did_you_add_tasty_ice_cream()
        assert counter_status == '2'

    def test_confirm_taxi_modal_shows_up(self):
        # Se asegura de que el botón de confirmar y el modal de busqueda sean visibles para el usuario.
        assert self.driver.find_element(*locators.confirm_button).is_enabled()
        UrbanRoutes(self.driver).confirm_and_look_for_taxi()
        assert WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locators.order_modal)).is_displayed()

    def test_show_driver_info(self):
        # Se asegura que aparece la informacion del conductor
        assert WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(locators.driver_icon))
        trip_confirm_message = UrbanRoutes(self.driver).show_driver_info()
        assert "El conductor llegará en" in trip_confirm_message


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
