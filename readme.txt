London MP Finder
_________________________



About:

A Flask-based web application which allows the user to enter their postcode and returns information about their constituency and MP by querying a PostgreSQL database.


Created by Conor Sneyd (https://github.com/conorsneyd)



Requirements:

Python 3.12, Flask, psycopg2, a PostgreSQL client (recommended: Postbird)



How to run:

- Create a new database within your PostgreSQL client called postcodes_mps.

- Use postcodes_mps.sql to populate your database, e.g. by running the command: psql -U [your username] -d postcodes_mps -f [the location of the file].

- Edit postcode_lookup.py and enter your database details into the postcode_lookup() function.

- Open app.py in Python, then open http://localhost:5000/ in browser and follow the instructions on screen.


Data:

Information on postcodes and constituencies provided by https://www.doogal.co.uk/ElectoralConstituencies and used to build a custom database.

Contains OS data © Crown copyright and database right 2024
Contains Royal Mail data © Royal Mail copyright and database right 2024
Contains National Statistics data © Crown copyright and database rights 2024
Source: Office for National Statistics licensed under the Open Government Licence v.3.0
Contains data from Wikipedia covered by the Creative Commons license 