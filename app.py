import functions
from classes import Car
from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", cars=functions.load())

@app.route('/add')
def add():
    name=request.args["name"]
    year=request.args["year"]
    color=request.args["color"]
    number=request.args["number"]
    owner=request.args["owner"]
    last_visit=request.args["last_visit"]
    last_fixup=request.args["last_fixup"]
    functions.add(name=name, year=year, color=color, number=number, owner=owner, last_visit=last_visit, last_fixup=last_fixup)
    return redirect(url_for('home'))

@app.route('/delete')
def delete():
    name=request.args["name"]
    number=request.args["number"]
    functions.delete(name,number)
    return redirect(url_for('home'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method=='POST':
        name=request.form["name"]
        year=request.form["year"]
        color=request.form["color"]
        number=request.form["number"]
        owner=request.form["owner"]
        last_visit=request.form["last_visit"]
        last_fixup=request.form["last_fixup"]
        functions.update(name, year, color, number, owner, last_visit, last_fixup)
        return redirect(url_for('home'))
    else:
        name=request.args["name"]
        year=request.args["year"]
        color=request.args["color"]
        number=request.args["number"]
        owner=request.args["owner"]
        last_visit=request.args["last_visit"]
        last_fixup=request.args["last_fixup"]
        return render_template("update.html", name=name, year=year, color=color, number=number, owner=owner, last_visit=last_visit, last_fixup=last_fixup)
    
@app.route('/profile')
def profile():
    name=request.args["name"]
    year=request.args["year"]
    color=request.args["color"]
    number=request.args["number"]
    owner=request.args["owner"]
    last_visit=request.args["last_visit"]
    last_fixup=request.args["last_fixup"]
    return render_template("profile.html", name=name, year=year, color=color, number=number, owner=owner, last_visit=last_visit, last_fixup=last_fixup)

@app.route('/search')
def search():
    query=str(request.args["query"])
    results=functions.search(query=query)
    return render_template("index.html", cars=results)


