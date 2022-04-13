# Zeit Sr SWE Take Home Challenge

This application is built on [FastAPI](https://fastapi.tiangolo.com/) and
[React](https://reactjs.org/).

## Prerequisites

You need a current version of [Python](https://www.python.org/downloads/) and
[pip](https://pypi.org/project/pip/). You also need a current version of
[Node](https://nodejs.org/en/).


## Installing

### Clone code

```bash
git clone https://github.com/gegnew/zeitchallenge
```

#

### Install backend dependencies

```bash
cd backend
pip install -e .
pip install -r requirements-dev.txt
```

#

### Install frontend dependencies

```bash
cd frontend
npm install
```

#

### Create .env file

Refer to `.env.example` in both `frontend/` and `backend/` and set required
variables in `project-root/frontend/.env` and `project-root/backend/.env`,
respectively.

#

## Usage

Start the backend server:

```bash
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

#

Start the frontend server:

```bash
cd frontend
npm run start
```

#

## Testing

Tests for the backend are written with
[pytest](https://docs.pytest.org/en/6.2.x/).

Run all tests from the command line with `pytest`. Run a single test with
`pytest tests/path/to/file`. Alternatively, use a [test
runner](https://github.com/vim-test/vim-test).

## Deployment

There is only one instance of `zeitchallenge`, deployed with `docker-compose`
on an EC2 server.

Deployment is managed with [Github
Actions](https://docs.github.com/en/actions). This is the "simplest-possible"
CI/CD with two workflows, defined in `project-root/.github/workflows/`:

1. `pytest.yml` runs `black`, `flake8`, and `pytest`. This runs on every push
   to any branch.
2. `deploy.yml` uses [AWS
   SSM](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
   to run a deployment file on the "production" EC2 instance. It runs when a pull request
   is merged to the `main` branch.

The `deploy.yml` workflow simply runs a "deploy.sh" script, which does:
```bash
#!/bin/sh

cd zeitchallenge
sudo git fetch --all
sudo git reset --hard  origin/main
sudo docker-compose up --build -d
```


## Owner

For questions about this package, please contact:

- [@gegnew](https://github.com/gegnew)
