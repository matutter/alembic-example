#!/bin/bash

docker-compose up -d

psql="docker exec -u postgres `docker-compose ps -q | head -1` psql -c"
$psql 'drop database test_alembic;'
if ! $psql 'create database test_alembic;'; then
  echo "Failed to create databse..."
  exit 2
fi

rm -rf migrations/versions/*

cat model_snippets/models_1.py > models.py
python init.py
python main_1.py

./add-migration.sh init db
alembic upgrade head

cat model_snippets/models_2.py >> models.py
python main_2.py

./add-migration.sh create admin user
alembic upgrade head

cat model_snippets/models_3.py >> models.py
python main_3.py

./add-migration.sh create super admin user
alembic upgrade head
