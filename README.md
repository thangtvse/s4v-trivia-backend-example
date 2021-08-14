## Local development

- Install Python 3.9. https://www.python.org/downloads/
- Install Pycharm Community. https://www.jetbrains.com/pycharm/download/#section=mac  
- Open this repository in Pycharm
- Create Python virtual environment. https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env
- Execute run.py

## Push to Heroku
- Create an account on Heroku and create a new app (it's free for the first app). Heroku will ask you for the app name. Remember this name.
- Install Heroku CLI. https://devcenter.heroku.com/articles/heroku-cli
- Set your app as a remote of this repository:

```
heroku git:remote -a [your-app-name]
```

- Make some changes
- Create a commit
- Push code to Heroku:
```
git push heroku main
```