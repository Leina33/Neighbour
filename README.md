# Neighbourhoo's website

A personal blogging website where you can create and share your opinions and other users can read and comment on them.

## Built By [DOMINIC RUTTO](https://github.com/Leina33/)

A neighbourhood website where you can reach out and share your activities with your neighbours and other users can views and on them. You can view the site at: https://dominic-pics.herokuapp.com

## Description

## User Stories

These are the behaviours/features that the application implements for use by a user.
As a user I would like to:

- See the pictures i posted
- save them
- check on caption location
- check on category

## Specifications

| Behaviour                            |            Input             |                                                               Output |
| :----------------------------------- | :--------------------------: | -------------------------------------------------------------------: |
| Display pictured                     |       **On page load**       |             List of various images sources is displayed per category |
| Display categories                   |      **Click on image**      |           Redirected to a page with a list of images from the source |
| Display location and date posted     |       **On page load**       |              Each image displays an location, description and author |
| Read an entire desc                  | **check category sub-title** | Redirected to the picked category source's site to read entire pitch |
| Go back to website category you need |        **Click Home**        |                                  Redirected to the post a pitch area |

## SetUp / Installation Requirements

### Prerequisites

- python3.6
- pip
- virtualenv
- psql database

### Cloning

- In your terminal:
  \$ git clone https://github.com/Leina33/Gallery.git

## Running the Application

- Creating the virtual environment
  $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
- Installing Django and other Modules
  $ python3.6 -m pip install djang0==1.11
        $ python3.6 -m pip install Flask-Bootstrap4
  $ python makemigration photos
        $ python manage.py migrate
  $ pip install psycopg2
        $ pip install pyuploadcare
  #check on requirements.txt file
- To run the application, in your terminal:
  \$ python3.6 manage.py runserver

## Testing the Application

- To run the tests for the class files:
  $ cd app
        $ python3.6 test.py

## Technologies Used

- Python3.6
- Django
- Html
- Bootstrap4

## License

MIT &copy;2019 [DOminic Rutto](https://github.com/Leina33)
