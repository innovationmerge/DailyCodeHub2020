// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Week with AWS S3 Node SDK

// Node program to configure Node SDK to interact with AWS S3
/* **************** Prerequisites ****************
Get Access Key ID and Secret Access Key 
from AWS console -> My Security Credentials ->   Access keys -> Create
Store it in dir ~/.aws/credentials (Linux, Unix, and macOS) or C:\Users\USER_NAME\.aws\credentials (Windows).
*/
// **************** Install AWS SDK Node module ****************
// npm install aws-sdk

// **************** Configuration ****************
// Load the SDK for JavaScript
var AWS = require('aws-sdk');
// Set the Region 
AWS.config.update({region: 'us-west-2'});
// Get current Region, Access key, Secret Access key (Confidential Information)
console.log("Region: ", AWS.config.region);
console.log("Access key:", AWS.config.credentials.accessKeyId);
console.log("Secret Access key:", AWS.config.credentials.secretAccessKey);

/* **************** Output ****************
Region:  us-west-2
Access key: ****************************
Secret Access key: ****************************
*/


