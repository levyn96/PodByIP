FROM python:3-slim
RUN pip install kubernetes
ADD main.py . 
CMD [ "python", "./main.py" ]
