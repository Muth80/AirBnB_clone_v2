#!/bin/bash

# Set MySQL connection parameters from environment variables
MYSQL_USER=$HBNB_MYSQL_USER
MYSQL_PASSWORD=$HBNB_MYSQL_PWD
MYSQL_HOST=$HBNB_MYSQL_HOST
MYSQL_DATABASE=$HBNB_MYSQL_DB

# Check if the database already exists
EXISTING_DB=$(mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -h"$MYSQL_HOST" -e "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '$MYSQL_DATABASE'" --skip-column-names)

# Create the database if it doesn't exist
if [ -z "$EXISTING_DB" ]; then
    mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -h"$MYSQL_HOST" -e "CREATE DATABASE $MYSQL_DATABASE"
fi

# Create the user and set the password
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -h"$MYSQL_HOST" -e "CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY '$HBNB_MYSQL_PWD'"

# Grant privileges to the user on the database
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -h"$MYSQL_HOST" -e "GRANT ALL PRIVILEGES ON $MYSQL_DATABASE.* TO 'hbnb_dev'@'localhost'"

# Grant SELECT privilege on performance_schema
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -h"$MYSQL_HOST" -e "GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'"

