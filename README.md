# GET RSS

This python script is used to consume rss feeds.
It can be useful for dataset generation for example

## Usage: 

```
get_rss.py [-h] [-i ITEMS [ITEMS ...]] [-f FILE] [-l LIMIT] [--id] [--no-id] url [url ...]


A simple rss feed consumer. writes a json output to stdout or specific file

positional arguments:
  url                   The rss feed url to get

options:
  -h, --help            show this help message and exit
  -i ITEMS [ITEMS ...], --items ITEMS [ITEMS ...]
                        Optional items (keys) to extract from the rss feed. By default only the title is extracted and mapped as text; if items are passed, the default behaviour is overridden
  -f FILE, --file FILE  An optional file argument; if provided the result will be written to the file else output is written to stdout
  -l LIMIT, --limit LIMIT
                        Limit the number of items (per url) in the output
  --id                  This option allows to specify whether a custom id should be added to the items. If id is specified in the items, this option will not override it
  --no-id
```
