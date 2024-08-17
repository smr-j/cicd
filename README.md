# Cloud Computing : CI/CD Workflows - Updated

The general structure of this repo is taken from the prior assignment, although I'm questioning whether I set this up correctly as per the assignment requests.
This repository currently contains code files for a simple CI/CD workflow, related tests, and Dockerfiles for both code files, in addition to a docker-compose.yml.
I'm going to be 100% honest here: I did not run this prior to committing and am conducting most of my checks through my tests workflow. I believe that the code is correctly written, but I'm willing to be proven wrong.

## About the Workflow
The workflow in this repository is configured to automatically run the test.py file in the src folder every time anything is pushed back to any branch.
This workflow can also be run manually by going to the 'Actions' tab and selecting 'github-actions-practice' which can be run with a 'workflow-dispatch' event trigger.

## Notes

This assignment was a huge struggle for me. I understand the different pieces of what I've written, but I'm not sure that I've implemented the required tests the way that I needed to or performed any of the necessary checks. I'm also not 100% sure that I've implemented every test, mostly because I'm not sure I understand what each test was supposed to be checking for.


## References

Sources consulted while trying to figure this out largely include the following in addition to Docker, Localstack, Boto3, Pytest, and AWS documentation: 

https://stackoverflow.com/questions/3825990/http-response-code-for-post-when-resource-already-exists
https://stackoverflow.com/questions/33297172/boto3-error-botocore-exceptions-nocredentialserror-unable-to-locate-credential
https://whattodevnow.medium.com/using-localstack-with-docker-compose-to-mock-aws-services-bb25a5b01d4b
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/
https://testdriven.io/blog/flask-pytest/
