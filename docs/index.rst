=============
atsphinx-feed
=============

Overview
========

This is sphinx-extension to generat RSS feed from "article" contents of documentation.
In this, "article" are documents added ``og-article`` directive by :pypi:`atsphinx-og-article`.

This collects documents with directive and generates RSS feed file (atom format) from them.

Installation
============

.. todo:: This is scheduled method.

.. code-block:: console

   pip install atsphinx-feed

This includes :pypi:`atsphinx-og-article` as dependencies.

.. code-block:: python

   extensions = [
       "atsphinx.og_article",  # Recommended
       "atsphinx.feed",
   ]
   # If "atsphinx.og_article" does not added, atsphinx-feed install it automately.

Usage
=====

When you run build by ``html`` -like builders, extension run work autometaly.
This generate RSS file into ``/feed.xml`` on your output directory.

Configuration
=============

.. todo:: Write it