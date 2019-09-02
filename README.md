## Rose Knows Best Django Site

This is the source for my personal website, which can be viewed live [here](https://www.roseknowsbest.com/).

## Installation

This project is packaged using the [Poetry](https://poetry.eustace.io/docs/) dependency management tool.  To install it 
locally, clone the repository and run the following shell command after adding poetry to the PATH and activating a 
virtual environment.

```console
$ poetry install
```

Next, you will need to run PostrgeSQL on port 5432 (this is the default). Once it is running, make sure the following 
environment variables have been set:

 - `ROSEKNOWSBEST_PG_USER`: The user name to connect to Postgres locally.
 - `ROSEKNOWSBEST_PG_PASS`: The password for this user.
 
Then, you can apply the migrations by running the following command from the project's root directory:

```console
$ python manage.py migrate
```

The final step is to start the development server and then visit http://localhost:8000 in your browser.

```console
$ python manage.py runserver
```

## Running the tests

Run the unit tests for the whole project using the following shell command.

```console
$ python -Wa manage.py test --verbosity=2
```

## Deployment

This site is hosted on Digital Ocean. Opening a pull request branch will deploy proposed changes to a test environment, 
and once a pull request is approved and merged it will be available deployed to the production website. This site is powered by
Django and the database backend is PostgreSQL.