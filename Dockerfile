FROM public.ecr.aws/lambda/python:3.8
# Copy function code
# COPY . ${LAMBDA_TASK_ROOT}
RUN mkdir ${LAMBDA_TASK_ROOT}/source
COPY . ${LAMBDA_TASK_ROOT}/source
COPY ./lambda_function.py ${LAMBDA_TASK_ROOT}
# Install the function's dependencies using file requirements.txt
# from your project folder.
# RUN /var/lang/bin/python3.8 -m pip install --upgrade pip
# COPY requirements.txt .
RUN pip3 install -r ./source/requirements.txt --target "${LAMBDA_TASK_ROOT}"
# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.lambda_handler" ]
