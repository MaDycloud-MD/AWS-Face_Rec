Dedicated to exploring diverse image recognition techniques and their multifaceted applications across various domains. Proficient in the field of computer vision, specializing in the identification and classification of objects. Aiming to elucidate the efficacy and adaptability of image recognition methodologies and their profound influence on industrial sectors.

Key Focus:

- In-depth analysis of image recognition techniques
- Expanding applications within different domains
- Object identification and classification expertise
- Demonstrated commitment to exploring computer vision advancements
- Highlighting the potential impact on industrial landscapes


# Commands

- Install aws-shell
```
pip install aws-shell
```

- Configure
```
aws configure
```

- Create a collection on aws rekognition
```
aws rekognition create-collection --collection-id facerecognition_collection --region us-east-1
```

- Create table on DynamoDB
```
aws dynamodb create-table --table-name facerecognition \
--attribute-definitions AttributeName=RekognitionId,AttributeType=S \
--key-schema AttributeName=RekognitionId,KeyType=HASH \
--provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
--region us-east-1
```

- Create S3 bucket
```
aws s3 mb s3://bucket-name --region us-east-1
```
