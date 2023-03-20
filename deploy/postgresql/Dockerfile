FROM postgres
ENV POSTGRES_PASSWORD <PWD>
ENV POSTGRES_DB <DB_NAMW>
COPY cnk_init.SQL /docker-entrypoint-initdb.d/
