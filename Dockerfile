FROM solr:8.10

COPY titles.json /data/titles.json

COPY schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

COPY synonyms/synonyms.txt /data/synonyms.txt

COPY web.xml /opt/solr/server/solr-webapp/webapp/WEB-INF/web.xml

USER root

RUN chmod +x /scripts/startup.sh

USER solr

ENTRYPOINT ["/scripts/startup.sh"]
