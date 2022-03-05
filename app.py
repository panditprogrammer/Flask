from datetime import datetime
from flask import Flask, redirect,render_template, request

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



# CREATE APP AND CONFIGURE 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///myDatabase.db' # database config 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
mydb = SQLAlchemy(app)



# CREATE CLASS FOR TODO APP 
class Todo(mydb.Model):
    s_number = mydb.Column(mydb.Integer, primary_key = True)
    title = mydb.Column(mydb.String(200), nullable = False)
    desc = mydb.Column(mydb.String(500), nullable = False)
    create_date = mydb.Column(mydb.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.s_number} => {self.title}"



# # our first route 
# @app.route("/")
# def Home():
#     return "Hello World"


@app.route("/", methods = ['GET','POST'])
def home():
    # get the form data 
    if request.method == 'POST':
        form_title = request.form["title"]
        form_desc = request.form["desc"]
        # save the form data in database
        todo = Todo(title=form_title,desc=form_desc)
        mydb.session.add(todo)
        mydb.session.commit()

    # get all the data from database 
    AllTodo = Todo.query.all()
    return render_template("index.html", allData = AllTodo)


# delete the todo item 
@app.route("/delete/<int:sn>")
def deleteTodo(sn):
    todo = Todo.query.filter_by(s_number = sn).first()
    
    mydb.session.delete(todo)
    mydb.session.commit()
    return redirect("/")

# update the todo item 
@app.route("/edit/<int:sn>", methods=["GET","POST"])
def updateTodo(sn):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(s_number = sn).first()
        todo.title = title
        todo.desc = desc
        mydb.session.add(todo)
        mydb.session.commit()
        return redirect ("/")

    todo = Todo.query.filter_by(s_number = sn).first()
    return render_template("edit.html",todoData = todo)


# @app.route("/add")
# def addTodo(title,desc):
#     todo = Todo(title,desc)
#     mydb.session.add(todo)
#     mydb.session.commit()
#     return "add todo "


if __name__ == "__main__":
    app.run(debug=False)

