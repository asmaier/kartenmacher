#!/usr/bin/env python

import argparse
import csv
import html as cgi
import geocoder
from string import Template

def filter_text(text):
    temp = text.replace("'","").replace("\n", "").replace("\r", "").strip()
    return cgi.escape(temp, quote=True)

javascript = Template("markers.push(L.marker([$lat, $lng]).addTo(map).bindPopup('$popup'));")

html_template = open("template.html", "r").read()
html = Template(html_template)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("csvfile", help="name of CSV file")
    parser.add_argument("names", help="column numbers with name information(comma separated)")
    parser.add_argument("addresses", help="column number with address information (comma separated)")
    parser.add_argument("link", nargs="?", help="column number with a web link")
    parser.add_argument("--heading", nargs="?", help="column number with an heading")
    parser.add_argument("outfile", help="name of output HTML file")
    args = parser.parse_args()

    names = args.names.split(",")
    addresses = args.addresses.split(",")
    link = args.link
    heading = args.heading

    markers =  []

    with open(args.csvfile) as input:
        reader = csv.reader(input)
        next(reader, None)  # skip the headers
        for row in reader:
            full_address = " ".join([filter_text(row[int(address)]) for address in addresses])
            if full_address.strip():
                if heading:
                    full_heading = filter_text(row[int(heading)])
                    print(full_heading)
                full_name = " ".join([filter_text(row[int(name)]) for name in names])
                print(full_name)
                print(full_address)
                if link:
                    full_link = "<a target=\"_blank\" href=\"{0}\">{0}</a>".format(filter_text(row[int(link)]))
                    print(full_link)

                g = geocoder.osm(full_address)
                if not g.latlng:
                    g = geocoder.yandex(full_address)
                # print(g.latlng)
                if g.latlng:
                    latitude, longitude = g.latlng
                    # print(latitude, longitude)
                    popup = ""
                    if heading:
                        popup += "<h3>" + full_heading + "</h3>"
                    popup += full_name + "<br />" + full_address
                    if link:
                        popup += "<br />" + full_link
                    markers.append(javascript.substitute(lat=latitude, lng=longitude, popup=popup ))

    outstring = html.substitute(markers="\n".join(markers))
    with open(args.outfile, "w") as output:
        output.write(outstring)




