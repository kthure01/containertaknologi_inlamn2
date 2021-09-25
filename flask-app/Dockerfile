FROM python:3.9-alpine3.13

LABEL vendor="Devops by Kent" \
    maintainer="Kent Thureson" \
    com.devops.kent.authors="kent.ho.thureson@gmail.com" \
    com.devops.kent.version="1.0.0" \
    com.devops.kent.release-date="2021-09-20"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
