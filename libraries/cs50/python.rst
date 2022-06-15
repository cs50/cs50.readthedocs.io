.. default-domain:: py
.. highlight:: python

============================
CS50 Library for Python
============================

Installation
============

.. code-block:: bash

    $ pip3 install cs50

Usage
=====

.. note::
    To use these functions, be sure to include ``import cs50`` atop your file.


.. function:: cs50.get_float(prompt)

    :param prompt: the :py:class:`str` with which to prompt the user for input

    :returns: the :py:class:`float` equivalent to the line read from stdin as precisely as possible, or `None` on error

    Prompts user for a line of text from standard input and returns the equivalent :py:class:`float`;
    if text does not represent a floating-point value or would cause overflow or underflow, user is reprompted.

    Example usage::

        f = get_float("Input a floating-point number: ")


.. function:: cs50.get_int(prompt)

    :param prompt: the :py:class:`str` with which to prompt the user for input

    :returns: the :py:class:`int` equivalent to the line read from stdin, or `None` on error

    Prompts user for a line of text from standard input and returns the equivalent :py:class:`int`;
    if text does not represent an integer, user is reprompted.

    Example usage::

        f = get_int("Input an integer: ")


.. function:: cs50.get_string(prompt)

    :param prompt: the :py:class:`str` with which to prompt the user for input

    :returns: the read line as a string sans line endings, or `None` on EOF.

    Prompts user for a line of text from standard input and returns it as a :py:class:`str`,
    sans trailing line ending. Supports CR (``\r``), LF (``\n``), and CRLF (``\r\n``) as line
    endings.

    Example usage::

        s = get_string("Input a string: ")


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

    Any argument whose value is a :py:class:`list` or :py:class:`tuple` of other values is converted to a comma-separated list of those values, formatted for SQL's ``IN`` operator. Any argument whose value is `None` is converted to `NULL` for SQL.

    :returns: 
        - for ``CREATE``, ``True`` on success or ``False`` on failure
        - for ``DELETE``, the number of rows deleted
        - for ``INSERT``, the primary key of a newly inserted row (or ``None`` if none)
        - for ``SELECT``, a :py:class:`list` of :py:class:`dict` objects, each of which represents a row in the result set
        - for ``UPDATE``, the number of rows updated
        - on integrity errors, a :py:class:`ValueError` is raised
        - on other errors, a :py:class:`RuntimeError` is raised

    Example usage::

        import cs50

        db = cs50.SQL("sqlite:///file.db")

        rows = db.execute("SELECT * FROM foo")

        rows = db.execute("SELECT * FROM foo WHERE bar = ? AND baz = ?", 1, 2)
        rows = db.execute("SELECT * FROM foo WHERE bar IN (?) AND baz IN (?)", [1, 2], [3, 4])

        rows = db.execute("SELECT * FROM foo WHERE bar = :bar AND baz = :baz", bar=1, baz=2)
        rows = db.execute("SELECT * FROM foo WHERE bar IN (:bar) AND baz IN (:baz)", bar=[1, 2], baz=[3, 4])

        id = db.execute("INSERT INTO foo (bar, baz) VALUES(?, ?)", 1, 2)
        id = db.execute("INSERT INTO foo (bar, baz) VALUES(:bar, :baz)", bar=1, baz=2)

        n = db.execute("UPDATE foo SET bar = ?, baz = ?", 1, 2)
        n = db.execute("UPDATE foo SET bar = :bar, baz = :baz", bar=1, baz=2)

        n = db.execute("DELETE FROM foo WHERE bar = ? AND baz = ?", 1, 2)
        n = db.execute("DELETE FROM foo WHERE bar = :bar AND baz = :baz", bar=1, baz=2)

FAQs
====

How can I use ``%`` with ``LIKE``?
----------------------------------

If ``s`` is a :py:class:`str`, you can prepend and/or append ``%`` to it as follows:

    .. code-block::

        rows = db.execute("SELECT * FROM foo WHERE bar LIKE ?", "%" + s + "%")

How can I add optional clauses to a query?
------------------------------------------

Based on user input, you might want to include or not include some clauses in a query. For instance, you might want to include `bar` and `baz` in a query only if they have values, in which case the number of placeholders you have in your query might vary. You could thus construct your query dynamically by joining the clauses and unpacking the placeholders' values as follows:

    .. code-block::

        query = "SELECT * FROM foo"

        clauses = []
        values = []

        if bar:
            clauses.append("bar = ?")
            values.append(bar)
        if baz:
            clauses.append("baz = ?")
            values.append(baz)

        if clauses:
            query = query + " WHERE " + " AND ".join(clauses)
        rows = db.execute(query, *values)

The end result is equivalent to:

    .. code-block::

        rows = db.execute("SELECT * FROM foo WHERE bar = ? AND baz = ?", bar, baz)

But you don't need to know in advance if `bar` and `baz` will have values.

How come I can't use parameter markers as placeholders for tables' or columns' names?
-------------------------------------------------------------------------------------

Parameter markers (e.g., ``?``) can only be used as placeholders for "literals" like integers and strings, not for "identifiers" like tables' and columns' names. If a user's input will determine the table or column on which you execute a statement, you can use a format string (f-string) instead, but **you must validate the user's input first, to ensure the table or column exists, lest you risk a SQL-injection attack**, as in the below:

    .. code-block::

        if column in ["foo", "bar", "baz"]:
            rows = db.execute(f"SELECT * FROM {column}")

How can I enable logging of SQL statements?
-------------------------------------------

By default, logging of SQL statements is disabled unless you have an environment variable called ``FLASK_ENV``, the value of which is ``development``, as is the case in `Visual Studio Code for CS50 <https://cs50.readthedocs.io/code/>`_. You can enable logging of SQL statements with code like:

    .. code-block::

        import logging

        logging.getLogger("cs50").disabled = False

Statements that succeed will be prefixed with ``INFO``. Statements that fail will be prefixed with ``ERROR``.

How can I disable logging of SQL statements?
--------------------------------------------

To disable logging of SQL statements, even if you have an environment variable called ``FLASK_ENV``, the value of which is ``development``, as is the case in `Visual Studio Code for CS50 <https://cs50.readthedocs.io/code/>`_, you can use code like:

    .. code-block::

        import logging

        logging.getLogger("cs50").setLevel("CRITICAL")

Troubleshooting
===============

ModuleNotFoundError: No module named '_sqlite3'
-----------------------------------------------

If on an ``apt``-based system, try:

    .. code-block::

        apt install libsqlite3-dev

If on a ``yum``-based system, try:

    .. code-block::

        yum install sqlite-devel
