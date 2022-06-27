FROM python:3
COPY Flask.py /
COPY db_connector.py /
EXPOSE 80:80
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "./Flask.py" ]
