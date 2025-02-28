# Quart Template

A web server template written using Python Quart.

## Set Environment Variables

可以使用如下4个文件设置相应的环境变量：

- [.env](.env)
- [.env.dev](.env.dev)
- [.env.prod](.env.prod)
- [.env.test](.env.test)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/King-sj/quart-template.git
    cd quart-template
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Set the environment variables:
    ```sh
    cp .env.example .env
    # Edit the .env file to configure your environment variables
    ```

2. Run the application:
    ```sh
    python run.py
    ```

## Project Structure

```
quart-template/
├── __pycache__/
├── .env
├── .env.dev
├── .env.prod
├── .env.test
├── .github/
├── .gitignore
├── .pre-commit-config.yaml
├── .pytest_cache/
├── .vscode/
├── docs/
├── ksj.session.sql
├── LICENSE
├── logs/
├── main.session.sql
├── migrations/
├── postgres.session.sql
├── pyproject.toml
├── pytest.ini
├── README.md
├── requirements.txt
├── run.py
├── settings.py
├── sql/
├── src/
│   ├── app.py
│   ├── args.py
│   ├── auth/
│   ├── configs/
│   ├── controllers/
│   ├── globals/
│   ├── models/
│   ├── plugins/
│   ├── types/
│   ├── utils/
│   └── __init__.py
├── static/
├── templates/
├── tests/
└── tmp/
```

## Running Tests

To run the tests, use the following command:
```sh
pytest
```

## License

This project is licensed under the terms of the Mozilla Public License Version 2.0.


## more docs
look the file in dir docs