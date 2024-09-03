docker-compose up -d postgres_primary postgres_replica



docker exec -it postgres-postgres_primary-1 psql -U user -d postgres
docker exec -it postgres-postgres_replica-1 psql -U replicator -d postgres
