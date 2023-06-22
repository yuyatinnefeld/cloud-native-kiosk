# cnk python backend service

docker image for the backend service [Docker Hub](https://hub.docker.com/repository/docker/yuyatinnefeld/cloud-native-kiosk-backend/python/general).


## Local Debugging

* Navigate into the working directory. - `cd ./deploy/backend`
* Install Python pacakges. - `pip install -r requirements.txt`
* Start the FastAPI server. -`uvicorn main:app --reload`
* Open the site. - `open http://127.0.0.1:8000`


## Python Backend Project Layout

    backend/
        app                         # FastAPI Source code
        docs/
            index.md                # The documentation homepage.
            gen_mkdocs_pages.py     # page generator.
        mkdocs.yml                  # The mkdocs configuration file.
        Dockerfile
        requirements_dev.txt        # debugging and CICD relevant requirements
        requirements.txt            # production relevant requirements
