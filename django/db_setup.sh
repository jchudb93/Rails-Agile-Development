
user= ecomstoreuser
password=ecomstore
dbname=ecomstore

psql -U postgres -c "create user $user with \
                     createdb login password '$password'"

echo "Created user '$user'"

psql -U postgres -c "create database $dbname with \
                     owner = $user \
                     encoding = utf8"

echo "Created database '$dbname' owned by user '$user'"
echo "Done."
