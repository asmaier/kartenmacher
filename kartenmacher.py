#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import argparse
import csv
import geocoder
from string import Template

javascript = Template('markers.push(L.marker([$lat, $lng]).addTo(map).bindPopup("$popup"));')

html_template = open("template.html", "r").read()
html = Template(html_template)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("csvfile", help="name of CSV file")
    parser.add_argument("names", help="name columns in CSV file (comma separated)")
    parser.add_argument("addresses", help="address columns in CSV file (comma separated)")
    parser.add_argument("outfile", help="name of output HTML file")
    args = parser.parse_args()

    names = args.names.split(",")
    addresses = args.addresses.split(",")

    markers =  []

    with open(args.csvfile) as input:
        for row in csv.reader(input):
            full_address = " ".join([row[int(address)].replace("\n", " ").replace("\r", " ") for address in addresses])
            if full_address.strip():
                full_name = " ".join([row[int(name)] for name in names])
                print full_name
                print full_address

                g = geocoder.google(full_address)
                print g.latlng
                if g.latlng:
                    latitude, longitude = g.latlng
                    print latitude, longitude
                    markers.append(javascript.substitute(lat=latitude, lng=longitude, popup=full_name + "<br />" + full_address))

    outstring = html.substitute(markers="\n".join(markers))
    with open(args.outfile, "w") as output:
        output.write(outstring)




