
- [Introduction](#introduction)
    - [Key Dependencies](#key-dependencies)
- [Tech Stack:](#tech-stack)
- [Main Files: Project Structure](#main-files-project-structure)
- [Development Setup](#development-setup)
- [Endpoints](#endpoints)

### Introduction

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server

### Tech Stack:

Our tech stack will include:

* **SQLAlchemy ORM** to be our ORM library of choice
* **PostgreSQL** as our database of choice
* **Python3** and **Flask** as our server language and server framework
* **Flask-Migrate** for creating and running schema migrations
* **HTML**, **CSS**, and **Javascript** with [Bulma](https://bulma.io/) for our website's frontend


### Main Files: Project Structure

```sh
casting-agency
├─ Procfile *** Procfile for heroku deployment
├─ README.md
├─ app.py *** The main driver of the app. "python app.py" to run after installing dependencies
├─ auth.py 
├─ manage.py
├─ migrations *** Migration folder keeping track on file migration
│  ├─ README
│  ├─ __pycache__
│  │  └─ env.cpython-38.pyc
│  ├─ alembic.ini
│  ├─ env.py
│  ├─ script.py.mako
│  └─ versions
│     ├─ 36701c375bcd_.py
│     └─ __pycache__
│        └─ 36701c375bcd_.cpython-38.pyc
├─ models.py *** Database models
├─ public
│  ├─ css
│  │  └─ main.css
│  └─ js
│     └─ app.js
├─ requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
├─ setup.sh *** Store ENV variable
├─ templates
│  └─ home.html
└─ test_app.py *** Tests for each endpoint
```

Overall:
* Models are located in the `models.py`.
* Controllers are located in `app.py`.
* The web frontend is located in `templates/`.


### Development Setup

First, [install Flask](http://flask.pocoo.org/docs/1.0/installation/#install-flask) if you haven't already.

  ```
  $ cd ~
  $ sudo pip3 install Flask
  ```

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

2. Install the dependencies:
  ```
  $ pip3 install -r requirements.txt
  ```

3. Run the development server:
  ```
  $ export FLASK_APP=app.py
  $ export FLASK_ENV=development # enables debug mode
  $ export FLASk_DEBUG=true #enable auto reload
  $ python3 app.py or flask run
  ```

4. Navigate to Home page [http://localhost:5000](http://localhost:5000)


### Endpoints
```GET/movies```

- Get all movies from db.
- Movies are returned as JSON object in the following format:
```
{
  "movies": [
    {
      "id": 1,
      "release_date": "Mon, 20 Aug 2018 00:00:00 GMT",
      "title": "Black Panther"
    }
  ],
  "success": true
}
```

```POST/movies```
- Adds a new movie to database
- Sample post request
```
{
  "title": "Black Panther",
  "release_date": "20 August 2018"
}
```
- If request is successful the response returned as JSON object in the following format.
```
{
  "message": "Successfully added",
  "movies": 1,
  "success": true
}
```
```DELETE/movies/<int:movie_id>```
- Delete movie from db.
- If request is successful the response returned as JSON object in the following format.
```
{
    "movies": 1,
    "message": "Successfully deleted.",
    "success": true
}
```

```PATCH/movies/<int:movie_id/>```
- Modified movies

If request is successful the response returned as JSON object in the following format.
```
{
  "movies": {
    "id": 3,
    "release_date": "Fri, 14 Oct 1994 12:03:45 GMT",
    "title": "The Shawshank Redemption"
  },
  "success": true
}
```
```GET/actors```

- Get all actors from db.
- Actors are returned as JSON object in the following format:
```
{
  "actors": [
    {
      "age": 30,
      "gender": "Female",
      "id": 1,
      "name": "Jennifer Lawrence"
    }
  ],
  "success": true
}
```

```POST/actors```
- Adds a new actor to database
- Sample post request
```
{
    "name": "Jennifer Lawrence",
    "age": 30,
    "gender": "Female"
}
```
- If request is successful the response returned as JSON object in the following format.
```
{
  "actors": 1,
  "message": "Actor successfully added.",
  "success": true
}
```
```DELETE/actors/<int:actor_id>```
- Delete an actor from db.
- If request is successful the response returned as JSON object in the following format.
```
{
    "movies": 1,
    "message": "Successfully deleted.",
    "success": true
}
```

```PATCH/actors/<int:actor_id/>```
- Modified actors

If request is successful the response returned as JSON object in the following format.
```
{
  "actors": {
    "age": 45,
    "gender": "Male",
    "id": 2,
    "name": "Leonado Dicaprio"
  },
  "message": "Successfully updated.",
  "success": true
}
```