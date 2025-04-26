Para lanzar las apps usamos uvicorn, para lanzar ejecutar los comandos:

docker build -t ogathon-challenges-api -f Dockerfile .
docker run -d -p 8080:8080 --env ASPNETCORE_HTTP_PORTS=8080 --name ogathon-challenges-api ogathon-challenges-api




Para reiniciar:

sudo docker stop ogathon-challenges-api
sudo docker rm ogathon-challenges-api
sudo docker build -t ogathon-challenges-api -f Dockerfile .
sudo docker run -d -p 8080:8080 --env ASPNETCORE_HTTP_PORTS=8080 --name ogathon-challenges-api ogathon-challenges-api
