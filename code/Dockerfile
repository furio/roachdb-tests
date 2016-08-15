FROM ubuntu:16.04
RUN apt-get update && apt-get install -y python python-pip python-psycopg2
COPY docker-wait.sh /tmp/loopme.sh
RUN chmod +x /tmp/loopme.sh
RUN pip install ptvsd
RUN mkdir /tmp/py-project
VOLUME ["/tmp/py-project"]
# Fake loop to keep container opened
CMD ["/tmp/loopme.sh"]