# Issue Description

Pydantic on Linux OS fails to read files and process vars
in `secrets_dir`, but Python core `open("path/to/file").read()` works fine.

On MacOS 11 reading secrets from `secrets_dir` with Pydantic works OK.

To test:
 - build the image using `Dockerfile` here
 - `cd /project`
 - `python config.py`
 - observe the printed output
 - check relevant dirs and file contents