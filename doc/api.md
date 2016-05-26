# API Documentation

## Get roles

To get the list of possible 'roles', issue a GET against `/roles` and you'll get something similar to:

```
["docker", "docker_registry", "mongodb", "mysql", "postgres", "redis", "wordpress"]
```

## Create a job

To create a task, you need to issue a POST against `/job` with the following payload:

```
{
  'role': 'SomeRole',
  'ip': 'TargetIP',
  'username': 'YourUser',
  'password': 'YourPassword'
}
```

If the task was successfully created, you should receive a 201 status code as well as the UUID for the task. The UUID is needed to get the status of the task.

For more information about the possible roles, see [Roles](#Roles).

## Get the status of a job

To get the status of a job, simply issue a GET against `/job/SomeUUID`. You should then get something like this in return (and a 200 status code):

```
{
  "status": "Done",
  "ip": "192.168.33.10",
  "attempts": 1,
  "role": "ping",
  "timestamp": "1449166675.0"
  "install_notes": "Installation notes in Markdown format (if available)."
}
```

The possible statuses for a job are:

* New
* Queued
* Provisioning
* Aborted
* Done
* Error
* Queued

## Abort a job

To abort a job, you can issue a DELETE against `/job/SomeUUID`. This should return a 204 status code if successful.

Please note that this will not *stop* a running job, but rather prevent future attempts.

It's also worth noting that deleting jobs is optional. Jobs will normally either complete (`status: Done`) or reach the maximum amount of retries. Redis will then purge these jobs with after 24 hours.

## Get Redis status

To make it easy to check the status of Redis, the output of Redis' `INFO` command has been exposed. You can get this data by issuing a GET to `/redis_status`
