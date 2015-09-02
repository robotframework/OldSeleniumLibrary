Selenium test library for Robot Framework
=========================================

This library is **deprecated**. Please use `Selenium2Library
<https://github.com/robotframework/Selenium2Library>`_ instead.

Introduction
------------

SeleniumLibrary is a test library for Robot Framework that enables testing
of web applications. As the name suggests, it uses `Selenium tool
<http://selenium.openqa.org>`_ internally. Because it uses the deprecated
Selenium 1.0 version also the library itself is deprecated. All new projects
should use Selenium2Library_ and existing users are also recommended to upgrade
to it.

This projects has been migrated from dying `Google Code
<http://code.google.com/p/robotframework-seleniumlibrary/>`_.

Installation
------------

See `<INSTALL.rst>`__ for installation and uninstallation instructions.

Usage
-----

To run tests with Robot Framework and SeleniumLibrary following things 
must be done

- SeleniumLibrary must be taken into use in Robot test data.
  See `Robot Framework User Guide`__ for more information.
- Selenium server must be started with command 
  ``java -jar [path_to_server]/selenium_server.jar``, where ``[path_to_server]``
  depends on platform. On Windows it will be 
  ``[PythonDir]\Lib\site-packages\SeleniumLibrary\lib`` and on Linux it is
  typically something like
  ``/usr/lib/python[version]/site-packages/SeleniumLibrary/lib``. 

__ http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html

Documentation
-------------

General library usage and available keywords are documented in `library documentation
<http://robotframework.org/SeleniumLibrary/SeleniumLibrary.html>`_.

`Wiki <https://github.com/robotframework/SeleniumLibrary/wiki>`_ contains additional
information.

Directory Layout
-----------------

demo/
    A simple demonstration, with an application running on localhost.

doc/
    Keyword documentation.

src/
    Python source code.

test/
    Acceptance tests for keywords using Robot Framework.
