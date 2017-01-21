Kartenmacher
==========

A python script for creating an interactive HTML map from a list of addresses in a CSV file.

Requirements
------------

 - Python 2.7
 - [geocoder library](https://pypi.python.org/pypi/geocoder)

Installation
------------

    $ pip install geocoder
    $ git clone https://github.com/asmaier/kartenmacher.git

Usage
-----

    $ python kartenmacher.py -h
    usage: kartenmacher.py [-h] csvfile names addresses link outfile

    positional arguments:
      csvfile     name of CSV file
      names       column numbers with name information (comma separated)
      addresses   column numbers with address information (comma separated)
      link        column number with a web link
      outfile     name of output HTML file

    optional arguments:
      -h, --help  show this help message and exit


Example:

If you have a Google Mail account you can export your contacts with addresses to e.g. Outlook CSV format.
In Outlook CSV the first name is stored in column 0 and the last name in column 2; the full address is stored
in column 23. Now assuming you have a file called `contacts.csv` in Outlook CSV format you can create a map from it like

	$ python kartenmacher.py contacts.csv 0,2 23 map.html

This will create a HTML file `map.html` showing an interactive map (based on Openstreetmap) with the addresses of all
your contacts marked on the map. You can click on each marker to see the name and the address. Pretty cool, isn't it?


