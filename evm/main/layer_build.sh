#!/bin/bash
DOCKER_BUILDKIT=1
PYTHON_VERSION=$1
DELETE=$2

mkdir -p ~/layer/
if [ "$DELETE" = "1" ]; then
  echo "Deleting python folder and zip file"
  rm -rf ~/layer/python ~/layer/python_layer.zip
fi

if [ -z "$PYTHON_VERSION" ]; then
  echo "Please provide a Python version as an argument. For example: ./layer_build.sh 3.7"
  exit 1
fi

docker build --build-arg PYTHON_VERSION=$PYTHON_VERSION -t my-lambda-layer .
docker run --name temp-container my-lambda-layer &
sleep 3
docker cp temp-container:/var/task/python ~/layer/python
docker stop temp-container
docker rm temp-container

du -sh ~/layer/python
ls -lh ~/layer/python | wc -l
tree -L 2 ~/layer/python
#zip -r /layer/python_layer.zip /layer/python
cd ~/layer
zip -r -q -9 python_layer.zip python


ls -lh ~/layer/python_layer.zip

S3_BUCKET=lambda-artifacts-f87dd42ec0fb11e5
LAYER_NAME=my-lambda-layer
LAYER_DESC="My Lambda Layer with dependencies"
AWS_REGION=ap-southeast-1

aws s3 cp ~/layer/python_layer.zip s3://$S3_BUCKET/

aws lambda publish-layer-version \
  --layer-name $LAYER_NAME \
  --description "$LAYER_DESC" \
  --content S3Bucket=$S3_BUCKET,S3Key=python_layer.zip \
  --compatible-runtimes python$PYTHON_VERSION \
  --region $AWS_REGION

cp -v ~/layer/python_layer.zip /layer/python_layer.zip