FROM python:3
COPY Flask.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "./Flask.py" ]
