#!/bin/bash

####CONSTANTS
echo "Setting environment variables for profile: "$1
PROFILE=$1

####LOGIC WHICH GREPS FOR THE PROFILE IN AWS CREDS FILE, GRABS THE KEYS, MAKES KEY UPPERCASE AND EXPORTS AS ENVIRONMENT VARIABLE
export "$(grep $PROFILE $HOME/.aws/credentials -A 2 | grep aws_access_key | sed 's/ //g' | sed 's/aws_access_key_id/AWS_ACCESS_KEY_ID/g')"
export "$(grep $PROFILE $HOME/.aws/credentials -A 2 | grep aws_secret_ | sed 's/ //g' | sed 's/aws_secret_access_key/AWS_SECRET_ACCESS_KEY/g')"
