# Lighthouse, the Check MK slack agent

## Deployment
TODO: ADD

## Quick start:

Verify python version is at least 3.6
`python --version`

Verify or install `pipenv`
`pip list | grep pipenv` or `pip install -g pipenv`

Generate local virtualenv using pipenv.
`pipenv --three`

Activate env
`pipenv shell`

Install pip packages
`pipenv install`


## Use of Environment variables
Lighthouse uses Environment variables to pull slack token and the slack
Lighthouse name. Currently the use of `SLACK_CLIENT_TOKEN` and `SLACK_CLIENT_NAME`
as the two variables. For development use of [direnv](https://github.com/direnv/direnv)
is suggested for development.


Lighthouse also uses CheckMk variables:
    CHECK_MK_SERVER=http://gewrnoccmk1test.taketwo.online/master_dev/check_mk/webapi.py
    CHECK_MK_USER=automation
    CHECK_MK_PASSWORD=<magicpassowrd>

The user needs to be an automation user in order to use the web api. Also, the server must be the
full path to the `webapi.py` Without the full path, the CheckMk client will not connect.


## Virtual Environment management
- [Pipenv](https://pipenv.readthedocs.io/en/latest)

Pipenv is a virtual Environment management tool that is the next generation of virtualenv. This tool wraps
and augments the use of virtualenv. If you are familiar with virtualenv, the use of pipenv should not be an issue.

Some of the advantages of `pipenv` include easily useable development packaging, package locking, and dependency chain
verification.

To install a production use package and update dependencies `pipenv install <package>` is used.

To install a development use package and update dependencies `pipenv install <package> --dev` is used.

This easy to separate command allows for a quick view in `Pipenv` to determine which packages are used in production and
which are used for development and testing.


To run a command directly in `pipenv` you can use a `pipenv run <command>.` This will allow execution of commands directly.

`pipenv run pytest` 

This will execute `pytest` in the virtual environment.

## Testing
Lighthouse is tested using `py.test.` This testing framework provides mocking, boilerplate, and other code replacements
reducing the amount of code required to test a function.

The other notable package used in Lighthouse testing is [VCR.py](https://vcrpy.readthedocs.io/en/latest/installation.html).
This package allows for local recordings of API responses.
Availability of these recordings provides a deterministic test set and fast testing for API endpoints without the need to
mock every request. This also provides a distinct line between API and Lighthouse issues.


### Running Tests
After installing the required packages using `pipenv` one can simply run `py.test` to execute all tests in the project.

Py.test also allows for the `py.test -f` argument which provides recursive directory checking for file changes followed by
execution of all tests in the project.

To correctly use VCR.py, run `pytest --vcr-record=none` on CI.
This will prevent VCR from recording new responses as well as calling to the server. This provides
closed loop testing. During development the use of `pytest --vcr-record=once`. Use of this will an error to be raised for new 
requests if there is a cassette file while recording new interactions if there is now cassette file.


In order to get the most out of your `pytests` we have implemented the use of
- pytest-cov
- pytest-picked
- pytest-random-order
- pytest-sugar
- pytest-xdist

Most of these do not need configuration:

Full use of local running of tests is done by `pytest --vcr-record=none -n 4 --random-order`

`--random-order` ensures that tests run in a random order to uncover any issues with order dependent tests.

`-n 4` allows tests to run in parallel using the number of cores your CPU has. In this case, 4.

`--vcr-record=none` prevents external calls


#### Coverage report

Pytest-cov provides coverage reports for testing. In order to use this feature, append the 
`--cov=lighthouse` to the end of your pytest commands.

`pytest --vcr-record=none -n 4 --random-order --cov=lighthouse`


### CI Tests

CI setup will require the correct environment variables to be specified. Check the Environment Variables section.

The full command to run is `pytest --vcr-record=none --random-order`

This will prevent VCR from recording new cassettes. This also ensures that all tests are run on local cassettes preventing unexpected results in
API calls and returns. Use of this method also allows for removal of tokens and other sensitive data from configuration files.


## Development tools

### Juypter Lab
Lighthouse uses `juypter lab` as an interactive web based shell and notebook management tool. This allows for easy testing and
quick hacking as well as inspection of running code. More information on Jupyter Labs can be found in its
[documentation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)

Notebooks are excluded from git by default. Saving and sharing notebooks is an effective way to demonstrate a 
bug or functionality without having to pass full code bases around.

### iPython

[iPython](https://ipython.readthedocs.io/en/stable/) is a part of the Labs components but can be use separate from the labs.
iPython provides a host of tools that allow for command line REPL and introspection to python code. This is an upgraded version of the standard
`python` command.

To use simply type `ipython` at your prompt. Use of `ipython --debug` will show all auto-loaded libraries and paths.


### Examples of Command Parsers
There are examples of both simple and complicated commands in the examples folders.

[examples](./examples)


## Additional notes
We have [Max Brennerm](https://github.com/brennerm) to thank for CheckMk implementation
of [Python CheckMk Web Api](https://github.com/brennerm/check-mk-web-api). We are grateful.
