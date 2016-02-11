#!/bin/bash

for i in worker api nginx; do
  docker tag provisioning_$i onapp/prov-$i
  docker push onapp/prov-$i
done
