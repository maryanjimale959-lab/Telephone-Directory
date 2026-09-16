import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DATA_FILE = "directory.json"

def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

@app.route("/")
def index():
    query = request.args.get("search", "").strip().lower()
    contacts = load_contacts()
    
    if query:
        filtered = {
            name: info for name, info in contacts.items() 
            if query in name.lower() or query in info.get("phone", "").lower() or query in info.get("email", "").lower()
        }
        return render_template("index.html", contacts=filtered, search_query=query)
    
    return render_template("index.html", contacts=contacts, search_query="")

@app.route("/add", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip()

        if name and phone:
            contacts = load_contacts()
            contacts[name] = {"phone": phone, "email": email}
            save_contacts(contacts)
            return redirect(url_for("index"))
            
    return render_template("add.html")

@app.route("/edit/<name>", methods=["GET", "POST"])
def edit_contact(name):
    contacts = load_contacts()
    
    if name not in contacts:
        return redirect(url_for("index"))
        
    if request.method == "POST":
        new_phone = request.form.get("phone", "").strip()
        new_email = request.form.get("email", "").strip()
        
        if new_phone:
            contacts[name]["phone"] = new_phone
            contacts[name]["email"] = new_email
            save_contacts(contacts)
            return redirect(url_for("index"))
            
    contact = contacts[name]
    return render_template("edit.html", name=name, contact=contact)

@app.route("/delete/<name>", methods=["POST"])
def delete_contact(name):
    contacts = load_contacts()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)