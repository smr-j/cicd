# Cloud Computing : CI/CD Workflows

The general structure of this repo is taken from the prior assignment, although I have a feeling that this isn't traditional structure, and I'm somewhat questioning whether I set this up correctly as per the assignment requests.
This repository currently contains code files for a simple CI/CD workflow, related tests, and Dockerfiles for both code files, in addition to a docker-compose.yml.
I'm going to be 100% honest here: I did not run this prior to committing. I just checked the code as best as I could and prepared to upload it. I believe that the code is correctly written, but the constructed workflow is a disaster.

## About the Workflow
The workflow in this repository is configured to automatically run the test.py file in the src folder every time anything is pushed back to any branch.
This workflow can also be run manually by going to the 'Actions' tab and selecting 'github-actions-practice' which can be run with a 'workflow-dispatch' event trigger.

## Notes

This assignment was a huge struggle for me. I understand some of the separate pieces of what I've written, but I don't understand how to put them into a seamless workflow, and that's reflected in the various ways that I've struggled.


## References

Sources consulted while trying to figure this out largely include the following in addition to Docker, Localstack, Boto3, and AWS documentation: 

https://stackoverflow.com/questions/3825990/http-response-code-for-post-when-resource-already-exists
