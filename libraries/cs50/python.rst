.. default-domain:: py
.. highlight:: python

============================
CS50 Library for Python
============================

Installation
============

Ubuntu
-------

.. code-block:: bash

    $ sudo pip3 install cs50


Fedora
-------
.. code-block:: bash

    $ sudo pip3 install cs50


Usage
=====

.. note::
    To use these functions, make sure to include ``import cs50`` atop your file.


.. function:: cs50.get_float(prompt)

    :param prompt: the :py:class:`str` with which to prompt the user for input

    :returns: the :py:class:`float` equivalent to the line read from stdin as precisely as possible, or `None` on error

    Prompts user for a line of text from standard input and returns the equivalent :py:class:`float`;
    if text does not represent a floating-point value or would cause overflow or underflow, user is reprompted.

    Example usage::

        f = get_float("Enter a floating-point number: ")


.. function:: cs50.get_int(prompt)

    :param prompt: the :py:class:`str` with which to prompt the user for input

    :returns: the :py:class:`int` equivalent to the line read from stdin, or `None` on error

    Prompts user for a line of text from standard input and returns the equivalent :py:class:`int`;
    if text does not represent an integer, user is reprompted.

    Example usage::

        f = get_int("Enter an integer: ")


.. function:: cs50.get_string(prompt)

    :param prompt: the :py:class:`str` with which to prompt the user for input

    :returns: the read line as a string sans line endings, or `None` on EOF.

    Prompts user for a line of text from standard input and returns it as a :py:class:`str`,
    sans trailing line ending. Supports CR (``\r``), LF (``\n``), and CRLF (``\r\n``) as line
    endings.

    Example usage::

        s = get_string("Enter a string: ")


.. function:: cs50.SQL(url)

    :param url: a :py:class:`str` that indicates database dialect and connection arguments

    :returns: a :py:class:`cs50.SQL` object that represents a connection to a database

    Example usage::

        db = cs50.SQL("sqlite:///file.db")  # For SQLite, file.db must exist
        db = cs50.SQL("mysql://username:password@host:port/database")  # For MySQL
        db = cs50.SQL("postgres://username:password@host:port/database")  # For PostgreSQL


.. function:: cs50.SQL.execute(sql, *args, **kwargs)

    :param sql: a :py:class:`str` that represents a single SQL statement, possibly with `parameter markers <https://www.python.org/dev/peps/pep-0249/#paramstyle>`_, with or without a trailing semicolon
    :param \*args: zero or more positional arguments with which any parameter markers should be substituted
    :param \*\*kwargs: zero or more named arguments with which any parameter markers should be substituted

    Any argument whose value is a ``list`` or ``tuple`` of other values is converted to a comma-separated list of those values, formatted for SQL's `IN` operator.

    :returns: for ``SELECT``, a :py:class:`list` of :py:class:`dict` objects, each of which represents a row in the result set; for INSERTs, the primary key of a newly inserted row (or ``None`` if none); for ``UPDATE``, the number of rows updated; for ``DELETE``, the number of rows deleted; for ``CREATE``, ``True`` on success or ``False`` on failure; on integrity errors, a ``ValueError`` is raised, on other errors, a ``RuntimeError`` is raised

    Example usage::

        import cs50

        db = cs50.SQL("sqlite:///file.db")

        rows = db.execute("SELECT * FROM foo")

        rows = db.execute("SELECT * FROM foo WHERE bar = ? AND baz = ?", 1, 2)
        rows = db.execute("SELECT * FROM foo WHERE bar IN (?) AND baz IN (?)", [1, 2], [3, 4])

        rows = db.execute("SELECT * FROM foo WHERE bar = :bar AND baz = :baz", bar=1, baz=2)
        rows = db.execute("SELECT * FROM foo WHERE bar = :bar AND baz = :baz", {"bar": 1, "baz": 2})
        rows = db.execute("SELECT * FROM foo WHERE bar IN (:bar) AND baz IN (:baz)", bar=[1, 2], baz=[3, 4])

        id = db.execute("INSERT INTO foo (bar, baz) VALUES(?, ?)", 1, 2)
        id = db.execute("INSERT INTO foo (bar, baz) VALUES(:bar, :baz)", bar=1, baz=2)
        id = db.execute("INSERT INTO foo (bar, baz) VALUES(:bar, :baz)", {"bar": 1, "baz": 2})

        n = db.execute("UPDATE foo SET bar = ?, baz = ?", 1, 2)
        n = db.execute("UPDATE foo SET bar = :bar, baz = :baz", bar=1, baz=2)
        n = db.execute("UPDATE foo SET bar = :bar, baz = :baz", {"bar": 1, "baz": 2})

        n = db.execute("DELETE FROM foo WHERE bar = ? AND baz = ?", 1, 2)
        n = db.execute("DELETE FROM foo WHERE bar = :bar AND baz = :baz", bar=1, baz=2)
        n = db.execute("DELETE FROM foo WHERE bar = :bar AND baz = :baz", {"bar": 1, "baz": 2})
