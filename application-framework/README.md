# Application Framework

App Engine is a good home for web applications, and web applications are
often built using a web framework.

The first public versions of App Engine supported a framework called 
[webapp](https://cloud.google.com/appengine/docs/standard/python/refdocs/google.appengine.ext.webapp).
Webapp was deprecated, but the open source
[webapp2](https://webapp2.readthedocs.io/en/latest/) framework is still
popular for Python 2.7 apps. That framework does not support Python 3, so
other frameworks must be used to migrate your web applications to
App Engine for Python 3.

The popular frameworks [Flask](https://flask.palletsprojects.com/en/1.1.x/)
and [Django](https://www.djangoproject.com/) work well with Python 2.7 and
Python 3, so a good migration strategy for existing webapp2 apps is:

1. Replace the use of webapp2 in your Python 2.7 app with Flask
   or Django, while remaining on App Engine for Python 2.7.

1. When the updated app is stable, migrate the code to Python 3 and deploy
   and test using App Engine for Python 3.

Flask is a micro-framework that is quite similar in scope to webapp2, and is
a good choice for this migration task. Some of the key changes between them
are shown in this table:

| Framework | webapp2 | Flask |
| --- | --- | --- |
| import statement | `import webapp2` | `from flask import Flask` |
| initialization | `app = webapp2.WSGIApplication([])` | `app = Flask(__name__)` |
| routing | defined at initialization,<br>as (_route_, _Class Name_) pairs, e.g.,<br> `app = webapp2.WSGIapplication([`<br> &nbsp;&nbsp;&nbsp;&nbsp;` ('/', HandlerClass)`<br>`])` | decorators, e.g., <br> `@app.route('/', methods=['GET'])` |
| handlers | class methods, named for HTTP verb, e.g.,<br> `class MainPage(webapp2.RequestHandler):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`def get(self):`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`self.response.write('Hello, World!')` | decorated methods, any name, e.g.,<br> `@app.route('/', methods=['GET'])`<br>`def hello():`<br>&nbsp;&nbsp;&nbsp;&nbsp;`return 'Hello, World!'` |
| "Hello, world" examples | [GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/appengine/standard/hello_world/main.py) | [GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/appengine/standard/flask/hello_world/main.py) |

Due to the minimal nature of the webapp2 framework, migration to Flask is
generally straightforward. See the "Hello, world" examples linked above
to survey the process.
