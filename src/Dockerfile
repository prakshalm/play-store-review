FROM python:3.9

WORKDIR /workspace

RUN cd /workspace
COPY . /workspace
RUN pip install -r requirements.txt

CMD ["python","main.py"]