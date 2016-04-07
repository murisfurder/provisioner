# MongoDB

* *Name*: mongodb
* *Requirement*: Ubuntu 12.04 or later
* *Exposes ports:* 127.0.0.1:27017

Installs the [official MongoDB Docker container](https://hub.docker.com/_/mongo/). MongoDB's persistent data is stored under `/var/lib/mongodb` in the VM.

## MongoDB Cluster

* *Name*: mongodb
* *Requirement*:
  * Ubuntu 12.04 or later
  * Three VMs
  * Weave module already deployed
* *Exposes ports:* 127.0.0.1:27017

Additional required keys:

 * `extra_vars['is_rs']`: Set to True to initiate replica set configuration of MongoDB.
 * `extra_vars['is_rs_master']`: Set to True to initiate the server as a the master (primary) node.
 * `extra_vars['is_rs_slave']`: Set to True for all slaves (secondaries).
 * `extra_vars['rs_init']`: Set to True to initialize the cluster (must be after the cluster has been fully initiated).

MongoDB can also be deployed in a cluster setup over a Weave network. See [python_mongodb_cluster_in_vagrant](examples/python_mongodb_cluster_in_vagrant.py) for a detailed example of a setup.
