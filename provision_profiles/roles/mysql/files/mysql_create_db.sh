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
SOCKET="/var/run/mysqld/mysqld.sock"

function generate_sql {
  echo "CREATE USER '$MYSQL_USER'@'%' IDENTIFIED BY '$MYSQL_PASSWORD';"
  echo "CREATE DATABASE $MYSQL_DATABASE;"
  echo "GRANT ALL ON $MYSQL_DATABASE.* TO '$MYSQL_USER'@'%';"
  echo 'FLUSH PRIVILEGES;'
}

# Wait for the container to start
CONTAINER=$(docker ps | grep "$MYSQL_CONTAINER")
while [[ -z "$CONTAINER" ]]; do
  echo 'Waiting for MySQL container to start'
  sleep 2
  CONTAINER=$(docker ps | grep "$MYSQL_CONTAINER")
done

# Wait for the MySQL container to come online
RETRIES=0
set +e
while [ "$RETRIES" -lt 5 ]; do
  docker exec "$MYSQL_CONTAINER" test -S "$SOCKET"
  if [ "$?" == 0 ]; then
    echo "MySQL is running."
    break
  else
    echo "Waiting for MySQL to start..."
    sleep 2
  fi
done
set -e

# Create SQL file
generate_sql > "/tmp/$MYSQL_USER.sql"

# Copy file into container
docker cp "/tmp/$MYSQL_USER.sql" $MYSQL_CONTAINER:/root/createdb.sql

# Execute the SQL file
RETRIES=0
set +e
while [ "$RETRIES" -lt 5 ]; do
  docker exec $MYSQL_CONTAINER sh -c '\
    exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD" \
    -e "source /root/createdb.sql;"'

  if [ "$?" == 0 ]; then
    echo 'Successfully created database...'
    break
  else
    echo 'Failed to create database. Retrying...'
    sleep 2
    let RETRIES=RETRIES+1
  fi
done
set -e

# Clean up
docker exec $MYSQL_CONTAINER rm /root/createdb.sql

touch /root/.created-mysql-database-$MYSQL_USER
