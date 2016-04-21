===============================
Multicast Socket
===============================

.. image:: https://img.shields.io/pypi/v/mcastsocket.svg
        :target: https://pypi.python.org/pypi/mcastsocket

..
    .. image:: https://img.shields.io/travis/mcfletch/mcastsocket.svg
            :target: https://travis-ci.org/mcfletch/mcastsocket

    .. image:: https://readthedocs.org/projects/mcastsocket/badge/?version=latest
            :target: https://readthedocs.org/projects/mcastsocket/?badge=latest
            :alt: Documentation Status


Provides a simple interface for configuring multicast socket services

* Free software: LGPL 2.1 license 

Sample Usage
------------

See docs/sample.py

.. literalinclude:: docs/sample.py
    :language: python 
    :linenos:

Migrating from `zeroconf.mcastsocket`
--------------------------------------

If you've been using the `forked zeroconf mcastsocket module <https://github.com/mcfletch/pyzeroconf>`_, just update your 
imports from::

    from zeroconf import mcastsocket 

to::

    from mcastsocket import mcastsocket 

and your code should continue to work.

Credits
---------

The original "how to work with multicast" code comes from PyZeroconf. The mcastsocket
module is largely new-code, but it does derive from the original PyZeroconf, so retains
its license (LGPL).

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
