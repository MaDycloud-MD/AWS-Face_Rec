# Project Title: 
## __Automated Face Recognition System Deployment using AWS Rekognition__
![Thumbnail](.\AWSFaceRekognition)

### Overview:
This project showcases the deployment of a robust face recognition system harnessing AWS Rekognition, strategically employing multiple AWS services including S3, Lambda, DynamoDB, and IAM roles.

### Objective:
The primary aim is to engineer a proficient face recognition system, empowered by AWS Rekognition's machine learning algorithms, capable of accurately identifying individuals depicted within images.

### Key Components:

#### AWS Services Utilized:

- __Amazon Rekognition:__ Employed for precise facial analysis and recognition within image data.
- __AWS Lambda:__ Developed serverless functions, triggered by S3 events upon image uploads, facilitating automated processing.
- __Amazon S3 (Simple Storage Service):__ Functioned as a secure storage repository for images while enabling seamless integration with Lambda functions.
- __Amazon DynamoDB:__ Leveraged as a NoSQL database, strategically storing facial prints (face IDs) and associated identities for recognition purposes.
- __IAM Role:__ Carefully crafted to allocate granular permissions, ensuring secure access for Lambda functions to DynamoDB, S3, and Rekognition services.

#### Implementation Steps:
1) __S3 Bucket Configuration:__ Established a dedicated S3 bucket ('famous persons-images') to efficiently manage and store images, activating Lambda functions upon new uploads.
2) __AWS Rekognition Collection Development:__ Created a specialized Rekognition collection ('famous persons') to centralize and index facial prints for recognition accuracy.
3) __DynamoDB Table Setup:__ Configured a DynamoDB table ('face recognition') as a robust repository, housing facial prints and associated identities for efficient retrieval during recognition processes.
4) __Lambda Function Development:__ Programmed Python-based Lambda functions, triggered by S3 events, orchestrating the extraction of facial prints from uploaded images and their subsequent storage within DynamoDB.
5) __Testing the Recognition System:__ Executed comprehensive testing scripts to validate the effectiveness of the recognition system, inputting images and ensuring accurate identification of known personalities while appropriately handling unrecognized individuals.

#### Workflow:

1) __Image Upload Phase:__ Uploaded images of notable personalities to the designated S3 bucket, accompanied by metadata specifying individual names for indexing purposes.
2) __Lambda Trigger Process:__ Lambda functions were automatically activated upon image uploads to S3, efficiently extracting facial prints using Rekognition API and securely storing them within DynamoDB.
3) __Recognition Process:__ Rigorous testing with diverse images verified the system's accuracy. The Rekognition API compared facial prints against indexed data in DynamoDB, successfully identifying known personalities while appropriately flagging unknown individuals.

#### Conclusion:
The project effectively demonstrates the streamlined integration of AWS Rekognition and associated services to craft a proficient face recognition system. By leveraging machine learning capabilities, it exemplifies a reliable approach to implementing accurate face recognition features without the complexities of intricate algorithm development. To further enhance accuracy, the system's index can be continually enriched by incorporating additional data.

#### Key Takeaways:

- AWS Rekognition streamlines and simplifies face recognition implementation.
- Seamless integration of AWS services ensures a robust and scalable system architecture.
- Continuous improvement opportunities exist by enriching the recognition index with additional data.


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
aws rekognition create-collection --collection-id FamousPerson_FaceRec --region ap-south-1

```

- Create table on DynamoDB
```
aws dynamodb create-table --table-name AWS_facerecognition \
--attribute-definitions AttributeName=RekognitionId,AttributeType=S \
--key-schema AttributeName=RekognitionId,KeyType=HASH \
--provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
--region ap-south-1
```

- Create S3 bucket
```
aws s3 mb s3://facerec-famousperson --region ap-south-1
```


Recognizing Tech Raj for their instrumental role in deploying an advanced Face Recognition System utilizing AWS Rekognition. Their expertise in integrating S3, Lambda, DynamoDB, and IAM roles was pivotal in engineering a precise recognition system leveraging machine learning for accurate image identification. Their meticulous management of setup, programming, and seamless integration showcased the efficiency of AWS Rekognition, resulting in a scalable system with ongoing enhancement capabilities through data enrichment for improved accuracy.

GitHub ID: https://github.com/teja156
<br>
Video Link: https://youtu.be/oHSesteFK5c?si=wRPvsnC7hC0C603A
