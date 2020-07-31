
import boto3
import io
import csv
from PIL import Image
from pprint import pprint
from datetime import date
from csv import DictWriter



def append_dict_as_row(file_name, dict_of_elem, field_names):
# Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
# Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
# Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)


fields = ['Faceid','Name', 'Date']
filename = "attendance1.csv"
today = date.today()
mydict  = {'Faceid': None, 'Name': None,'Date':None}




rekognition = boto3.client('rekognition', region_name='ap-south-1')
dynamodb = boto3.client('dynamodb', region_name='ap-south-1')

image = Image.open("image15.jpeg")
stream = io.BytesIO()
image.save(stream,format="JPEG")
image_binary = stream.getvalue()

response = rekognition.detect_faces(
    Image={'Bytes':image_binary}
        )

all_faces=response['FaceDetails']

# Initialize list object
boxes = []

# Get image diameters
image_width = image.size[0]
image_height = image.size[1]

# Crop face from image
for face in all_faces:
    box=face['BoundingBox']
    x1 = int(box['Left'] * image_width) * 0.9
    y1 = int(box['Top'] * image_height) * 0.9
    x2 = int(box['Left'] * image_width + box['Width'] * image_width) * 1.10
    y2 = int(box['Top'] * image_height + box['Height']  * image_height) * 1.10
    image_crop = image.crop((x1,y1,x2,y2))

    stream = io.BytesIO()
    image_crop.save(stream,format="JPEG")
    image_crop_binary = stream.getvalue()

    # Submit individually cropped image to Amazon Rekognition
    response = rekognition.search_faces_by_image(
            CollectionId='family_collection',
            Image={'Bytes':image_crop_binary}
            )

    if len(response['FaceMatches']) > 0:
        # Return results
        print ('Coordinates ', box)

        for match in response['FaceMatches']:

            face = dynamodb.get_item(
                TableName='family_collection',
                Key={'RekognitionId': {'S': match['Face']['FaceId']}}
                )

            if 'Item' in face:
                person = face['Item']['FullName']['S']
            else:
                person = 'no match found'

            mydict['Faceid']=match['Face']['FaceId']
            mydict['Name']=person
            mydict['Date']=today
            append_dict_as_row('attendance1.csv', mydict, fields)
            print (match['Face']['FaceId'],match['Face']['Confidence'],person)









            #print(match['Face']['FaceId'])  #FaceId
            #print('----------')
            #print(match['Face']['Confidence'])  #percentage
            #print('-------------')
            #print(person)             #FullName
