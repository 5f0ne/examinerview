import os
import sys
import csv
import json
import argparse

from examinerview.Controller import Controller
from examinerview.classes.Event import Event
from examinerview.classes.Timeline import Timeline

events = []

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--data", "-d", type=str, required=True, help="Path to csv file")
    parser.add_argument("--output", "-o", type=str, default=".", help="Path to output dir")
    parser.add_argument("--format", "-f", type=str, default="%Y-%m-%d %H:%M:%S.%f", help="The timestamp format")
    parser.add_argument("--delimiter", "-e", type=str, default=";", help="The delimiter for csv file")
    parser.add_argument("--quotechar", "-q", type=str, default='"', help="The quotechar for csv file")
    args = parser.parse_args()

    ctrl = Controller()

    ctrl.printHeader()

    ctrl.printMessage("        Read data from: " + args.data)

    with open(args.data, 'r', encoding="utf8") as csv_file:

        tl = Timeline()
        reader = csv.reader(csv_file, delimiter=args.delimiter, quotechar=args.quotechar)

        count = 0
        for row in reader:
            if(count > 0):
                event = Event(row[0], row[1], row[2], row[3], row[4], row[5], row[6], args.format)
                events.append(event)
                tl.addEvent(event)
            count = count + 1


    # Create the config file
    jsonPath = os.path.join(args.output, "timeline.json")
    with open(jsonPath, 'w', encoding="utf8") as f:
        json.dump(vars(tl), f, indent=4)

    ctrl.printMessage("Write timeline data to: " + jsonPath)

    # Create the paths
    p = os.path.dirname(__file__)
    tplPath = os.path.join(p, "template", "index.html")
    outputFile = os.path.join(args.output, "examinerview.html")
   
    # Read the template
    html = open(tplPath).read()
    html = html.replace("[DATA_INSERT]", "var data = " + json.dumps(vars(tl)))

    # Write the result
    with open(outputFile, "w") as fp:
        fp.write(html)

    ctrl.printMessage("       Write result to: " + outputFile)
    ctrl.printExecutionTime()

if __name__ == "__main__":
    sys.exit(main())