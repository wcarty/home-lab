curl --cacert /etc/ssl/certs/ca.crt  https://nginx-ssl-service.default.svc.cluster.local -v

curl https://nginx-ssl-service.default.svc.cluster.local -k  -v
