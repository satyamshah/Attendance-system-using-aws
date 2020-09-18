import boto3
def list_collections():
 max_results=2

 client=boto3.client('rekognition')
 #Display all the collections
 print('Displaying collections...')
 response=client.list_collections(MaxResults=max_results)
 collection_count=0
 done=False

 while done==False:
    collections=response['CollectionIds']
    for collection in collections:
        print (collection)
        collection_count+=1

    if 'NextToken' in response:
        nextToken=response['NextToken']

    else:
        done=True

    response=client.list_collections(NextToken=nextToken,MaxResults=max_results)

   
    return collection_count
def main():
 collection_count=list_collections()
 print("collections: " + str(collection_count))
if __name__ == "__main__":
    main()
