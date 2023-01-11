FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY service /service
WORKDIR /service
EXPOSE 8000
RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

# Add none root user
RUN     apk add doas; \
        adduser --disabled-password service-adduser; \
        echo 'permit service-adduser as root' > /etc/doas.d/doas.conf


USER service-adduser
#