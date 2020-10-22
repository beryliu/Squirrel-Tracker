## Squirrel-Tracker

This is the final project for IEORE4501 Tools for Analytics, Columbia University.


### Project Description

This is a web application developed with Django framework designed to keep track of all the known squirrels. The application can import the [2018 Central Park Squirrel Census](https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv) data using the management command:

```
$ python manage.py import_squirrel_data /path/to/file.cs
```

,and export the data using the management command:

```
$ python manage.py export_squirrel_data /path/to/file.cs
```

The users are allowed to add, update, and view squirrel data. The web application also includes a map view that displays the location of all the squirrel sightings and a view that provides some general statistics about the sightings.
 

### Contributors

Nianbin Liu & Zhanbo Peng

Group Name: Project Group 37

UNIs: [nl2736, zp2226]

