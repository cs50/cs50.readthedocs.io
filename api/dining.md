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

Returns a JSON array of objects, each of which represents a category of food. For example, <https://api.cs50.io/dining/categories>.

```
GET https://api.cs50.io/dining/categories/:id
```

Returns a JSON object that represents a category, where `:id` is that category's `id`. For example, <https://api.cs50.io/dining/categories/32> represents Fresh Fruit, whereas <https://api.cs50.io/dining/categories/62> represents Daily Soups. Yum!

### Locations

```
GET https://api.cs50.io/dining/locations
```

Returns a JSON array of objects, each of which represents a location on campus. For example, <https://api.cs50.io/dining/locations>.

```
GET https://api.cs50.io/dining/locations/:id
```

Returns a JSON object that represents a location on campus. For example, <https://api.cs50.io/dining/locations/30> represents Annenberg Hall, while <https://api.cs50.io/dining/locations/7> represents Dunster and Mather House. Because some dining halls (e.g., Dunster's and Mather's) share kitchens (and thus menus), they also share an `id` (and `name`) in the API.

### Recipes

```
GET https://api.cs50.io/dining/recipes
```

Returns a JSON array of objects, each of which represents a recipe. For example, <https://api.cs50.io/dining/recipes>.

```
GET https://api.cs50.io/dining/recipes/:id
```

Returns a JSON object that represents a recipe. For example, <https://api.cs50.io/dining/recipes/22011> represents Kabocha Squash Soup, whereas <https://api.cs50.io/dining/recipes/22045> represents Wheat Tortillas. Yum!
