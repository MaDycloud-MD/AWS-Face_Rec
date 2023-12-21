import boto3
import io
from PIL import Image

rekognition = boto3.client('rekognition', region_name='ap-south-1')
dynamodb = boto3.client('dynamodb', region_name='ap-south-1')

image_path = input("Enter path of the image to check: ")

image = Image.open(image_path)

if(image_path.endswith(".jpg")):
        stream = io.BytesIO()
        image.save(stream,format="JPEG")
        image_binary = stream.getvalue() 
    
else:
        # Convert image to RGB (if necessary)
        if image.mode == "RGBA":
            rgb_image = image.convert("RGB")
        else:
            rgb_image = image

        # Save as JPEG
        stream = io.BytesIO()
        rgb_image.save(stream, format="JPEG")
        image_binary = stream.getvalue()

        # Save the converted image
        with open("output_image.jpg", "wb") as output_file:
            output_file.write(image_binary)
            print("Image converted and saved as JPEG")


response = rekognition.search_faces_by_image(
        CollectionId='FamousPerson_FaceRec',
        Image={'Bytes':image_binary}                                       
        )

found = False
for match in response['FaceMatches']:
    print (match['Face']['FaceId'],match['Face']['Confidence'])
        
    face = dynamodb.get_item(
        TableName='AWS_facerecognition',  
        Key={'RekognitionId': {'S': match['Face']['FaceId']}}
        )
    
    if 'Item' in face:
        print ("Found Person: ",face['Item']['FullName']['S'])
        found = True

if not found:
    print("Person cannot be recognized")