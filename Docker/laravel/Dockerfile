FROM httpd:alpine

MAINTAINER David Delgado <lokiteitor513@gmail.com>

RUN apk --no-cache add \
    curl \
    php7 \
    php7-openssl \
    php7-pdo \
    php7-mbstring \
    php7-tokenizer \
    php7-xml \
    php7-ctype \
    php7-json \
    php7-pdo_mysql \
    php7-apache2 \
    php7-session

#RUN a2enmod rewrite
RUN chown www-data:www-data -R /usr/local/apache2/htdocs/


#ENTRYPOINT ["/bin/bash"]

COPY httpd-foreground /usr/local/bin/
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf

EXPOSE 80
CMD ["httpd-foreground"]
