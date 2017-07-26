plugin_type: test
description: Heat test runner
subparsers:
    octario:
        help: Heat test runner
        description: Heat test runner
        include_groups: ['Ansible options', 'Inventory', 'Common options', 'Answers file']
required: yes