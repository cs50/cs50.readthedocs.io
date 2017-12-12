---
toc: left
---

# Heroku

Here's how to deploy your implementation of [C$50 Finance](https://docs.cs50.net/2017/fall/psets/7/finance/finance.html) to Heroku from GitHub.

1. Watch [Brian's seminar](https://youtu.be/MJUJ4wbFm_A) to learn about `git` and GitHub, if not already familiar.

1. Sign up for free, private GitHub repositories at <https://education.github.com/discount_requests/new>, if you haven't already.

1. Create a new **private** repository at <https://github.com/new> (called, e.g., `finance`).

1. Take note of the **HTTPS** URL of the repository (e.g., `https://github.com/username/finance.git`, where `username` is your own GitHub username).

1. Change to your implementation's directory on CS50 IDE.

    ```
    cd ~/workspace/pset7/finance/
    ```

1. Create a `git` repo therein.

    ```
    git init
    ```

1. Add the GitHub repository as a "remote," where `username` is your own GitHub username.

    ```
    git remote add origin https://github.com/username/finance.git
    ```

1. Push your code to GitHub.

    ```
    git commit -am "first commit"
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

1. Search for and provision **Heroku Postgres** at `https://dashboard.heroku.com/apps/app-name/resources`, where `app-name` is your Heroku app's name; select a **Plan name** of **Hobby Dev — Free**.

1. At `https://dashboard.heroku.com/apps/app-name/resources`, where `app-name` is your Heroku app's name, click **Heroku Postgres :: Database**. In the tab that opens, click **Settings**, then click **View Credentials...**. Highlight and copy the **URI** that appears.

1. In CS50 IDE, open `application.py` in `~/workspace/pset7/finance/` and find:

    ```py
    db = SQL("sqlite:///finance.db")
    ```

    Replace `sqlite:///finance.db` with that URI (so that the CS50 Library will connect to your Postgres database instead of your SQLite database).

1. In CS50 IDE, execute the below to import `finance.db` into your Postgres database, where `URI` is that same URI. Be sure to append `?sslmode=require` to the URI.

    ```
    pgloader finance.db URI?sslmode=require
    ```

    Thereafter, if you'd like to browse or edit your Postgres database, you can use Adminer (a tool like phpLiteAdmin for Postgres databases), which is installed on CS50 IDE. To launch Adminer, execute

    ```
    adminer50
    ```

    and visit the outputted URL. Log in using your database's credentials: at `https://dashboard.heroku.com/apps/app-name/resources`, where `app-name` is your Heroku app's name, click **Heroku Postgres :: Database**. In the tab that opens, click **Settings**, then click **View Credentials...**. 

1. Create a new file in CS50 IDE called `Procfile` in `~/workspace/pset7/finance/` whose contents are:

    ```
    web: gunicorn application:app
    ```

   That file will tell Heroku to look in a file called `application.py` for a variable called `app` and serve it with [Gunicorn](http://gunicorn.org/), a production-quality web server. (Flask's built-in web server is "good enough for testing but probably not what you want to use in production.")

1. Add that file to your repository and push it to GitHub.

    ```
    git add -am "added Procfile"
    git push
    ```

    If you visit `https://app-name.herokuapp.com/`, where `app-name` is your Heroku app's name, you should see your app! If you instead see some error, visit `https://dashboard.heroku.com/apps/app-name/logs`, where `app-name` is your app's name, to diagnose! Each time you add (new or changed) files to your repository and push to GitHub hereafter, your app will be re-deployed to Heroku.
