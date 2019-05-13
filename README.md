# App

# Todo
1. Why does it break on 'from . import app'?
2. Password protect Heroku or Flask app.

---

## 2. Installation
### 2.1. Getting started
1. Follow this [guide](https://medium.com/@manajitpal/auto-deployment-using-bitbucket-and-heroku-521b4271cc27) up until "Binding Heroku with Bitbucket".
2. Follow this [guide](https://code.visualstudio.com/docs/python/tutorial-flask) up until "Create and run a minimal Flask app".
3. Unzip setup-app.zip in repo.
4. Continue with the guide from step 1.

### 2.2. Dependencies
```
pip3 install pymongo
pip3 install dnspython
pip3 install quandl # also installs numpy and pandas
pip3 install beautifulsoup4
```

### 2.3. Commands
- Run virtual environment in VS Terminal with `source env/bin/activate`. This is only needed if (env) is exited in VS Terminal window.
- Run Flask app: `python3 -m flask run`, or using debugger `⌃F5`.
- Run Flask app outside VS Code debugger:
    1. Set an environment variable for `FLASK_APP`. On Linux and macOS, use export set `FLASK_APP=webapp`.
    2. In the `app` folder, launch the program using `python3 -m flask run`.