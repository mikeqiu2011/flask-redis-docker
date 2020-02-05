https://docs.docker.com/engine/swarm/stack-deploy/

docker swarm init --advertise-addr \$(hostname -i)
docker node ls

docker service create --name registry -p 5000:5000 registry:2

docker-compose build
docker stack deploy -c docker-compose.yml flask-demo

curl -X POST -H "Content-Type: text/plain" --data "hello mike" http://localhost:5001/todos/1
