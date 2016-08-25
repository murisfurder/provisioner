---
layout: page
title: File and folder structure
permalink: /docs/file-and-folder-structure
tags: docs
redirect_from:
  - /docs/file_and_folder_structure
---

A role in Provisioner is simply an Ansible playbook, along with some documentation.

Most modules would have a structure similar to this:

```
├── doc
│   └── roles
│       └── foobar.md
└── provision_profiles
    ├── roles
    │   ├── foobar
    │   │   ├── files
    │   │   │   └── some-file.sh
    │   │   └── tasks
    │   │       └── main.yml
    ├── foobar.yml
    └── foobar_install_notes.tpl
```

The file/folders inside `role`, as well as `foobar.yml`  should be self explanatory for anyone familiar with Ansible.

Beyond these files, we have two Provisioner specific files:

 * `doc/roles/foobar.md`: This file includes generic instruction and a description of the role.
 * `provision_proviles/foobar_install_notes.tpl`: This is the post-installation notes that will be parsed and returned by the API. These is a template that can include parameters, such as credentials. This file must be named the same as the role, but with `_install_notes.tpl` appended to it.
