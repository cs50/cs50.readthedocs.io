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

* [`https://api.cs50.io/dining/locations`](https://api.cs50.io/dining/locations), which returns a JSON array of objects, each of which represents a location on campus.
* `https://api.cs50.io/dining/locations/:id`, where `:id` is the `id` of a location, which returns a JSON object that represents that location.

* [`https://api.cs50.io/dining/categories`](https://api.cs50.io/dining/categories), which returns a JSON array of objects, each of which represents a category of food.
* `https://api.cs50.io/dining/categories/:id`, where `:id` is the `id` of a category, which returns a JSON object that represents that category.

### Locations

For all locations, GET [`https://api.cs50.io/dining/locations`](https://api.cs50.io/dining/locations). A JSON array like the below will be returned:

```json
[
  ...,
  {
    "id": 7,
    "name": "Dunster and Mather House"
  },
  ...
  {
    "id": 9, 
    "name": "Adams House"
  },
  ...
  {
    "id": 30, 
    "name": "Annenberg Hall"
  }, 
  ...
]
```

For a specific location, GET `https://api.cs50.io/dining/locations/:id`, where `:id` is that location's `id`. A JSON object like the below will be returned:

```json
{
  "id": 7,
  "name": "Dunster and Mather House"
}
```

Because some dining halls (e.g., Dunster's and Mather's) share kitchens (and thus menus), they also share an `id` and `name` in the API.
