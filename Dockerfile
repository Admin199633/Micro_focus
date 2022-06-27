FROM python:3
COPY Flask.py /
EXPOSE 80:5000
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "./Flask.py" ]
