# cnk backend service

docker image for backend service [dockerhub](https://hub.docker.com/repository/docker/yuyatinnefeld/cloud-native-kiosk-backend/general).

## Local Run

* `pip install -r requirements.txt` - install pacakges
* `uvicorn main:app --reload` - Start the FastAPI server.
* `open http://127.0.0.1:8000` - Open the pages

## Backend Project layout

    backend/
        app                         # FastAPI Source code
        docs/
            index.md                # The documentation homepage.
            gen_mkdocs_pages.py     # page generator.
        mkdocs.yml                  # The mkdocs configuration file.
        Dockerfile
        requirements_dev.txt        # debugging and CICD relevant requirements
        requirements.txt            # production relevant requirements
