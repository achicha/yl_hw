### How to run:
```shell
cd yl_hw/hw4
docker-compose up --build -d
alembic upgrade head
```

---------------------
### helpers
```shell
# DB migration
# https://stackoverflow.com/questions/68932099/how-to-get-alembic-to-recognise-sqlmodel-database-model
alembic revision --autogenerate -m "first commit"
alembic upgrade head
```