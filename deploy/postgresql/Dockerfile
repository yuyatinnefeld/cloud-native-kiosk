FROM postgres
ENV POSTGRES_PASSWORD super_password
ENV POSTGRES_DB ckn_db
COPY cnk_init.SQL /docker-entrypoint-initdb.d/
