
# docker_odoo_chasqui

Este repositorio contiene todos los archivos necesarios para crear una imagen de Docker de Odoo preconfigurado con addons de regionalización argentina y módulos útiles para el portal de ventas online "Chasqui".

## Pre-requisitos

Asegúrate de tener Docker y Docker Compose instalados en tu sistema para poder utilizar este proyecto. Para más información sobre cómo instalar Docker, visita [Instalar Docker](https://docs.docker.com/get-docker/).

## Configuración inicial

Antes de construir la imagen de Docker, es necesario preparar los addons necesarios. Esto se realiza con el siguiente comando:

```bash
bash odoo16/prepare_addons.sh
```

Este script configura los addons necesarios para Odoo, incluyendo los módulos específicos de regionalización para Argentina y otros módulos útiles para "Chasqui".

## Construcción de la imagen

Una vez que los addons están preparados, puedes proceder a construir la imagen de Docker utilizando el siguiente comando:

```bash
docker build -t odoo4chasqui ./odoo16
```

Este comando construye la imagen de Docker etiquetada como `odoo4chasqui` basándose en los archivos y configuraciones ubicados en el directorio `odoo16`.

## Ejecución del contenedor

Para iniciar el contenedor de Docker, usa Docker Compose con el siguiente comando:

```bash
docker-compose up --build
```

Este comando levanta el contenedor de Odoo configurado, reconstruyendo la imagen si es necesario y iniciando los servicios definidos en tu archivo `docker-compose.yml`.

## Uso

Una vez que el contenedor está en funcionamiento, puedes acceder a tu instancia de Odoo configurada a través de tu navegador web en `http://localhost:8069`.

## Contribuciones

Las contribuciones a este proyecto son bienvenidas. Por favor, asegúrate de seguir las pautas de contribución listadas en `CONTRIBUTING.md`.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo `LICENSE.md` para más detalles.
