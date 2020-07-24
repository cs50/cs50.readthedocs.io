.. default-domain:: c
.. highlight:: c

============================
CS50 Library for C
============================

Installation
============

Ubuntu
-------

.. code-block:: bash
    
    $ curl -s https://packagecloud.io/install/repositories/cs50/repo/script.deb.sh | sudo bash
    $ sudo apt install libcs50


Fedora
-------
.. code-block:: bash 

        $ curl -s https://packagecloud.io/install/repositories/cs50/repo/script.rpm.sh | sudo bash
        $ dnf install libcs50


From Source (Linux and Mac)
---------------------------
  1. Download the latest release from https://github.com/cs50/libcs50/releases
  2. Extract ``libcs50-*.*``
  3. ``cd libcs50-*``
  4. ``sudo make install``



Environment Variables
---------------------

For parity with CS50 CLI, CS50 Sandbox, CS50 Lab, and CS50 IDE, you may want to set these environment variables:

.. code-block:: bash 

    CC="clang"
    CFLAGS="-fsanitize=signed-integer-overflow -fsanitize=undefined -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow"
    LDLIBS="-lcrypt -lcs50 -lm"

Troubleshooting
---------------

If when compiling your program, you see:


    ``/usr/bin/ld: cannot find -lcs50``:
        Add ``export LIBRARY_PATH=/usr/local/lib`` to your ``.bashrc``.
    
    ``fatal error: 'cs50.h' file not found``:
        Add ``export C_INCLUDE_PATH=/usr/local/include`` to your ``.bashrc``.
    
    ``cannot open shared object file: No such file or directory``:
        Add ``export LD_LIBRARY_PATH=/usr/local/lib`` to your ``.bashrc``.


Usage
=====

.. note::
    To use these functions, make sure to include ``#include <cs50.h>`` atop your file and compile with the ``-lcs50`` flag.


.. type:: string

    Type representing a C string. Aliased to :code:`char *`.

    Example usage::

        string s = "hello, world!";


.. function:: char get_char(const char *format, ...)
    
    :param format: the :func:`printf`-like format string used to display the prompt
    :param ...: values to be substituted into the format string a la :func:`printf`
    :returns: the :code:`char` equivalent to the line read from stdin, or :macro:`CHAR_MAX` on error

    Prompts user for a line of text from standard input and returns the equivalent :code:`char`;
    if text does not represent a single char, user is reprompted.

    Example usage::
        
        #include <stdio.h>
        #include <cs50.h>

        int main(void)
        {
            // attempt to read character from stdin
            char c = get_char("Enter char: ");

            // ensure character was read successfully
            if (c == CHAR_MAX)
            {
                return 1;
            }

            char next = get_char("You just entered %c. Enter another char: ", c);

            if (next == CHAR_MAX)
            {
                return 1;
            }

            printf("The last char you entered was %c\n", next);
        }



.. function:: double get_double(const char *format, ...)
    
    :param format: the :func:`printf`-like format string used to display the prompt
    :param ...: values to be substituted into the format string a la :func:`printf`

    :returns: the :code:`double` equivalent to the line read from stdin in [:macro:`DBL_MIN`, :macro:`DBL_MAX`), as precisely as possible, or :macro:`DBL_MAX` on error

    Prompts user for a line of text from standard input and returns the equivalent :code:`double`;
    if text does not represent a double or would cause overflow or underflow, user is reprompted.

    Example usage::

        double divide_doubles(void)
        {
            // read double from stdin
            double d = get_double("Enter a double: ");

            // make sure we read one successfully
            if (d == DBL_MAX)
            {
                return DBL_MAX;
            }

            double e = get_double("What do you want to divide %lf by? ", d);

            // make sure we don't divide by zero
            if (e == DBL_MAX || e == 0.0)
            {
                return DBL_MAX;
            }

            return i / j;
        }




.. function:: int get_int(const char *format, ...)
    
    :param format: the :func:`printf`-like format string used to display the prompt
    :param ...: values to be substituted into the format string a la :func:`printf`

    :returns: the :code:`int` equivalent to the line read from stdin in [:macro:`INT_MIN`, :macro:`INT_MAX`) or :macro:`INT_MAX` on error

    Prompts user for a line of text from standard input and returns the equivalent :code:`int`;
    if text does not represent an int or would cause overflow, user is reprompted.

    Example usage::


        #include <cs50.h>
        
        ... 

        // Returns the sum of two ints read from stdin, or INT_MAX if there was an error.
        int add_ints(void)
        {
            // read int from stdin
            int i = get_int("Enter an int: ");

            // make sure we read one successfully
            if (i == INT_MAX)
            {
                return INT_MAX;
            }

            int j = get_int("What do you want to add %d to? ", i);

            if (j == INT_MAX)
            {
                return INT_MAX;
            }

            return i + j;
        }


.. function:: float get_float(const char *format, ...)
    
    :param format: the :func:`printf`-like format string used to display the prompt
    :param ...: values to be substituted into the format string a la :func:`printf`

    :returns: the :code:`float` equivalent to the line read from stdin in [:macro:`FLT_MIN`, :macro:`FLT_MAX`), as precisely as possible, or :macro:`FLT_MAX` on error

    Prompts user for a line of text from standard input and returns the equivalent float;
    if text does not represent a float or would cause overflow or underflow, user is reprompted.

    Example usage::

        // Returns the product of two floats, or FLT_MAX on error.
        float multiply_floats(void)
        {
            // read float from stdin
            float f = get_float("Enter a float: ");

            // make sure we read one successfully
            if (f == FLT_MAX)
            {
                return FLT_MAX;
            }

            float g = get_float("What do you want to multiply %f by? ", f);

            if (g == FLT_MAX)
            {
                return FLT_MAX;
            }

            return f * g;
        }



.. function:: long get_long(const char *format, ...)
    
    :param format: the :func:`printf`-like format string used to display the prompt
    :param ...: values to be substituted into the format string a la :func:`printf`

    :returns: the :code:`long` equivalent to the line read from stdin in [:macro:`LONG_MIN`, :macro:`LONG_MAX`) or :macro:`LONG_MAX` on error

    Prompts user for a line of text from standard input and returns the equivalent :code:`long`; if text does not represent an int or would cause overflow, user is reprompted.

    Example usage::


        #include <cs50.h>
        
        ... 

        // Returns the difference of two longs read from stdin, or LONG_MAX if there was an error.
        long subtract_longs(void)
        {
            // read long from stdin
            long i = get_long("Enter a long: ");

            // make sure we read one successfully
            if (i == LONG_MAX)
            {
                return LONG_MAX;
            }

            long j = get_long("What do you want to subtract from %ld? ", i);

            if (j == LONG_MAX)
            {
                return LONG_MAX;
            }

            return i - j;
        }


.. function:: char *get_string(const char *format, ...)

    :param format: the :func:`printf`-like format string used to display the prompt
    :param ...: values to be substituted into the format string a la :func:`printf`

    :returns: the read line as a string sans line endings, or :macro:`NULL` on :macro:`EOF`.

   Prompts user for a line of text from standard input and returns it as a string (:code:`char *`),
   sans trailing line ending. Supports CR (``\r``), LF (``\n``), and CRLF (``\r\n``) as line
   endings. Stores string on heap, but library’s destructor frees memory on program’s
   exit.

   Example usage::

       int main(void)
       {
           string s = get_string("Enter string: ");

           // ensure string was read
           if (s == NULL)
           {
               return 1;
           }

           string next = get_string("You just entered %s. Enter a new string: ", s);

           if (next == NULL)
           {
               return 1;
           }

           printf("Your last string was %s\n", next);
       }

 
