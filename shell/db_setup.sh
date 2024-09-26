#Set up a Docker container of PSQL DB
docker volume create vicarius_task_vol
docker run --name vicarius-task-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -v vicarius_task_vol:/var/lib/postgresql/data -d -p 5432:5432 postgres
