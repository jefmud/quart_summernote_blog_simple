# quart_summernote_blog_simple
A simple blog built on Quart, Summernote (WYSIWIG editor) and TinyMongo

intent:

This small program is intended to demonstrate a simple blog built on Phil Jones' Quart microframework.  It wouldn't take much to flesh this out with user authentication (flask_login) and a simple administrative interface.

Quart asyncio (https://github.com/pgjones/quart)

**Quart is an ASYNC superset of Flask.**  The project takes some of the strongest features of Armin Ronacher's Flask project and moves it into the Python 3 asynchronous realm.  Porting simple Flask apps to Quart is relatively trivial, but you should look carefully at their documentation.  Some of the Flask addons will work with a "monkey patch" (quart.flask_ext).  See the documentation and examples for details.

**Summernote** - a very nice JavaScript WYSIWYG editor (https://github.com/summernote/summernote).

All the styling and support come from Bootstrap 4 using a CDN for simplicity.  The page templates could be easily changed to locally served static JavaScript (JQuery) and CSS.

**TinyMongo** - serves as a simple database.

I like to think of it as a SQLite local version of PyMongo (https://github.com/schapman1974/tinymongo)

The TinyMongo could be easily changed to PyMongo with a remote database.  But for simplicity, we keep the files local.

The structure is simple enough to be replaced by any other sort of database/ORM, i.e. SQLAlchemy, PeeWee, etc.
