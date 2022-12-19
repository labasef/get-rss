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

## Examples

Get items from nature rss feed
```
python3 get_rss.py "http://www.nature.com/nature/current_issue/rss"
```

Get the last 2 items (title and link) from lemonde rss feed
```
python3 get_rss.py "https://www.lemonde.fr/rss/une.xml" -i "title" "link" --limit 2
```

Get the last 5 items (title and link) from elife rss feed without generated id
```
python3 get_rss.py http://elife.elifesciences.org/rss/recent.xml -i "title" "link" --limit 5 --no-id
```

## RSS feeds examples

### News

*    Lemonde -  https://www.lemonde.fr/rss/une.xml
*    LeParisien - https://feeds.leparisien.fr/leparisien/rss
*    France24 - https://www.france24.com/fr/rss
*    Francetvinfo - https://www.francetvinfo.fr/titres.rss

### Science
 
*    Nature - http://www.nature.com/nature/current_issue/rss
*    Science - http://www.sciencemag.org/rss/current.xml
*    Cell - http://rss.sciencedirect.com/publication/science/00928674
*    eLife - http://elife.elifesciences.org/rss/recent.xml
*    PLoS Biology - https://journals.plos.org/plosbiology/feed/atom
*    PNAS - http://www.pnas.org/rss/current.xml

