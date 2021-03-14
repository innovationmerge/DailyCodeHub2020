// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with AWS S3 Node SDK

// Node program to Upload a File to an Amazon S3 Bucket

/* **************** Prerequisites ****************
        Refer to DAY 112 Post */
// **************** Configuration ****************
// Load the SDK for JavaScript
var AWS = require('aws-sdk');

// Create S3 service object
s3 = new AWS.S3();
// call S3 to retrieve upload file to specified bucket
var uploadParams = {Bucket: "nnm-test3", Key: '', Body: ''};
var file = "test_file.txt";

// Configure the file stream and obtain the upload parameters
var fs = require('fs');
var fileStream = fs.createReadStream(file);
fileStream.on('error', function(err) {
  console.log('File Error', err);
});
uploadParams.Body = fileStream;
var path = require('path');
uploadParams.Key = path.basename(file);

// call S3 to retrieve upload file to specified bucket
s3.upload (uploadParams, function (err, data) {
  if (err) {
    console.log("Error", err);
  } if (data) {
    console.log("Upload Success", data.Location);
  }
});
/* ******** Output *********
Upload Success 
https://****-nnm-test3.s3.amazonaws.com/test_file.txt
*/



