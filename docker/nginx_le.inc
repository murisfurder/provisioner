# Required for Let's Encrypt
location ~ /.well-known {
  root /var/www;
  try_files $uri $uri/ =404;
  allow all;
}
