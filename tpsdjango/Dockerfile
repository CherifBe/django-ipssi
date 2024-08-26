FROM python:3.9.17

WORKDIR /usr/src/application

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DATABASE_URL=mysql+aiomysql://root:testing@db:3306/testing

RUN export DATABASE_URL=${DATABASE_URL}

CMD ["python", "tpsdjango/manage.py", "runserver", "0.0.0.0:8000"]