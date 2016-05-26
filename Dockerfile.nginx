FROM nginx
RUN openssl dhparam -out /etc/ssl/dhparam.pem 2048
COPY docker/prov.crt /etc/ssl/private/prov.crt
copy docker/prov.key /etc/ssl/private/prov.key
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
COPY docker/nginx_ssl.inc /etc/nginx/ssl_params.inc
COPY docker/nginx_le.inc /etc/nginx/le.inc

# Docker for Mac Beta doesn't like chained commands. Separating.
RUN mkdir -p /var/www
RUN touch /etc/nginx/api_auth.inc
RUN touch /etc/nginx/.htpasswd
