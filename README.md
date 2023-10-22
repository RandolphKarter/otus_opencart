# Autotests for web-application Opencart with Pytest, Jenkins and Docker.

Technology stack:
* Pytest
* Requests
* Selenium
* MariaDB Connector
* Faker
* Allure
* Selenoid
* Docker
* Jenkins

Tests can be run locally (in a local browser or using Selenoid) and with Jenkins in a Docker container.

The tests assume storing environment variables in a `.env` file on the local machine.

### Example `.env` file with required values:
* API_USER = you Opencart API username
* API_KEY = you Opencart API key
* DB_USER = OPENCART_DATABASE_USER from Opencart docker image
* DB_HOST = you Opencart local host IP
* DB_NAME = OPENCART_DATABASE_NAME from Opencart docker image
* OC_ADMIN_NAME = Opencart admin username
* OC_ADMIN_PW = Opencart admin password

For setup and use Opencart API read this [article](https://docs.opencart.com/en-gb/system/users/api/)

### Run commands:
#### Build Docker container:
`docker build -t <image_name>`

#### Run Docker container:
`docker run --env-file <path_to_env-file> --rm -t <image_name> <pytest_params>`

#### Run Jenkins:
`docker run --env-file <path_to_env-file> -p 8082:8080 -v /var/run/docker.sock:/var/run/docker.sock --group-add=$(stat -c %g /var/run/docker.sock) --name <container_name> -t <image_name>`