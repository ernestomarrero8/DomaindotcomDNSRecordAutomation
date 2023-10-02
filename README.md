# Automatización de Creación de Registro DNS con Selenium

Este proyecto automatiza el proceso de crear un registro DNS mediante el uso de Selenium, una herramienta para probar aplicaciones web.

## 📋 Requisitos

- Python 3.11
- Selenium
- ChromeDriver

## 🛠️ Instalación

1. **Clonar este repositorio**
   ```sh
   git clone https://github.com/ernestomarrero8/DomaindotcomDNSRecordAutomation

2. **Instalar las dependencias**

pip install selenium
Descargar ChromeDriver
Añadir la ubicación de ChromeDriver al PATH de tu sistema operativo.

## 🚀 Uso
Ejecutar el script de Python desde la línea de comandos, pasando el nombre del registro DNS y la IP del servidor como argumentos.

python dominio.py <nombre_registro> <ip_servidor>
Ejemplo:

python dominio.py ejemplo 127.0.0.1


## ⚙️ Funcionamiento
El script inicia un navegador Chrome y navega a la página de login.
Rellena el formulario de login con el usuario y la contraseña.
Navega a la página de gestión de DNS.
Hace clic en el botón para añadir un nuevo registro DNS.
Rellena el formulario con el nombre del registro, el tipo de registro ('A'), la IP del servidor, y el TTL ('1/2 Hour').
Hace clic en el botón para enviar el formulario y añadir el registro DNS.
Cierra el navegador.

## 📝 Notas
Asegúrate de modificar el script con tu usuario y contraseña antes de ejecutarlo.
El uso de este script debe ser un variables de entornos o con algun keyvault, utilizar usuarios y contraseñas en el codigo es una mala practica que podria comprometer sus dominios.
