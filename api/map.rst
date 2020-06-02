Map API
=======

CS50's Map API provides programmatic access via HTTP to data from `map.harvard.edu <https://map.harvard.edu/>`_.

Buildings
---------

Getting Buildings
^^^^^^^^^^^^^^^^^

.. http:get:: /map/buildings

    :synopsis: Returns a JSON array of objects, each of which represents a building. For example, https://api.cs50.io/map/buildings.

    :query address: If provided, any building whose address contains **address** will be returned.
    :query name: If provided, building whose name contains **name** will be returned.

    :statuscode 200: Always returned, even if no buildings match ``address`` or ``name``.

    :>jsonarr string address: A building's (street) address.
    :>jsonarr string city: A building's city (in Massachusetts).
    :>jsonarr object geometry: An object with two keys: **point**, the value of which is an array with two values, each of which is a ``float``, representing a building's latitude and longitude, respectively; and **polygons**, which is an array of arrays, each of which represents a polygon that outlines (part of) a building's footprint, each of whose values is an array with two values, each of which is a ``float``, representing the latitude and longitude of a vertex of the polygon.
    :>jsonarr integer id: A building's unique identifer. Usable as a primary key in a databse.
    :>jsonarr string image: URL of a building's image, if any.
    :>jsonarr string name: A building's name, if any.

    **Example #1: Getting All Buildings**

    https://api.cs50.io/map/buildings

    .. tabs::

        .. code-tab:: python

            import requests

            # Get buildings
            response = requests.get("https://api.cs50.io/map/buildings")

            # Convert JSON to list of dicts
            buildings = response.json()

            # Print each building's name
            for building in buildings:
                print(building["name"])

        .. code-tab:: bash cURL

            curl "https://api.cs50.io/map/buildings"

    **Example #2: Getting All Wigglesworth Buildings**

    https://api.cs50.io/map/buildings?name=wigglesworth

    .. tabs::

        .. code-tab:: python

            import requests

            # Get buildings
            response = requests.get("https://api.cs50.io/map/buildings?name=wigglesworth")

            # Convert JSON to list of dicts
            buildings = response.json()

            # Print each building's name
            for building in buildings:
                print(building["name"])

        .. code-tab:: bash cURL

            curl "https://api.cs50.io/map/buildings?name=wigglesworth"

    **Example #3: Getting All Buildings on Oxford Street**

    https://api.cs50.io/map/buildings?address=oxford%20street

    .. tabs::

        .. code-tab:: python

            import requests

            # Get buildings
            response = requests.get("https://api.cs50.io/map/buildings?name=oxford%20street")

            # Convert JSON to list of dicts
            buildings = response.json()

            # Print each building's name
            for building in buildings:
                print(building["name"])

        .. code-tab:: bash cURL

            curl "https://api.cs50.io/map/buildings?name=oxford%20street"

Getting a Building
^^^^^^^^^^^^^^^^^^

.. http:get:: /map/buildings/(id)

    :synopsis: Returns a JSON object that represents a building, where **id** is that building's unique identifier. For example, https://api.cs50.io/map/buildings/1358 represents Mather House, while https://api.cs50.io/map/buildings/1145 represents Matthews Hall.

    :param id: A building's unique identifier.

    :statuscode 200: Returned if a building with **id** exists.
    :statuscode 404: Returned if no building with **id** exists.

    :>json string address: A building's (street) address.
    :>json string city: A building's city (in Massachusetts).
    :>json object geometry: An object with two keys: **point**, the value of which is an array with two values, each of which is a ``float``, representing a building's latitude and longitude, respectively; and **polygons**, which is an array of arrays, each of which represents a polygon that outlines (part of) a building's footprint, each of whose values is an array with two values, each of which is a ``float``, representing the latitude and longitude of a vertex of the polygon.
    :>json integer id: A building's unique identifer. Usable as a primary key in a databse.
    :>json string image: URL of a building's image, if any.
    :>json string name: A building's name, if any.

    **Example #1: Getting Mather House**

    https://api.cs50.io/map/buildings/1358

    .. tabs::

        .. code-tab:: python

            import requests

            # Get building
            response = requests.get("https://api.cs50.io/map/buildings/1358")

            # Convert JSON to dict
            building = response.json()

            # Print building's name
            print(building["name"])

        .. code-tab:: bash cURL

            curl "https://api.cs50.io/map/buildings/1358"

Acknowledgements
----------------

Special thanks to CS50's friends at Harvard's `Center for Geographic Analysis <https://gis.harvard.edu/>`_ for this API's data!
