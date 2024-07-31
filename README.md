# Cloud Computing : CI/CD Workflows [REST API Update]

The general structure of this repo is taken from the prior assignment, although I have a feeling that this isn't traditional structure, and I'm somewhat questioning whether I set this up correctly as per the assignment requests.
This repository currently contains code files for an extremely simple REST API, related tests, and Dockerfiles for both code files.
I'm going to be 100% honest here: I did not run this prior to committing. I just checked the code as best as I could and prepared to upload it. As far as I can tell, the code is correctly written, but the constructed workflow is a disaster.

## About the Workflow
The workflow in this repository is configured to automatically run the test.py file in the src folder every time anything is pushed back to any branch. Unfortunately, it is also automatically running the rest.py file until I manually cancel the action. While I know the REST API is supposed to run until manually stopped, I'm not sure this is the best method for manually stopping it.
These workflows can also be run manually by going to the 'Actions' tab and selecting 'github-actions-practice' which can be run with a 'workflow-dispatch' event trigger.
I'm not sure this workflow is configured correctly since these two aren't decoupled into their own workflows.

As of the time that I updated this README.md file, the tests weren't working correctly because I wasn't creating the URL I've specified in the test_Dockerfile. This is on me - I'm trying to fix it but there aren't many resources I've found that cover this material.

## Notes

I'm well-aware that there are likely a handful of extra tests I should've written, like verifying the url was getting constructed correctly, but to be honest, I found getting even this much done to be somewhat overwhelming. I understand the separate pieces of what I've written, but I don't understand how to put them into a seamless workflow, and that's reflected in the fact that I'm struggling to get the tests running.


## References

Sources consulted while trying to figure this out largely include the following in addition to Docker, Github, and Flask documentation: 

https://dev.to/codemaker2015/build-and-deploy-flask-rest-api-on-docker-25mf
https://restfulapi.net/http-status-codes/
https://developers.lseg.com/en/article-catalog/article/getting-start-unit-test-for-an-http-rest-application-with-python
https://medium.com/@oyetoketoby80/how-to-write-unit-test-for-your-rest-api-f8f71376273f
https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
https://docs.github.com/en/actions/using-containerized-services/about-service-containers

While I did Google other things and reference some of the in-class work, I'm not sure that those things helped or informed what I did.
