# Dining API

CS50's Dining API provides programmatic access (via HTTP) to data from [Harvard University Dining Services](https://dining.harvard.edu/) (HUDS), including menus for

* [undergraduate dining halls](https://dining.harvard.edu/campus-dining/undergraduate-dining/weeks-menu)
* [graduate dining halls](https://dining.harvard.edu/campus-dining/graduate-dining-halls/menus), and
* some [cafes](https://dining.harvard.edu/campus-dining/cafes/hungry) on campus.

## Endpoints

Each of the API

On errors, each endpoint returns a status code of 

Each of the API's endpoints returns output in [JSON](https://en.wikipedia.org/wiki/JSON) format.

### Locations

For all locations, GET `https://api.cs50.io/dining/locations`. A JSON array like the below will be returned:

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
