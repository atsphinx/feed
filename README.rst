=============
atsphinx-feed
=============

Simple RSS feed generator based Open Graph.

Oviewview
=========

Sphinx extension to add RSS feed of documents.

This is using ``atsphin-og-article``, and pick documents included ``og-article`` directive.
You can select only documents that you want to notify as RSS.

Getting started
===============

Install from PyPI.

.. code:: console

   pip install atsphinx-feed

Configure your ``conf.py``.

.. code:: python

   extensions = [
       "atsphinx.feed",
       "atsphinx.og_article",
   ]

When you build by html-like builder, this generates Atom style feed file into outdir.

.. code:: plain

  - _build/html/
    + index.html
    + atom.xml <- Generated!!
    - _static/

You can configure behevior of extension.
Please see docs.
