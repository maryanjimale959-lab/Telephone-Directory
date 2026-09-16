# Telephone-Directory
A modern, full-stack web application built with Python and Flask to manage contact records. Features dynamic search, full CRUD operations (add, edit, delete), persistent local JSON storage, and a responsive UI styled with Bootstrap 5.
#  Telephone Directory System

A clean, full-stack web-based Telephone Directory application built with Python and Flask. This system allows users to seamlessly manage contacts with full CRUD (Create, Read, Update, Delete) capabilities, instant search filtering, and persistent local data storage.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Framework-Flask-green.svg)
![Bootstrap](https://img.shields.io/badge/UI-Bootstrap%205-purple.svg)

---

## Features

- ** Complete Contact Management:** Add, view, edit, and delete contacts with ease.
- ** Dynamic Search:** Filter entries in real-time by name, phone number, or email address.
- ** Data Persistence:** Automatically saves all records to a local JSON database (`directory.json`) so data persists across sessions.
- ** Modern UI:** Designed with Bootstrap 5, FontAwesome icons, avatar letter badges, and custom responsive CSS.

---

##  Tech Stack

- **Backend:** Python 3, Flask
- **Frontend:** HTML5, CSS3, Bootstrap 5, Jinja2 Templating
- **Data Storage:** JSON (JavaScript Object Notation)

---

##  Project Structure

```text
telephone_directory/
│
├── app.py              # Main Flask application logic & routing
├── directory.json      # Persistent local database file
└── templates/          # HTML templates rendered by Flask
    ├── index.html      # Main directory dashboard & search view
    ├── add.html        # New contact creation form
    └── edit.html       # Contact details modification form
