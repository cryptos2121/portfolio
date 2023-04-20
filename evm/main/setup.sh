#!/bin/bash

pip install awscliv2 aws-sam-cli; alias aws='awsv2'; awsv2 --install; aws --version; sam --version
pip install python-decouple

sudo yum install jq tree -y

