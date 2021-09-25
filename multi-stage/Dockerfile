# Använder alpine bara för att använda en liten Linux image
# att demonstrera multi stage. Som alias får den heta builder
FROM alpine AS builder

# Kallar min arbetsfolder för /app1
WORKDIR /app1

# Kopierar in några filer till /app1
COPY nginx.conf ./default.conf
COPY ./www/index.html .


# Det är här det kommer hända.
# Använder nginx officiella image för att köra en webbserver
FROM nginx

# Här kallar jag arbetsfoldern för /app2
WORKDIR /app2

# Här kopierar jag in filerna från byggsteget, builder, till de platser
# de ska ha för att lösa uppgiften att få utskrivit "Hello World"
# när jag surfar in på localhost:80
COPY --from=builder /app1/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app1/index.html /usr/share/nginx/html

# Detta är kommandot för att starta webbservern i containern.
CMD ["nginx", "-g", "daemon off;"]


# Detta kommando bygger min egen nginx image
# docker build -t kthure01/nginx .

# Detta kommando använder jag för att starta en ny container.
# docker run -d -p 80:80 -v $(pwd)/www:/usr/share/nginx/html kthure01/nginx
#
# "-d" kör containern i bakgrunden
# "-p" talar om att jag vill publicera en containers port på någon port jag väljer
# "-v" "Monterar/länkar" en folder på min dator till en plats i containern.
# Att använda volymer är ett sätt att spara data utanför containern.
# 