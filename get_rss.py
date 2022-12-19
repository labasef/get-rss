#!/usr/bin/env python3

import argparse
import feedparser
import yaml
import json
import csv
import uuid
import sys
from io import StringIO


parser = argparse.ArgumentParser(description="A simple rss feed consumer. writes a json output to stdout or specific file")
parser.add_argument('url', type=str, nargs='+', help='The rss feed url to get')
parser.add_argument('-i', '--items', type=str, nargs='+', help='Optional items (keys) to extract from the rss feed. By default only the title is extracted and mapped as text; if items are passed, the default behaviour is overridden')
parser.add_argument('-f', '--file', type=str, help='An optional file argument; if provided the result will be written '
                                                   'to the file else output is written to stdout')
#parser.add_argument('--format', type=str, nargs='?', default='json', help='An optional argument to specify the output format; supported formats are json and csv, default format is json')
parser.add_argument('-l', '--limit', type=int, default=-1, help='Limit the number of items (per url) in the output')
parser.add_argument('--id', dest='_id', action='store_true', help='This option allows to specify whether a custom id should be added to the items. If id is specified in the items, this option will not override it')
parser.add_argument('--no-id', dest='_id', action='store_false')
parser.set_defaults(_id=True)


def write(arg: dict):
    if args.file:
        with open(args.file, 'a') as f:
            json.dump(arg, f)
        print(args.file)
    else:
        out = json.dumps(arg)
        print(out)


def consume_feed(url):
    res = []
    feed = feedparser.parse(url)
    if args.items:
        struct = {item: item for item in args.items}
    else:
        # default structure dictionnary; key: key to be found in rss feed, value: mapped key for json output
        struct = {"title": "text"}
    if feed:
        for item in feed["items"][:args.limit]:
            try:
                tmp = {value: item[key] for key, value in struct.items()}
                if args._id: 
                    # if id argument is set to true add a custom id to result
                    res.append({"id": str(uuid.uuid4())} | tmp)
                else:
                    res.append(tmp)
            except KeyError as e:
                # printing errors to standard error
                print(str(e), file=sys.stderr)
    return res


if __name__ == "__main__":
    result = []
    args = parser.parse_args()
    if args.url:
        for url in args.url:
            result += consume_feed(url)
        write(result)
