# Autotests for web-application Opencart with Pytest, Jenkins and Docker.

Technology stack:
* Pytest
* Requests
* Selenium
* MariaDB Connector
* Faker
* Allure
* Docker
* Jenkins

Tests can be run locally (in a local browser or using Selenoid) and with Jenkins in a Docker container.

The tests assume storing environment variables in a `.env` file on the local machine.

### Run commads:
#### For build Docker container:
`docker build -t <image_name>`

#### For run Docker container:
`docker run --env-file <path_to_env-file> --rm -t <image_name> <pytest_params>`

#### For run Jenkins:
`docker run --env-file <path_to_env-file> -p 8082:8080 -v /var/run/docker.sock:/var/run/docker.sock --group-add=$(stat -c %g /var/run/docker.sock) --name <container_name> -t <image_name>`