# Question:Descriptions on how you modified the template to conduct the testing if any. If you propose a different approach than the template, explain how you did that and justify why.

- Description:
   1. A summary of what the pull request changes: all reviewers are able to figure out what have been changed quickly.
   2. Sections of the assignment's guidelines this pull request addresses: find out which requirement or constraint this PR addresses.
   3. Issues this pull request addresses: all reviewers are able to see which issue is related to this PR.

- Type:
   1. Bug Fix: this checkbox shows that current PR is resolving bugs.
   2. New Feature: this checkbox shows that current PR is add new features to project.
   3. New test case(s): this checkbox shows that current PR is add new test cases.
   4. Refactoring/cleaning: this checkbox shows that current PR is deleting codes from project.
   5. Breaking change: this checkbox shows that current PR contains breaking change, should be reviewed carefully.
   6. Documentation: this checkbox shows that current PR is adding documentation for project.

- Testing:
   1. Describe any testing you accomplished and provide instructions on how to replicate it: all reviewers can view the accomplishment of current test cases and reproduce test case if test failed.

- Checklist:
   1. Ran PyLint and have resolved any fixable formatting errors: ensure every PR is formatted for better readability.
   2. Included comments to describe how the code works: all reviewers can understand the logic of codes .
   3. Ran new and existing unit tests locally without causing any warnings or errors: all code must be ran under local env before PR.
   4. No unneeded modifications within the pull request, which for example may be caused by using "git add .": PR should not contain unrelated file change.
   5. If the pull request contains any merge conflicts, then please address them at the time of creating the pull request: avoid merge conflicts