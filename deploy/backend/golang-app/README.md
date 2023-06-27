# Run Golang App
```bash
docker build -t yuyatinnefeld/golang-simple-app .
docker run  -e MESSAGE="hi mom, i'm using golang!" -it -p 9999:9999 yuyatinnefeld/golang-simple-app
```