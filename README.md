# Test Kuantaz

## Description
---
API Rest written with Python using Flask and SQLAlchemy.

### Construction 🛠️
* **Language:** Python 3.9
* **Technologies:** Flask, SQL Alchemy, Marshmallow, Flasgger.
* **Database:** PostgreSQL 15

## Requirements
---
- Docker installed

- Remember to copy the env.test to .env ( in folder app ) to add environment variables to the application.

## Installation and execution
---
Clone or Fork the project.

Run ```docker-compose``` command inside **docker-python** folder.

* Building the containers: ```docker-compose build```

* Starting the services: ```docker-compose up -d```

* Stoping the services: ```docker-compose stop```

By default the service will run under the following port:
- test_kuantaz: 5000

## Project Structure
---
The following diagram describe the project structure used for this API
```
test_kuantaz
│   .gitignore
│   README.md
│   docker-compose.yml
│   .pre-commit-config.yaml
│
└───app
│   │   .env.docker
│   │   .env.test
│   │   .entrypoint.sh
│   │   Dockerfile
│   │   requirements.txt
│   │   requirements-docker.txt
│   │   .dockerignore
│   │
│   │   main.py
│   │
│   └───config                  Contains system settings
│   │   │
│   │   └───http_status_code.py Contains constants for HTTP_CODE for endpoint.
│   │   │
│   │   └───constants.py        Constants used in the project
│   │
│   │   └───database.py         Functions and constants for manage database
│   │
│   │   └───exceptions.py       Contains the custom exceptions for project
│   │
│   │   └───environment.py      Environment variables
│   │
│   └───models                  Contains the models for database
│   │
│   │   ...
│   │
│   └───queries                 Functions for manage database with models
│   │
│   │   ...
│   │
│   └───schemas                 Contains the schematics (marshmallow) used in the project
│   │
│   │   ...
│   │
│   └───services                The application service layer
│   │
│   │   ...
│   │
│   └───utils                   Functions utils
│   │
│   │   ...
│   │
│   └───swagger_docs
│   │
│   └───tests
│
└────────────
...

```

## Documentation 📕
---

The documentation is in postman and swagger.

swagger : http://localhost:5000/graphql (execute for dev or docker)

postman : [documentation on Postman](documentation/test_kuantaz.postman_collection.json). Remember to add the environment variables in postman ( {{base_url}} )


#### Note 🔍
To use test data, make a Get request for endpoint "/dummy"

## Development 💻

Requirements:
- virtualenv
- python3.9

If you want to run the project to develop , you can run the following commands:
```shell
   cd app

   virtualenv -p python3.9 env

   source env/bin/activate # in linux or macos

   pip install -r requirements
```

Run with env activated:

```shell
   python main.py
```

If you want to contribute to the project, Remember that pre-commit is used for uniform code styling, so you'll need to **install the pre-commit**.

## Testing ⚙️

Requirements: Follow the instructions it says in Development

To run the tests:

```shell
   cd app

   source env/bin/activate

   python -m pytest
```

### Authors ✒️

* **Author:** Steve Matos, <steve.matos.1998@gmail.com>
