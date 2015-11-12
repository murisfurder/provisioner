FROM python:2-onbuild
RUN apt-get update && apt-get install sshpass && apt-get clean
ENV ANSIBLE_HOST_KEY_CHECKING=False
CMD [ "python", "-u", "./app.py"  ]
