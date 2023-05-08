# Postgresql

## Setup a Local PostgreSQL Database

```
DOCKER_IMAGE="my-postgres-db"
PASSWORD="super_password"
CONTAINER_NAME="postgres-server"

docker build -t ${DOCKER_IMAGE} ./
docker run -d --name ${CONTAINER_NAME}  -e POSTGRES_PASSWORD=${PASSWORD} -p 5432:5432 ${DOCKER_IMAGE}
docker exec -it ${CONTAINER_NAME} bash
```

## Verify Postgresql Setup
```
psql -h localhost -p 5432 -U postgres --password

postgres=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access privileges
-----------+----------+----------+------------+------------+------------+-----------------+-----------------------
 ckn_db    | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            |
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            |
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
           |          |          |            |            |            |                 | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
           |          |          |            |            |            |                 | postgres=CTc/postgres
```

## Installing the PgAdmin4
```
DOCKER_IMAGE_PGADMIN="dpage/pgadmin4"
docker pull ${DOCKER_IMAGE_PGADMIN}
docker pull dpage/pgadmin4
docker run -p 5050:80 \
    -e 'PGADMIN_DEFAULT_EMAIL=user@domain.com' \
    -e 'PGADMIN_DEFAULT_PASSWORD=pwd' \
    -d ${DOCKER_IMAGE_PGADMIN}
```

### Login pq admin
```
open http://localhost:5050/
```
