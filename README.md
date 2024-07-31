# Cloud Computing : CI/CD Workflows

This repository currently contains code files from an extremely simplistic fighting simulator created when the owner of this repository was still learning to program in Python.

## About the Workflow
The workflow in this repository should be configured to automatically run the test.py files in the src folder every time anything is pushed back to any branch. 
It can also be run manually by going to the 'Actions' tab and selecting 'github-actions-practice' which can be run with a 'workflow-dispatch' event trigger.

The requirements.txt file is very bare-bones because the code itself is bare-bones. (I added numpy and matplotlib to requirements.txt as a method of verifying that my workflow was able to install requirements). 

## Notes

I believe that in order to include the driver.py file in the workflow, I would have to change some of my code, which was designed to take user input. I will work on it (or replace it with alternate code).


## References
Sources consulted while trying to figure this out largely include the following although I did Google several other things that did not help or work:

https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions
https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows
