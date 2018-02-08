# rhos-capps-dfg

# Usage with InfraRed

## Installation

1. Install infrared (https://github.com/redhat-openstack/infrared)

2. Install this plugin:

       infrared plugin add https://github.com/rrasouli/rhos-capps-dfg.git

## Usage

Setup heat:
    
    infrared rhos-capps-dfg --setup-heat yes


Run old versions liberty:

    infrared rhos-capps-dfg --run-liberty yes


Run old versions mitaka:

    infrared rhos-capps-dfg --run-mitaka yes
