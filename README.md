# Python-Flask Tutorial for absolute beginner's

## 1 create a virtual env 
```
env MyenvName

 ```

## 2 select env or activate env
```
MyenvName\Scripts\activate.bat  
```
## 3 Install Flask and flask_sqlalchemy

```
pip install flask
pip install Flask-SQLAlchemy
```

## 4 Create New File 'app.py' and configure flask app with sqlite database
```
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///myDatabase.db'    
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
mydb = SQLAlchemy(app)

```
 
 ## 5 Create First route 
 ```
@app.route("/")
def home():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)


 ```

 ## 6 Run the flask app 
 ```
 flask run

 ```
 ### Set the debuger = True for developement and autoreload (ps,cmd)
 Powershell for Windows (goto documentation for mac or linux)
 ```
$env:FLASK_ENV = "development"
```
CMD for Windows
 ```
set FLASK_ENV=development
```

 Congratulations! you have successfully run the First Flask App.

 # Database Create and configurations Commands

 ## 1 First open python interpreter and import yourDatabase
 ```
 from app import Mydatabase
 ```
## 2 Create database and columns
```
Mydatabase.create_all()
``` 



# Flask Starter Template 

## create your first app in flask
Click here for documentation https://flask.palletsprojects.com/en/2.0.x/quickstart/


# Flask SQLAlchemy documentaions 
click here https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

