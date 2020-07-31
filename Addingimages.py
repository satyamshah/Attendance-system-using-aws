import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image01.jpeg','satyam'),
      ('image02.jpeg','satyam'),
      
      ('image03.jpeg','Priyanka'),
      ('image04.jpeg','Priyanka'),
     
       ('image05.jpeg','Beda'),
      ('image06.jpeg','Beda'),
     
       ('image07.jpeg','shashwat'),
      ('image08.jpeg','shashwat')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('kiitattendancebucket','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]}
                    )