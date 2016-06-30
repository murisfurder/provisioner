#!/bin/bash -e

function error_usage {
  echo 'Usage: mysql_createdb.sh username password'
  echo 'This will create a database by the same name as the username and grant full access to said database to the user.'
  exit 1
}

if [ -z "$1" ]; then
  error_usage
elif [ -z "$2" ]; then
  error_usage
fi

# Define the variables
MYSQL_USER="$1"
MYSQL_DATABASE="$1"
MYSQL_PASSWORD="$2"
MYSQL_CONTAINER="mysql"

function generate_sql {
  echo "CREATE USER '$MYSQL_USER'@'%' IDENTIFIED BY '$MYSQL_PASSWORD';"
  echo "CREATE DATABASE $MYSQL_DATABASE;"
  echo "GRANT ALL ON $MYSQL_DATABASE.* TO '$MYSQL_USER'@'%';"
  echo 'FLUSH PRIVILEGES;'
}

# Create SQL file
generate_sql > "/tmp/$MYSQL_USER.sql"

# Copy file into container
docker cp "/tmp/$MYSQL_USER.sql" $MYSQL_CONTAINER:/root/createdb.sql

# Execute the SQL file
docker exec $MYSQL_CONTAINER sh -c '\
  exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"\
  -e "source /root/createdb.sql;"'

# Clean up
docker exec $MYSQL_CONTAINER rm /root/createdb.sql
