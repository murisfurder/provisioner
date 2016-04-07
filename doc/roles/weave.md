# Weave

* *Name*: weave
* *Requirement*: Ubuntu 12.04 or later

Installs the [Weave Net](https://www.weave.works/products/weave-net/) with encrypted communication.

Additional required keys:

 * `extra_vars['is_master']`: Set to True to initiate the server as the master node.
 * `extra_vars['is_slave']`: Set to True to initiate the server as a slave nodes.
 * `extra_vars['passphrase']`: Must be the same on master and slave nodes.
 * `extra_vars['master_ip']`: Required if is_slave. Specify the public IP of the master node.

For a complete example, check out [example/python_weave_in_vagrant.py](https://github.com/OnApp/provisioner/blob/master/example/python_weave_in_vagrant.py).
