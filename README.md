# fastapi_with_openai_api
## Name
FastAPI with OpenAI API Integration

## Description
This project is built in [FastAPI](https://fastapi.tiangolo.com/) using python 3.11.

This project contains routes for getting form data from user and sending it to [OpenAI API](https://beta.openai.com/).

## Project Structure
```
├── apps
│   ├── blog
│   │   ├── __init__.py
│   │   ├── route.py
│   ├── __init__.py
│   core
│   │   ├── __init__.py
│   │   ├── configuration.py
│   │   ├── helper.py
│   │   ├── middlewares.py
│   │   ├── response_message.py
│   │   ├── router.py
│   static
│   ├── templates
│   |   ├── index.html
│   ├── redoc.standalone.js
│   ├── swagger-ui-bundle.js
│   ├── swagger-ui-.css
|   main.py
│   Pipfile
│   Pipfile.lock
│   README.md
│   .gitignore
│   .env.example
```

## Installation
- Configure [Pyenv](https://realpython.com/intro-to-pyenv/):
To configure pyenv you can follow this [tutorial](https://realpython.com/intro-to-pyenv/).

- Install mysql dependencies:
```
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

- Python Installation:
To run project, you must have python 3.11 installed on your system.
If python 3.11 is not installed pyenv will install it for you as you have already configured pyenv.

- Change Global Python Version:
```
pyenv global 3.11.0
```

- Pipenv Installation:
After that, you need to install pipenv to handle virtual environments, you can install it by typing this command in your terminal:
```
pip install pipenv or
pip3 install pipenv
```

Adding pipenv to path
```
echo 'export PATH="/home/<user>/.local/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
```

Verify your pipenv installation:
```
pipenv
```

- Creating Virtual Environment
Go to project directory and type following command in terminal.
```
pipenv sync
```

This will create a virtual environment for your project along with dependencies.

- Activate Virtual Environment
To active virtual environment type following command in terminal.
```
pipenv shell
```

You can verify your environment dependencies by running:
```
pip list
```

## Running Project
- Run Project
```
uvicorn main:app --reload --host localhost --port 8000
```

- Acessing Project
```
http://localhost:8000/
```

- Accessing Swagger UI
```
http://localhost:8000/docs
```

- Accessing ReDoc
```
http://localhost:8000/redoc
```
