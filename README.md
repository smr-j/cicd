# Cloud Computing : CI/CD Workflows - Updated

The general structure of this repo is taken from the prior assignment. This repository currently contains code files for a simple CI/CD workflow, related tests, and Dockerfiles for both code files, in addition to a docker-compose.yml.

## About the Workflow
The workflow in this repository is configured to automatically run the test.py file in the src folder every time anything is pushed back to any branch.
This workflow can also be run manually by going to the 'Actions' tab and selecting 'github-actions-practice' which can be run with a 'workflow-dispatch' event trigger.

## References

Sources consulted largely include the following in addition to Docker, Localstack, Boto3, Pytest, and AWS documentation: 

https://stackoverflow.com/questions/3825990/http-response-code-for-post-when-resource-already-exists
https://stackoverflow.com/questions/33297172/boto3-error-botocore-exceptions-nocredentialserror-unable-to-locate-credential
https://whattodevnow.medium.com/using-localstack-with-docker-compose-to-mock-aws-services-bb25a5b01d4b
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/
https://testdriven.io/blog/flask-pytest/
