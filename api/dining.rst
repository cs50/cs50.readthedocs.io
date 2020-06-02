Dining API
==========

CS50's Dining API provides programmatic access via HTTP to data from `Harvard University Dining Services <https://dining.harvard.edu/>`_ (HUDS), including menus for undergraduate dining halls, graduate dining halls, and some cafes on campus. The API provides endpoints for:

* `Categories`_
* `Locations`_
* `Menus`_
* `Recipes`_

Categories
----------

Getting Categories
^^^^^^^^^^^^^^^^^^

.. http:get:: /dining/categories

    :synopsis: Returns a JSON array of objects, each of which represents a category of food. For example, https://api.cs50.io/dining/categories.

    :statuscode 200: Always returned.

    :>jsonarr integer id: A category's unique identifer. Usable as a primary key in a databse.
    :>jsonarr string name: A category's name.

    **Example: Getting All Categories**

    https://api.cs50.io/dining/categories

    .. tabs::

        .. code-tab:: python

            import requests

            # Get categories
            response = requests.get("https://api.cs50.io/dining/categories")

            # Convert JSON to list of dicts
            categories = response.json()

            # Print each category's name
            for category in categories:
                print(category["name"])

        .. code-tab:: bash cURL

            curl "https://api.cs50.io/dining/categories"

Getting a Category
^^^^^^^^^^^^^^^^^^

.. http:get:: /dining/categories/(id)

    :synopsis: Returns a JSON object that represents a category, where **id** is that category's unique identifier. For example, https://api.cs50.io/dining/categories/32 represents Fresh Fruit, whereas https://api.cs50.io/dining/categories/62 represents Daily Soups. Yum!

    :param id: A location's unique identifier.

    :statuscode 200: Returned if a category with **id** exists.
    :statuscode 404: Returned if no category with **id** exists.

    :>json integer id: A category's unique identifer. Usable as a primary key in a databse.
    :>json string name: A category's name.

    **Example: Getting Fresh Fruit**

    https://api.cs50.io/dining/categories/32

    .. tabs::

        .. code-tab:: python

            import requests

            # Get category
            response = requests.get("https://api.cs50.io/dining/categories/32")

            # Convert JSON to dict
            category = response.json()

            # Print category's name
            print(category["name"])

        .. code-tab:: bash cURL

            curl "https://api.cs50.io/dining/categories/32"

Locations
---------

Getting Locations
^^^^^^^^^^^^^^^^^

.. http:get:: /dining/locations

    :synopsis: Returns a JSON array of objects, each of which represents a location. For example, https://api.cs50.io/dining/locations.

    :statuscode 200: Always returned.

    :>jsonarr integer id: A location's unique identifer. Usable as a primary key in a databse.
    :>jsonarr string name: A location's name.

    **Example: Getting All Locations**

    https://api.cs50.io/dining/locations

    .. tabs::

        .. code-tab:: python

            import requests

            # Get locations
            response = requests.get("https://api.cs50.io/dining/locations")

            # Convert JSON to list of dicts
            locations = response.json()

            # Print each location's name
            for location in locations:
                print(location["name"])

        .. code-tab:: bash cURL

            curl "https://api.cs50.io/dining/locations"

Getting a Location
^^^^^^^^^^^^^^^^^^

.. http:get:: /dining/locations/(id)

    :synopsis: Returns a JSON object that represents a location, where **id** is that location's unique identifier. For example, https://api.cs50.io/dining/locations/30 represents Annenberg Hall, while https://api.cs50.io/dining/locations/7 represents Dunster and Mather House. Because some dining halls (e.g., Dunster's and Mather's) share kitchens (and thus menus), they also share an **id** (and **name**) in the API.

    :param id: A location's unique identifier.

    :statuscode 200: Returned if a location with **id** exists.
    :statuscode 404: Returned if no location with **id** exists.

    :>json integer id: A location's unique identifer. Usable as a primary key in a databse.
    :>json string name: A location's name.

    **Example: Getting Annenberg Hall**

    https://api.cs50.io/dining/locations/7

    .. tabs::

        .. code-tab:: python

            import requests

            # Get location
            response = requests.get("https://api.cs50.io/dining/locations/30")

            # Convert JSON to dict
            location = response.json()

            # Print location's name
            print(location["name"])

        .. code-tab:: bash cURL

            curl "https://api.cs50.io/dining/locations/7"

Menus
-----

.. note::
   Each query parameter can have multiple values, as by including it in a URL multiple times.

Getting Menus 
^^^^^^^^^^^^^

