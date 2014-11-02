HOST="localhost"
USER="root"
PASSWORD="baza1"

echo 'Installing CamelDb ...' 

mysql -h $HOST -u $USER -p$PASSWORD < scripts/drop_user.sql
mysql -h $HOST -u $USER -p$PASSWORD < scripts/create_database.sql
mysql -h $HOST -u $USER -p$PASSWORD < scripts/create_user.sql
mysql -h $HOST -u $USER -p$PASSWORD < scripts/install.sql

echo 'Success!'


