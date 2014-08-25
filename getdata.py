#!/usr/bin/env python
import urllib
import sys
import json

base = 'http://alpha.avoindata.fi/data/api'
demodatafile = 'data.json'
current = json.load(open(demodatafile))

datasets = [
	"kuormituksen-testidataa",
	"baconese-testidataa"
    ]

def sync():
    for name in datasets:
        print 'Retrieving: %s' % name
        out = get_dataset(name)
        current['datasets'][name] = out

    outfo = open(demodatafile, 'w')
    json.dump(current, outfo, indent=2, sort_keys=True)

def get_dataset(name):
    url = base + '/3/action/package_show?id=' + name
    fo = urllib.urlopen(url)
    parsed = json.load(fo)
    parsed = parsed['result']
    from pprint import pprint
    pprint(parsed)
    for resource in parsed['resources']:
        for key in ['webstore_url', 'webstore_last_updated',
                'resource_group_id',  'position',
                'cache_url']:
            del resource[key]
    for key in ['isopen', 'groups', 'revision_id',
        'type', 'metadata_modified', 'metadata_created',
        'id'
        ]:
        del parsed[key]
    return parsed

if __name__ == '__main__':
    sync()
