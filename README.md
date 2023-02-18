# Universe

A Django API to retrieve the content of the universe, including planets, stars, galaxies, and all other forms of matter and energy

## Developement

Apply migrations:

```
python universe/manage.py migrate
```

Load the data (planets, stars, galaxies...):

```
python universe/manage.py loaddata db.json
```

Run server:

```
python universe/manage.py runserver
```

## Dump data

Dump data:

```
python universe/manage.py dumpdata [apps name] --indent 2 > db.json
```

```
python universe/manage.py dumpdata common astronomical_object --indent 2 > db.json
```
