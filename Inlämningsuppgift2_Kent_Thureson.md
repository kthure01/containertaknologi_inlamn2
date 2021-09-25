**Inlämningsuppgift 2**

**Del 1, Teoretiskt**

**1.1 Docker och containerteknologi**

- Vad är Docker(plattformen)?
- Vad är en Docker Image och hur relaterar en sådan till Docker Containers?
- Vad innebär containerteknologi?
- Vad är Docker Registry?
- Hur lyder Docker Linux Kernels arbetsbeskrivning (vad den gör och hur det går till)?
- På vilket sätt kan Docker och Docker Containers jämföras med fartygstransporter? 
- Vad händer när vi har en Dockerfile och kör "docker build ."? Gå igenom build-processen

**1.2 Docker Client**

**1.3 Docker Compose**

version: "3.8"
services: 
flask:
container\_name: flaskcontainer
build:
`  `context: ./app
`  `dockerfile: Dockerfile.dev
ports:
`  `- "5000:5000"
depends\_on: 
`  `- db
networks:
`  `- flask\_app\_net
db:
container\_name: dbcontainer
image: postgres:latest
restart: always
environment: 
`  `POSTGRES\_DB: mydb
`  `POSTGRES\_PASSWORD: postgres
`  `POSTGRES\_USER: postgres
volumes:
`  `- postgres\_data:/var/lib/postgresql/data/
networks:
`  `- flask\_app\_net

networks:   
flask\_app\_net:
`    `driver: bridge
​
volumes:
postgres\_data:
​

**Del 2, Praktiskt**

**2.1 Flask app**

**2.2 Multi-stage Build**

**2.3 Docker Compose**

**3. Projekt**
