FROM python:2-onbuild
RUN apt-get update && apt-get install -y sshpass && apt-get clean
ENV ANSIBLE_HOST_KEY_CHECKING=False
CMD [ "python", "-u", "./worker.py"  ]
