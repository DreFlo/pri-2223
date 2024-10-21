#!/bin/bash

precreate-core titles

# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 5

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema.json \
    http://localhost:8983/solr/titles/schema

# Add synonyms file
cp /data/synonyms.txt /var/solr/data/titles/conf/synonyms.txt



# Populate collection
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/titles.json \
    http://localhost:8983/solr/titles/update

# Restart in foreground mode so we can access the interface
solr restart -f