
import tracery
from tracery.modifiers import base_english
import json


from crypt import methods
from flask import Flask, request
from flask import render_template 

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    # return_make_re render_template("index.html")
    return render_template("index.html")


@app.route("/result", methods = ["POST" , "GET"])
def result():
    # output = request.form.to_dict()
    # name =' output["name"]'
        
    rules = {
        "origin": "#interjection.capitalize#, #name#! I'm #profession.a#, not #profession.a#!",
        "interjection": ["alas", "congratulations", "eureka", "fiddlesticks",
            "good grief", "hallelujah", "oops", "rats", "thanks", "whoa", "yes"],}

    names_data = json.loads(
        open("source/name.json").read())                      # load names from json file



    occupation_data = json.loads(
        open("source/job.json").read())                      # load 

    rules["name"] = names_data["name"]           # add names to rules
    rules["profession"] = occupation_data["job"]         

    # generate!
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    name =grammar.flatten("#origin#")
        

    return render_template("index.html", name=name)
if __name__ == "__main__":
    app.run(debug=True, port = 5001)




























