import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image1.jpg','Elon Musk'),
      ('image2.jpg','Elon Musk'),
      ('image3.jpg','Bill Gates'),
      ('image4.jpg','Bill Gates'),
      ('image5.jpg','Sundar Pichai'),
      ('image6.jpg','Sundar Pichai'),
      ('image7.jpg','Jeff Bezos'),
      ("image8.jpg",'Jeff Bezos'),
      ("image9.jpg",'Neha Jetwani'),
      ("image10.jpg",'Neha Jetwani'),
      ("image11.jpg",'Neha Jetwani'),
      ("image12.jpg",'Sharukh Khan'),
      ("image13.jpg",'Sharukh Khan'),
      ("image14.jpg",'Sharukh Khan'),
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('facerec-famousperson','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
