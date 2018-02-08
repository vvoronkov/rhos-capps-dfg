---
plugin_type: test
subparsers:
    rhos-capps-dfg:
        description: RHOS capps dfg tests
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: Setup
              options:
                  setup-heat:
                      type: Bool
                      default: no
                      help: Setup heat

            - title: Run tests
              options:
                  run-liberty:
                      type: Bool
                      default: no
                      help: Install the coverage
                  run-mitaka:
                      type: Bool
                      default: no
                      help: Install the coverage
