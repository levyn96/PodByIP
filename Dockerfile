FROM python:3-slim
RUN mkdir app
WORKDIR app
RUN pip install kubernetes && pip install flask 
ADD main.py . 
EXPOSE 5000
CMD [ "python", "/app/main.py" ]
