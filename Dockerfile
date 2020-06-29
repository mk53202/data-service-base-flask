FROM python:3.7-alpine

ADD requirements.txt .

RUN apk add python3-dev build-base linux-headers pcre-dev postgresql-dev git postgresql-client bash

# RUN apk add postgresql-dev
RUN pip install --no-cache-dir -r requirements.txt
# RUN git clone https://github.com/masroore/pg_simple.git # this is a workaround to force install pg_simple
# RUN python3 pg_simple/setup.py install  # this is a workaround to force install pg_simple
# RUN pip install pg_simple    # this is a workaround to force install pg_simple
# Adding application files
ADD . /webapp

# Configure path /webapp to HOME-dir
ENV HOME /webapp
WORKDIR /webapp

ENTRYPOINT ["uwsgi"]
CMD ["--http", "0.0.0.0:8080", "--wsgi-file", "wsgi.py", "--callable", "app", "--processes", "1", "--threads", "8"]