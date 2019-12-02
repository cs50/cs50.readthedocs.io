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

### Locations

```
GET https://api.cs50.io/dining/locations
```

Returns a JSON array of objects, each of which represents a location on campus. For example, <https://api.cs50.io/dining/locations>.

```
GET https://api.cs50.io/dining/locations/:id
```

Returns a JSON object that represents a location on campus. For example, <https://api.cs50.io/dining/locations/30> represents Annenberg Hall, while <https://api.cs50.io/dining/locations/7> represents Dunster and Mather House. Because some dining halls (e.g., Dunster's and Mather's) share kitchens (and thus menus), they also share an `id` (and `name`) in the API.

### Categories

```
GET https://api.cs50.io/dining/categories
```

Returns a JSON array of objects, each of which represents a category of food. For example, <https://api.cs50.io/dining/categories>.

```
GET https://api.cs50.io/dining/categories/:id
```

Returns a JSON object that represents a category, where `:id` is that category's `id`. For example, <https://api.cs50.io/dining/categories/32> represents Fresh Fruit, whereas <https://api.cs50.io/dining/categories/62> represents Daily Soups. Yum!

### Recipes

```
GET https://api.cs50.io/dining/recipes
```

Returns a JSON array of objects, each of which represents a recipe. For example, <https://api.cs50.io/dining/recipes>.

```
GET https://api.cs50.io/dining/recipes/:id
```

Returns a JSON object that represents a recipe. For example, <https://api.cs50.io/dining/recipes/22011> represents Kabocha Squash Soup, whereas <https://api.cs50.io/dining/recipes/22045> represents Wheat Tortillas. Yum!

### Menus

```
GET https://api.cs50.io/dining/menus
```

Returns a JSON array of objects, each of which represents a menu item (i.e., a recipe being served in some category for some meal at some location(s)). For example, <https://api.cs50.io/dining/menus> represents today's menus. Within each of those objects, the value of `category` is the `id` of a [category](#categories), the value of `location` is the `id` of a [location](#locations), the value of `meal` is the `id` of a [meal](#meals), and the value of `recipe` is the `id` of a [recipe](#recipes).

Supports these parameters, each of which can be multivalued:

* `date`, the value of which should be a date in YYYY-MM-DD format. Defaults to today's date (in Eastern Time). For example, <https://api.cs50.io/dining/menus> represents today's menus, whereas <https://api.cs50.io/dining/menus?date=2019-12-02> represents menus for 2 December 2019, and <https://api.cs50.io/dining/menus?date=2019-12-02&2019-12-03> represents menus for 2 December 2019 and 3 December 2019.
* `meal`, the value of which should be the `id` of a meal. For example, <https://api.cs50.io/dining/menus?meal=1> represents today's lunch menus, whereas <https://api.cs50.io/dining/menus?meal=1&meal=2> represents today's lunch and dinner menus.
* `location`, the value of which should be the `id` of a location. For example, <https://api.cs50.io/dining/menus?location=7> represents today's menu at Dunster and Mather House, whereas <https://api.cs50.io/dining/menus?location=5&location=38> represents today's menus at Cabot and Pforzheimer House as well as Currier House.
* `category`, the value of which should be the `id` of a category. For example, <https://api.cs50.io/dining/menus?category=32> represents today's menus, if any, with Fresh Fruit, whereas <https://api.cs50.io/dining/menus?category=32&category=15> represents today's menus, if any, with Fresh Fruit or Vegetables.
* `recipe`, the value of which should be the `id` of a recipe. For example, <https://api.cs50.io/dining/menus?recipe=22011> represents today's menus, if any, with Kabocha Squash Soup, whereas <https://api.cs50.io/dining/menus?recipe=22011&recipe=22045> represents today's menus with Kabocha Squash Soup or Wheat Tortillas.

Any of these parameters can be used together. For example, <https://api.cs50.io/dining/menus?location=5&location=38&meal=0> represents today's breakfast menus at Cabot and Pforzheimer House as well as Currier House.

## Notes

* [Bagged meals](https://dining.harvard.edu/campus-dining/undergraduate-dining/weeks-menu) for undergraduates are only available at some [locations](#locations) (i.e., undergraduate dining halls), and their [recipes](#recipes) are in multiple categories. Accordingly, you can GET them via a (long!) URL like
  <https://api.cs50.io/dining/menus?category=87&category=91&category=92&category=93&category=94&category=95&category=96&category=97&location=5&location=7&location=8&location=9&location=14&location=15&location=16&location=30&location=38>.
* Fly-By is implemented as a [location](#locations). Accordingly, you can GET today's Fly-By's menu via a URL like <https://api.cs50.io/dining/menus?location=29>.
