import argparse
import logging
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


# Configurar logging
logging.basicConfig(filename='dns_creation_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Parsear argumentos de la línea de comandos
parser = argparse.ArgumentParser(description='Crear un registro DNS.')
parser.add_argument('nombre_registro', type=str, help='Nombre del registro DNS.')
parser.add_argument('ip_servidor', type=str, help='IP del servidor.')
args = parser.parse_args()

nombre_registro = args.nombre_registro
ip_servidor = args.ip_servidor
usuario = "tu_usuario"
clave = "tu_clave$"

# Inicializar el navegador
try:
    driver = webdriver.Chrome()
    logging.info("Navegador iniciado correctamente.")
except Exception as e:
    logging.error("Error al iniciar el navegador: %s", e)
    raise

try:
    # Navegar a la página de login
    driver.get("https://www1.domain.com/login")
    logging.info("Navegado a la página de login.")

    # Llenar el formulario de login
    driver.find_element(By.ID, "credential_c0").send_keys(usuario)
    driver.find_element(By.ID, "credential_c1").send_keys(clave + Keys.RETURN)
    logging.info("Formulario de login completado.")

    # Navegar a la página de gestión de DNS
    driver.get("https://www1.domain.com/controlpanel/foundation/codifyanalytics.tech/dns")
    logging.info("Navegado a la página de gestión de DNS.")

    # Hacer click en el span 'DNS RECORDS'
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='DNS RECORDS']"))
    ).click()
    logging.info("Haciendo click en 'DNS RECORDS'.")

    # Hacer click en el botón para añadir un registro DNS
    try:
        add_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qe-id='btn-add-dns-record']"))
        )
        logging.info("Botón encontrado. Realizando click.")
        add_button.click()
        logging.info("Click realizado en el botón para añadir un registro DNS.")
    except TimeoutException:
        logging.error("No se pudo encontrar el botón para añadir un registro DNS.")
        driver.quit()
        raise

    # Completar el formulario para añadir el registro DNS
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    ).send_keys(nombre_registro)
    logging.info(f"Introduciendo el nombre del registro: {nombre_registro}")

    # Seleccionar el tipo de registro 'A'
    select_tipo = Select(
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "type"))
        )
    )
    select_tipo.select_by_value("A")
    logging.info("Seleccionando el tipo de registro 'A'.")

    # Introducir la IP del servidor
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "data"))
    ).send_keys(ip_servidor)
    logging.info(f"Introduciendo la IP del servidor: {ip_servidor}")

    # Seleccionar el TTL '1/2 Hour'
    select_ttl = Select(
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "ttl"))
        )
    )
    select_ttl.select_by_value("1800")
    logging.info("Seleccionando el TTL '1/2 Hour'.")

    # Hacer click en el botón para enviar el formulario
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qe-id='btn-submit-dns']"))
    ).click()
    logging.info("Haciendo click en el botón para enviar el formulario.")

    time.sleep(10)

except Exception as e:
    logging.error("Error en el script: %s", e)
    raise

finally:
    # Cerrar el navegador al finalizar
    driver.quit()
    logging.info("Navegador cerrado.")
