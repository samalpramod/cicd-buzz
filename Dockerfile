RUN pip install -r /src/requirements.txt
COPY app.py /src
COPY buzz /src/buzz
COPY static /src/static
COPY templates /src/templates
CMD python /src/app.py
