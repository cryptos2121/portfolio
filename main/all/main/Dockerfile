ARG PYTHON_VERSION
FROM public.ecr.aws/lambda/python:${PYTHON_VERSION}

COPY requirements.txt ./

RUN mkdir -p /var/task/python/lib/python3.7/site-packages && \
    python -m pip install -r requirements.txt -t /var/task/python/lib/python3.7/site-packages

# RUN ls -la /var/task/python/lib/python3.7/site-packages

#CMD ["app.lambda_handler"]
CMD ["sleep", "5"]
