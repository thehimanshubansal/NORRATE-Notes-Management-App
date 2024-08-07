
# Notes Web Application



## Overview
The Notes Web Application is a simple and intuitive platform for users to create, view, and manage their notes. Built using the Flask framework, this application demonstrates essential web development concepts, including routing, templating, form handling, and database integration.

## Features

1. **Home Page**:
   - It is the first page that will display and from where users can go to other pages.

2. **Add Note**:
   - A form where users can enter a new note.
   - Upon submission, the note is added to the list and stored in the database.

3. **Persistent Storage**:
   - Notes are stored in a SQLite database, ensuring they persist across server restarts.

4. **Styling**:
   - Basic CSS is applied to improve the user interface and enhance the user experience.

## Technical stack

- **Flask**: The core web framework used to handle routing, request handling, and response generation.
- **SQLAlchemy**: ORM (Object-Relational Mapping) tool used to interact with the SQLite database.
- **HTML/CSS**: Frontend technologies used to build and style the user interface.
## Application Structure


- **Project Directory**:
  - `app.py`: Main application file containing route definitions and application logic.
  - `templates/`: Directory containing HTML templates.
    - `base.html`: Base template that other templates extend from.
    - `home.html`: Template for the home page displaying the list of notes.
    - `add_note.html`: Template for the page where users can add a new note.
  - `static/`: Directory containing static files like CSS.
    - `styles.css`: CSS file for styling the application.

## Challenges left out

- Login in/ Sign in and authentication functionality yet to be made.
- Some notes management tasks are pending like grouping and deletion of notes.
- Hosting of website is not done.

## Authors

- [@thegyanvirsingh](https://www.github.com/thegyanvirsingh)
- [@khushi7lakra](https://github.com/khushi7lakra)
- [@thehimanshubansal](https://www.github.com/thehimanshubansal)

