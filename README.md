# loan app

simple dumb flask app for now

to run it locally:

```bash
export FLASK_APP=app.py
flask run
```

URL:
https://github.com/erwangranger/loan-application-app.git


* build

```bash
buildah bud -f Dockerfile -t loanapp:01 .
```

run

```bash
podman run --rm -it -p 0.0.0.0:5000:5000 loanapp:01
#podman run --rm -d -p 5000:5000 loanapp:01
```

references / inspirations:

https://github.com/tiangolo/full-stack-fastapi-postgresql

https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/

https://analyticsindiamag.com/fastapi-vs-flask-comparison-guide-for-data-science-enthusiasts/

https://testdriven.io/blog/moving-from-flask-to-fastapi/

https://github.com/Vijaysinh7000/cardiac-arrest-prediction

https://www.youtube.com/watch?v=q8jaJ4Y3H7E

