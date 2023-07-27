# How to Contribute

 Always happy to get issues identified and pull requests!

 ## General considerations

 1. Keep it small. The smaller the change, the more likely we are to accept.
 2. Changes that fix a current issue get priority for review.
 3. Check out [GitHub guide][submit-a-pr] if you've never created a pull request before.

 ## Getting started

 1. Fork the repo
 2. Clone your fork
 3. Create a branch for your changes

 This last step is very important, don't start developing from master, it'll cause pain if you need to send another change later.

 TIP: If you're working on a GitHub issue, name your branch after the issue number, e.g. `issue-123-<ISSUE-NAME>`. This will help us keep track of what you're working on. If there is not an issue for what you're working on, create one first please. Someone else might be working on the same thing, or we might have a reason for not wanting to do it.

 ## Venv

 As is best practice, you should install the project and its dependencies into a virtual environment and not your system wide Python installation.

 Personally I prefer to use the standard lib venv module for this.

 The scripts used by the following section require that your venv be named `.venv` and exist in the parent folder of the project directory.

 ```
 ├── isecapipy
 |   ├── src
 |   ├── tests
 |   ├── ...
 ├── .venv
 └── private work of yours outside project dir
 ```

To specify a unique or helpful prompt description when the venv is activated, create it with the following syntax:

    python -m venv .venv --prompt isecapipy

Which will create a prompt looking like the below image which is helpful when jumping between terminal windows:

![Prompt with venv description](/docs_imgs/venv_with_prompt.PNG "venv w. prompt")

 ## Pre-commit

 GitHub Actions is going to run Pre-commit hooks on your PR. If the hooks fail, you will need to fix them before your PR can be merged. It will save you a lot of time if you run the hooks locally before you push your changes. To do that, you need to install pre-commit on your local machine.

 ```shell
 pip install pre-commit
 ```

 Once installed, you need to add the pre-commit hooks to your local repo.

 ```shell
 pre-commit install
 ```

 Now, every time you commit, the hooks will run and check your code. If they fail, you will need to fix them before you can commit.

 If it happened that you committed changes already without having pre-commit hooks and do not want to reset and recommit again, you can run the following command to run the hooks on your local repo.

 ```shell
 pre-commit run --all-files
 ```

### Windows Users Extra Requirements

On Windows, as bash is not installed natively, you may need to add your git/git bash Programs folder to your PATH environment variable for the scripts called by pre-commit to run.

The scripts start with the standard #!/usr/bin/sh 'shebang' line to tell the interpreter what program to use to run the scripts.

Windows doesn't normally use these lines however your implimentation of git should, but for it to run properly, the location containing the /usr directory needs to be on PATH.

For regular Git for Windows / Git Bash, this would normally be found at "C:\Program Files\Git" for modern 64 bit installs.

Add this to Path to ensure the pre-commit hooks run successfully.

 ## Help Us Improve This Documentation

 If you find that something is missing or have suggestions for improvements, please submit a PR.

 [submit-a-pr]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
