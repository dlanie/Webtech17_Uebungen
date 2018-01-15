# coding: utf-8
# Uni Osnabrück, Web-Technologien 2017/2018
# Übungsblatt 01, Aufgabe 1-3
#

# https://docs.python.org/3/library/json.html
import json


def read_json(fn):
    """Read a members-json file from the file identified by fn. Content is parsed but not validated."""
    file = open(fn, "r")
    return(json.load(file))

def print_html(fn, name, members):
    """Print HTML table to file 'fn'. Uses 'name' for heading and walks through 'members' structure."""
    headline = "<h1>" + name + "</h1>"
    table = "<table><tr>"
    memberkeys = members[0].keys()
    for c in memberkeys:
        table = table+"<td>"+c+"</td>"
    table=table+"</tr>"
    for i in range(len(members)):
        #memberkeys = members[i].keys()
        table=table+"<tr>"
        for b in memberkeys:
            table=table+"<td>"+members[i][b]+"</td>"
        table=table+"</tr>"
    table=table+"</table>"
    file = open(fn, "w")
    file.write(headline + "<br>" + table)
    file.close()

if __name__ == '__main__':  # Python jargon for main - only executed if script is used as top level script
    infile = "members.json"
    outfile = "members.html"
    data = read_json(infile)
    print_html(outfile, data["name"], data["members"])
    print("HTML table written to '{}'".format(outfile))
