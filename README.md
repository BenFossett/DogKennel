# DogKennel
A demonstration of different referencing methods using PyMongo.

There are four files, each making use of a different method of referencing:
* basic_db.py - No referencing
* childref_db.py - Parent-to-Child referencing
* childrefs_db.py - Parent-to-Children referencing
* parentref_db.py - Child-to-Parent referencing

To view a demonstration of the database functionality, run the file "mongod.exe", included in your MongoDB installation,
and then execute one of these files as you would a normal Python script. In your terminal, you will see various statements
printed detailing what is currently happening in the database.
