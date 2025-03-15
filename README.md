Mi nombre es Milena Vargas 
Bootcamp QA Engineer
Proyecto Urban Routes - Pruebas de Automatización
Descripción del Proyecto
Este proyecto consiste en la automatización de pruebas para la aplicación Urban Routes. Las pruebas verifican la funcionalidad de la plataforma en el proceso de solicitud de un taxi, asegurando que todas las interacciones del usuario funcionen correctamente. Se han implementado pruebas automatizadas para validar desde la configuración de direcciones hasta la confirmación del viaje.
Tecnologías y Herramientas Utilizadas
•	Python: Lenguaje principal para la automatización de pruebas.
•	Selenium WebDriver: Herramienta para la automatización de navegadores.
•	PyTest: Framework de pruebas utilizado.
•	Requests: Librería para realizar peticiones HTTP.
Estructura del Proyecto
Se han creado los siguientes archivos:
-	data.py               # Datos utilizados en las pruebas (URL, teléfono, tarjeta, etc.).
-	locators.py           # Localizadores de elementos de la interfaz.
-	main.py               # Implementación de la clase UrbanRoutes con los métodos de interacción.
-	test_urbanroutes.py   # Pruebas automatizadas con PyTest.
-	README.md             # Documentación del proyecto.
Casos de Prueba Implementados
1.	Configurar direcciones: Establecer la dirección de origen y destino.
2.	Seleccionar tarifa Comfort: Elegir la tarifa de servicio.
3.	Ingresar número de teléfono: Validar el ingreso del teléfono y el código de confirmación.
4.	Agregar tarjeta de crédito: Verificar la correcta adición de un método de pago.
5.	Escribir mensaje para el conductor: Confirmar la entrada de comentarios.
6.	Seleccionar comodidades: Elegir opciones adicionales como manta y pañuelos.
7.	Pedir 2 helados: Validar la selección de productos adicionales.
8.	Confirmar viaje: Comprobar que se muestra el modal de búsqueda de taxi.
9.	Verificar información del conductor: Validar que se muestra correctamente la información del conductor asignado.
Instalación y Configuración
Prerrequisitos
•	Tener instalado Python 3.x.
•	Instalar las dependencias necesarias ejecutando: 
•	pip install -r requirements.txt
Ejecución de Pruebas
Para ejecutar las pruebas, usa el siguiente comando en la terminal dentro del directorio del proyecto:
pytest test_urbanroutes.py
Esto ejecutará todas las pruebas y mostrará los resultados en la consola.
