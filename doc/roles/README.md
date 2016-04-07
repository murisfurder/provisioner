# Roles

For all roles, the 'role', 'ip', 'username' and 'password' keys are required.

## Ping

* *Name*: ping
* *Requirement*: None

The `ping` profile simply pings the server using Ansible's built-in ping module. Despite the name, this doesn't actually ping (i.e. send an ICMP package), but rather connects to the server over SSH.

## SSH keys

* *Name*: ssh-keys
* *Requirement*: Should work on any Linux/UNIX style operating system.

Installs one or more SSH keys.

Additional required keys:

 * `extra_vars['ssh-user']`: The user where to which we want to install the SSH key (defaults to username)
 * `extra_vars['ssh-keys']`: A list of one or more SSH keys to install
