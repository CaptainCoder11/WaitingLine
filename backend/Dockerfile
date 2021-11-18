FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY . /usr/app/
EXPOSE 3333
WORKDIR /usr/app/
RUN pip install -r requirement.txt

CMD ["uvicorn", "src.main:app", "--reload" , "--host", "0.0.0.0" , "--port" , "3333"]
