# App Engine Migration Guide

This is repository is a guide for developers
needing to move the App Engine Standard for Python 2.7 apps to App Engine
Standard for Python 3.8. Many of the steps here would also be helpful if the
target environment were another Python 3.x system.

Community contributions of examples of migration challenges people have
encountered and overcome are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md)
for how to offer a contribution. In a nutshell, you should fork this
repository, add your examples, and then submit a pull request. We will review
the request and ask you to sign a Contributor License Agreement before merging
the it.

## Contributing changes

* See [CONTRIBUTING.md](CONTRIBUTING.md)

## Licensing

* See [LICENSE](LICENSE)

## Planning for migration

Migrating an app from App Engine Standard for Python 2.7
system to App Engine Standard for Python 3.8 necessarily
involves making the code compliant with
Python 3.8. It is possible to do that while having the code continue to run
properly under Python 2.7. There are many guides available on how to do this,
such as the standard Python documentation for Porting Python 2 Code to
Python 3. This guide defers to those other sources on how to make such
needed changes. Instead, this guide focuses on the specific App Engine
changes that must be addressed.

The first step in migrating your app is to identify the
features it uses that are not available in the current runtime. These may include:

* An application framework, such as webapp or webapp2, that cannot run under Python 3.x.
* Bundled libraries that are being used:
  * Blobstore
  * Datastore
  * Images
  * Logging
  * Mail
  * Memcache
  * Task queue
  * URL fetch
  * User authentication

Developers should identify which of these issues apply to their app, and
address them one at a time in a way that continues to work under Python 2
in the Gen 1 environment, but will also work once the app is moved to
Python 3 in the Gen 2 environment. Migration strategies and software samples
are provided for each of these areas in the following sections.

## Hands-on experience

If you're starting or looking into Python 2 to 3 migration from the first-gen to second-gen App Engine runtimes, Google is going to try to help you so you don't have to both port from 2.x to 3.x **and** move from bundled to unbundled services at the same time. One of those resources are a set of hands-on tutorials (called codelabs) along with a matching repo. Find them at https://github.com/googlecodelabs/migrate-python2-appengine ... they are meant to be complementary to the examples found here in this repo.
