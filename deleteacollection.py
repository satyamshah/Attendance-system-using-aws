#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
from botocore.exceptions import ClientError
from os import environ

def delete_collection(collection_id):


    print('Attempting to delete collection ' + collection_id)
    client=boto3.client('rekognition')
    status_code=0
    try:
        response=client.delete_collection(CollectionId=collection_id)
        status_code=response['StatusCode']
        
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print ('The collection ' + collection_id + ' was not found ')
        else:
            print ('Error other than Not Found occurred: ' + e.response['Error']['Message'])
        status_code=e.response['ResponseMetadata']['HTTPStatusCode']
    return(status_code)


def main():
    #add here the name of collection you want to delete.
    collection_id='Collection'
    status_code=delete_collection(collection_id)
    print('Status code: ' + str(status_code))

if __name__ == "__main__":
    main() 