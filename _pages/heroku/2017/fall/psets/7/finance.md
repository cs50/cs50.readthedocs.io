---
toc: left
---

# Heroku

Here's how to deploy your implementation of [C$50 Finance](https://docs.cs50.net/2017/fall/psets/7/finance/finance.html) to Heroku from GitHub.

1. Watch [Brian's seminar](https://youtu.be/MJUJ4wbFm_A) to learn about `git` and GitHub, if not already familiar.

1. Sign up for free private repositories at <https://education.github.com/discount_requests/new>. 

1. Create a new **private** repository at <https://github.com/new> (called, e.g., `finance`).

1. Highlight and copy the **HTTPS** URL of the repository (e.g., `https://github.com/username/finance.git`, where `username` is your own GitHub username).

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
    git add -am "first commit"
    git push -u origin master
    ```
    If you visit `https://github.com/username/finance`, where `username` is your own GitHub username, you should see your code in the repository. 

1. Sign up for a free account at <https://signup.heroku.com/>, if you don't have one already.

1. Create a new app at <https://dashboard.heroku.com/new-app>.

1. Via the **Deploy** tab that appears, configure your app as follows.

    * **Add this app to a pipeline:** No need to configure; leave as is.

    * **Deployment method:** Select **GitHub**, then click **Connect to GitHub**. If prompted to log into GitHub, click **Authorize heroku**.

    * **App connected to GitHub:** Search for your app's repository (e.g., `username/finance`, where `username` is your own GitHub username), then click **Connect**.

    * **Automatic deploys:** Click **Enable Automatic Deploys**.

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

If you visit `https://app-name.herokuapp.com/`, where `app-name` is your Heroku app's name, you should see your app! If you instead see some error, visit `https://dashboard.heroku.com/apps/app-name/logs, where `app-name` is your app's name, to diagnose the issue!
