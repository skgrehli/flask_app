# App

# Todo
- Basic functionality, [1](https://www.codeproject.com/Articles/1255416/Simple-Python-Flask-Program-with-MongoDB).
    - On append-ticket page:
        1. List all open tickets (id, instrument).
        2. When ticket is clicked, show form to add lot.
        3. Recalculate in EUR.
    - Om index/dashboard (will be merged):
        1. Display open positions with exposures etc.
        2. Display metrics such as average loss, average profit.
        3. Display feed.
- Merging RSS-feeds without Zapier, [1](https://bit.ly/2VSJEil)

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

---

## 3. Security
### 3.1. Password protection
Documentation on BasicAuth can be found [here](). To protect a single page, set `app.config['BASIC_AUTH_FORCE']` to `False` and define the route as the following:
```
@app.route('/secret')
@basic_auth.required
def secret_view():
    return render_template('secret.html')
```

---

## X. Future functionality
- Heroku Private Spaces to prevent unauthorized access to db, [guide](https://www.mongodb.com/blog/post/integrating-mongodb-atlas-with-heroku-private-spaces).