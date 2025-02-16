kubectl create namespace synology-csi

kubectl create secret -n synology-csi generic client-info-secret --from-file=client-info.yml


