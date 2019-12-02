# Dining API

CS50's Dining API provides programmatic access via HTTP to data from [Harvard University Dining Services](https://dining.harvard.edu/) (HUDS), including menus for

* [undergraduate dining halls](https://dining.harvard.edu/campus-dining/undergraduate-dining/weeks-menu)
* [graduate dining halls](https://dining.harvard.edu/campus-dining/graduate-dining-halls/menus), and
* some [cafes](https://dining.harvard.edu/campus-dining/cafes/hungry) on campus.

The API expects requests via GET (or HEAD).

On success, the API returns data in [JSON](https://en.wikipedia.org/wiki/JSON) format with an HTTP status code of 200.

On failure, the API returns an HTTP status code of

* 400, if an endpoint wasn't used properly, or
* 404, if an endpoint doesn't exist.

## Endpoints

### Categories

```
GET https://api.cs50.io/dining/categories
```

Returns a JSON array of objects, each of which represents a category of food. For instance, <https://api.cs50.io/dining/categories>.

```
GET https://api.cs50.io/dining/categories/:id
```

Returns a JSON object that represents a category, where `:id` is that category's `id`. For example, <https://api.cs50.io/dining/categories/90> represents Fresh Fruit. Yum!

### Locations

For a JSON array of objects, each of which represents a location on campus, GET [`https://api.cs50.io/dining/locations`](https://api.cs50.io/dining/locations).

For a JSON object that represents a specific location on campus, GET `https://api.cs50.io/dining/locations/:id`, where `:id` is that location's `id`.

### Recipes

For a JSON array of objects, each of which represents a recipe, GET [`https://api.cs50.io/dining/recipes`](https://api.cs50.io/dining/recipes).

For a JSON object that represents a specific recipe, GET `https://api.cs50.io/dining/recipe/:id`, where `:id` is that recipe's `id`.
<--

* [`https://api.cs50.io/dining/categories`](https://api.cs50.io/dining/categories), which returns a JSON array of objects, each of which represents a category of food.
* `https://api.cs50.io/dining/categories/:id`, where `:id` is the `id` of a category, which returns a JSON object that represents that category.

-->
