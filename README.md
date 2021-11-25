# loan app

simple dumb flask app for now

to run it locally:

```bash
export FLASK_APP=app.py
flask run
```

URL: <https://github.com/erwangranger/loan-application-app.git>


* build

```bash
buildah bud -f Dockerfile -t loanapp:01 .
```

run

```bash
podman run --rm -it -p 0.0.0.0:5000:5000 loanapp:01
#podman run --rm -d -p 5000:5000 loanapp:01
```