.. http:get:: /dining/menus

    :synopsis: Returns a JSON array of objects, each of which represents a menu item (i.e., a recipe being served in some category for some meal at one or more locations). For example, https://api.cs50.io/dining/menus represents today's menus. Within each of those objects, the value of **category** is the **id** of a category, the value of **location** is the **id** of a location, the value of **meal** is the **id** of a meal, and the value of **recipe** is the **id** of a recipe. Any of the query parameters can be used together. For example, https://api.cs50.io/dining/menus?location=5&location=38&meal=0 represents today's breakfast menus at Cabot and Pforzheimer House as well as Currier House.

    :query date: The date for a menu, formatted as ``YYYY-MM-DD``. Defaults to today’s date (in Eastern Time). For example, https://api.cs50.io/dining/menus represents today’s menus, whereas https://api.cs50.io/dining/menus?date=2019-12-02 represents menus for 2 December 2019, and https://api.cs50.io/dining/menus?date=2019-12-02&date=2019-12-03 represents menus for 2 December 2019 and 3 December 2019.
    :query meal: The unique identifier of a meal. For example, https://api.cs50.io/dining/menus?meal=1 represents today’s lunch menus, whereas https://api.cs50.io/dining/menus?meal=1&meal=2 represents today’s lunch and dinner menus.
    :query location: The unique identifier of a location. For example, https://api.cs50.io/dining/menus?location=7 represents today’s menu at Dunster and Mather House, whereas https://api.cs50.io/dining/menus?location=5&location=38 represents today’s menus at Cabot and Pforzheimer House as well as Currier House.
    :query category: The unique identifier of a category. For example, https://api.cs50.io/dining/menus?category=32 represents today’s menus, if any, with Fresh Fruit, whereas https://api.cs50.io/dining/menus?category=32&category=15 represents today’s menus, if any, with Fresh Fruit or Vegetables.
    :query recipe: The unique identifier of a recipe. For example, https://api.cs50.io/dining/menus?recipe=22011 represents today’s menus, if any, with Kabocha Squash Soup, whereas https://api.cs50.io/dining/menus?recipe=22011&recipe=22045 represents today’s menus with Kabocha Squash Soup or Wheat Tortillas.

    :statuscode 200: Returned if endpoint is used properly, even if no menus match the query parameters.
    :statuscode 400: Returned if endpoint isn't used properly.

    :>jsonarr integer id: A recipe's unique identifer. Usable as a primary key in a databse.
    :>jsonarr string name: A recipe's name.

    **Example: Getting Annenberg Hall's Lunch Menu for 2 December 2019**

    https://api.cs50.io/dining/menus?date=2019-12-02&location=7&meal=1

    .. tabs::

        .. code-tab:: python

            import requests

            # Get Annenberg Hall's lunch menu for 2019-12-02
            response = requests.get("https://api.cs50.io/dining/menus", {"date": "2019-12-02", "location": 7, "meal": 1})

            # Convert JSON to list of dicts
            menu = response.json()

            # Print number of recipes on menu
            print(len(menu))

        .. code-tab:: bash cURL

            curl "https://api.cs50.io/dining/menus?date=2019-12-02&location=7&meal=1"

Recipes
-------

Getting Recipes
^^^^^^^^^^^^^^^^^^

.. http:get:: /dining/recipes

    :synopsis: Returns a JSON array of objects, each of which represents a recipe. For example, https://api.cs50.io/dining/recipes.

    :statuscode 200: Always returned.

    :>jsonarr integer id: A recipe's unique identifer. Usable as a primary key in a databse.
    :>jsonarr string name: A recipe's name.

    **Example: Getting All Recipes**

    https://api.cs50.io/dining/recipes

    .. tabs::

        .. code-tab:: python

            import requests

            # Get categories
            response = requests.get("https://api.cs50.io/dining/recipes")

            # Convert JSON to list of dicts
            recipes = response.json()

            # Print each recipe's name
            for recipe in recipes:
                print(recipe["name"])

        .. code-tab:: bash cURL

            curl "https://api.cs50.io/dining/recipes"

Getting a Recipe
^^^^^^^^^^^^^^^^

.. http:get:: /dining/recipes/(id)

    :synopsis: Returns a JSON object that represents a recipe, where **id** is that recipe's unique identifier. For example, https://api.cs50.io/dining/recipes/22011 represents Kabocha Squash Soup, whereas https://api.cs50.io/dining/recipes/22045 represents Wheat Tortillas. Yum!

    :param id: A recipe's unique identifier.

    :statuscode 200: Returned if a recipe with **id** exists.
    :statuscode 404: Returned if no recipe with **id** exists.

    :>json integer id: A recipe's unique identifer. Usable as a primary key in a databse.
    :>json string name: A recipe's name.

    **Example: Getting Kabocha Squash Soup**

    https://api.cs50.io/dining/recipes/22011

    .. tabs::

        .. code-tab:: python

            import requests

            # Get recipe
            response = requests.get("https://api.cs50.io/dining/recipes/22011")

            # Convert JSON to dict
            recipe = response.json()

            # Print recipe's name
            print(recipe["name"])

        .. code-tab:: bash cURL

            curl "https://api.cs50.io/dining/recipes/22011"

Acknowledgements
----------------

Special thanks to CS50's friends at `HUDS <https://dining.harvard.edu/>`_ and `HUIT <https://huit.harvard.edu/>`_ for this API's data!
