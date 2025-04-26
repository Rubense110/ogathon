Para lanzar las apps usamos uvicorn, para lanzar:

uvicorn main:app --host 0.0.0.0 --port 8080

build
docker build -t ogathon-challenges-api -f Dockerfile .

run
docker run -d -p 8080:8080 --env ASPNETCORE_HTTP_PORTS=8080 --name ogathon-challenges-api ogathon-challenges-api
