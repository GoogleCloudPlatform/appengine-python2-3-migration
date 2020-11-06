# Migrating Datastore

Google Cloud Datastore is a widely used NoSQL database service. The
`google.appengine.ext.ndb` library (called legacy NDB throughout this
document) provides access to that service, but is only available
for App Engine Standard for Python 2.7 applications.

The `google.cloud.datastore` library can be used inside or outside App Engine
in either Python 2.7 or 3, so it is a possible stepping stone to migrating
older App Engine apps. However, that library has differently named methods
and parameter structures from the legacy NDB library. There is another
alternative available: `google.cloud.ndb` (called Cloud NDB hereafter).
Legacy NDB applications can be converted to Cloud NDB with only minimal changes,
and can run under Python 2.7 or 3, inside or outside App Engine.

Migrating an application from Legacy NDB to Cloud NDB requires new changes,
summarized in this table:

| | Legacy NDB | Cloud NDB |
| --- | --- | --- |
| import statement | `from google.appengine.ext import ndb` | `from google.cloud import ndb` |
| initialization | implicit | `client = ndb.Client()` |
| method names, parameters, and responses | same in both |
| method calls | `item.put()` | must be called in a context:<br>`with client.context():`<br>&nbsp;&nbsp;&nbsp;&nbsp;`item.put()` |
| data caching | automatic | explicitly use Redis:<br>`cache = ndb.RedisCache.from_environment()`<br>`with client.context(global_cache=cache):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`item.put()` |

There may be performance differences between using Legacy NDB and Cloud NDB,
with either one working better for your specific application. Updated apps
should be benchmarked to make sure there are no performance changes that
would harm the overall application.

Since both legacy NDB and Cloud NDB operate on Cloud Datastore, the Python
Datastore library `google.cloud.datastore` can be used instead of either
of them. This library has syntactic changes from the NDB libraries, but has
similar operations, allowing the migration. Cloud Datastore can be used in either
Python 2.7 and 3. Again, there may be performance differences depending on
which library is used, so updated performance-critical apps should be benchmarked.

| | Cloud NDB | Cloud Datastore |
| --- | --- | --- |
| import statement | `from google.cloud import ndb` | `from google.cloud import datastore ` |
| initialization | `client = ndb.Client()` | `client = datastore.Client()` |
| method names, parameters, and responses | `client.Key()`<br>Entities are class instances<br>`class_instance.put()`<br>`result = class.query()` | `client.key()`<br>`ent = datastore.Entity()`<br>`client.put(ent)`<br>`q = client.query(); result = q.fetch()` |
| method calls | must be called in a context | no context needed |
| data caching | explicitly use Redis | application must manage caching |

## Sample Application Three Ways

The changes needed to migrate from Legacy NDB to either Cloud NDB or Cloud
Datastore are demonstrated in the three sample applications in this folder. The
applications are functionally identical, and use the Datastore the same way,
but accessed with different Python libraries. If the applications are deployed
one after another in the same Google Cloud project, the data created by any
of them will be displayed by any other of them.

The application is a simple guest book where visitors can post a short text
and have it appear on the home page with everyone else's test. Those posts
can be grouped into differently named books, which can be created or just
navigated to by entering their name on the home page.

1. [Original Legacy NDB example](legacy-ndb). This application can only run
in App Engine Standard for Python 2.7 due to its use of the Legacy NDB
library.

1. [Cloud NDB example](cloud-ndb). The source code for this application is
almost identical to the Legacy NDB example, except that it uses the newer
Cloud NDB library, and must create a client object and place database operations
in a client context. This can run under Python 2.7 or Python 3, and can even
run outside of App Engine.

1. [Cloud Datastore example](cloud-datastore). When compared to the other
examples side-by-side, it is clear that this application has almost identical
steps and operations as the others, but with very different syntax and method
calls. In particular, using Cloud Datastore does not require creating a class
representing the entities, and library creates entities for your. As with the
Cloud NDB example, this can run under Python 2.7 or Python 3, and can run
inside or outside of App Engine.
