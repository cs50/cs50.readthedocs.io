# Heroku

[Heroku](https://www.heroku.com/) is a "platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud." Heroku even offers a [free plan](https://www.heroku.com/pricing).

Here's how to deploy your implementation of, say, [C$50 Finance](https://cs50.harvard.edu/x/2020/tracks/web/finance/) to Heroku from GitHub.

1. Watch [Brian's seminar](https://youtu.be/MJUJ4wbFm_A) to learn about `git` and GitHub, if not already familiar.

1. Sign up for free, private GitHub repositories at <https://education.github.com/discount_requests/new>, if you haven't already.

1. Create a new **private** repository at <https://github.com/new> (called, e.g., `finance`).

1. Take note of the **HTTPS** URL of the repository (e.g., `https://github.com/username/finance.git`, where `username` is your own GitHub username).

1. Change to your `finance` directory in CS50 IDE, as via `cd`.

1. Create a `git` repo therein.

    ```
    git init
    ```

1. Add the GitHub repository as a "remote," where `username` is your own GitHub username.

    ```
    git remote add origin https://github.com/username/finance.git
    ```

1. In the `requirements.txt` file inside of your `finance` directory, add `gunicorn` and `psycopg2`, each on separate lines.

1. Push your code to GitHub.

    ```
    git add -A
    git commit -m "first commit"
    git push -u origin master
    ```
    If you visit `https://github.com/username/finance`, where `username` is your own GitHub username, you should see your code in the repository.

1. Sign up for a free Heroku account at <https://signup.heroku.com/>, if you don't have one already.

1. Create a new app at <https://dashboard.heroku.com/new-app>.

1. Configure your app at `https://dashboard.heroku.com/apps/app-name/deploy/github`, where `app-name` is your Heroku app's name.

    * **Add this app to a pipeline:** No need to configure; leave as is.

    * **Deployment method:** Select **GitHub**, then click **Connect to GitHub**. If prompted to log into GitHub, click **Authorize heroku**.

    * **App connected to GitHub:** Search for your app's repository (e.g., `username/finance`, where `username` is your own GitHub username), then click **Connect**.

    * **Automatic deploys:** Click **Enable Automatic Deploys**.

1. Configure your app at `https://dashboard.heroku.com/apps/app-name/settings`, where `app-name` is your Heroku app's name.

    1. Click **Reveal Config Vars**.

    1. Add a new variable called **API_KEY**, the value of which is your API token for IEX. Recall that, after registering for a developer account at <https://iexcloud.io/>, you can obtain your API token under **API Tokens**. Be sure to use your **PUBLISHABLE** token as the value for **API_KEY**, not your **SECRET** token.

1. Search for and provision **Heroku Postgres** at `https://dashboard.heroku.com/apps/app-name/resources`, where `app-name` is your Heroku app's name; select a **Plan name** of **Hobby Dev — Free**.

1. At `https://dashboard.heroku.com/apps/app-name/resources`, where `app-name` is your Heroku app's name, click **Heroku Postgres :: Database**. In the tab that opens, click **Settings**, then click **View Credentials...**. Highlight and copy the **URI** that appears.

1. In CS50 IDE, open `application.py` in `finance/` and replace

    ```py
    db = SQL("sqlite:///finance.db")
    ```

    with

    ```py
    db = SQL(os.getenv("DATABASE_URL"))
    ```

    so that the CS50 Library will connect to your PostgreSQL database instead of your SQLite database. Be sure to add

    ```py
    import os
    ```

    atop `application.py`, if not there already.

1. In CS50 IDE, execute the below to import `finance.db` into your PostgreSQL database, where `URI` is that same URI. Be sure to append `?sslmode=require` to the URI.

    ```
    pgloader --no-ssl-cert-verification finance.db URI?sslmode=require
    ```

    Thereafter, if you'd like to browse or edit your PostgreSQL database, you can use Adminer (a tool like phpLiteAdmin for PostgreSQL databases), at [adminer.cs50.net](https://adminer.cs50.net/). Log in using your database's credentials: at `https://dashboard.heroku.com/apps/app-name/resources`, where `app-name` is your Heroku app's name, click **Heroku Postgres :: Database**. In the tab that opens, click **Settings**, then click **View Credentials...**.

1. Create a new file in CS50 IDE called `Procfile` in `finance/` whose contents are:

    ```
    web: gunicorn application:app
    ```

   That file will tell Heroku to look in a file called `application.py` for a variable called `app` and serve it with [Gunicorn](http://gunicorn.org/), a production-quality web server. (Flask's built-in web server is "good enough for testing but probably not what you want to use in production.")

1. Add that file to your repository and push it to GitHub.

    ```
    git add -A
    git commit -m "added Procfile"
    git push
    ```

    If you visit `https://app-name.herokuapp.com/`, where `app-name` is your Heroku app's name, you should see your app! If you instead see some error, visit `https://dashboard.heroku.com/apps/app-name/logs`, where `app-name` is your app's name, to diagnose! Each time you add (new or changed) files to your repository and push to GitHub hereafter, your app will be re-deployed to Heroku.
