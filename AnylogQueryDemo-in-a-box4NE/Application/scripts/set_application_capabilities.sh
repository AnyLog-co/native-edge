#!/bin/bash

set -e
ctx instance runtime-properties capabilities "@{}"
FACT_PATH="$(ctx node properties ansible_env_vars.ANSIBLE_FACT_PATH)"

ctx instance runtime-properties application_details "$(cat $FACT_PATH/anylog_endpoint.fact | tr -d '\"')"
