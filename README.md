Kartenmacher
============

A python script for creating an interactive HTML map from a list of addresses in a CSV file.

Requirements
------------

 - Python 3.0
 - [geocoder library](https://pypi.python.org/pypi/geocoder)

Installation
------------

    $ git clone https://github.com/asmaier/kartenmacher.git
    $ pip3 install geocoder

Usage
-----

    $ python3 kartenmacher.py -h
    usage: kartenmacher.py [-h] [--heading [HEADING]] csvfile names addresses [link] outfile

    positional arguments:
      csvfile     name of CSV file
      names       column numbers with name information (comma separated)
      addresses   column numbers with address information (comma separated)
      link        column number with a web link
      outfile     name of output HTML file

    optional arguments:
      -h, --help  show this help message and exit
      --heading [HEADING]  column number with an heading


Examples
--------

### Map of Google mail contacts

If you have a Google Mail account you can export your contacts with addresses to e.g. Outlook CSV format.
In Outlook CSV the first name is stored in column 0 and the last name in column 2; the full address is stored
in column 23. Now assuming you have a file called `contacts.csv` in Outlook CSV format you can create a map from it like

	$ python3 kartenmacher.py contacts.csv 0,2 23 map.html

This will create a HTML file `map.html` showing an interactive map (based on Openstreetmap) with the addresses of all
your contacts marked on the map. You can click on each marker to see the name and the address. Pretty cool, isn't it?

### Map of Google spreadsheet

If you have a Google spreadsheet with name information stored in column 0, address information stored in column 1 and a corresponding 
web link stored in column 2 you can easily create a map from it. First download the Google spreadsheet as CSV file. You can do this 
manually or you can download the file directly (when you have set share to "Anyone with the link can view") in a bash terminal
(see also https://stackoverflow.com/questions/10730712/download-unpublished-google-spreadsheet-as-csv)

    $ curl https://docs.google.com/spreadsheets/d/LONG_ID_STRING/export?format=csv -o spreadsheet.csv
    $ python3 kartenmacher.py spreadsheet.csv 0 1 2 map.html

This will again create a HTML file `map.html` showing an interactive map with the addresses of your spreadsheet marked on the map.
If you click on a marker you will see in addition a web link (from column 2 of your spreadsheet), which you can click on and will
open the corresponding web page to the marker in a new tab.


