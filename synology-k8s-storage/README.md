Clone the git repository. git clone https://github.com/SynologyOpenSource/synology-csi.git

Enter the directory. cd synology-csi

Copy the client-info-template.yml file. cp config/client-info-template.yml config/client-info.yml

Edit config/client-info.yml to configure the connection information for DSM. You can specify one or more storage systems on which the CSI volumes will be created. Change the following parameters as needed:

host: The IPv4 address of your DSM.
port: The port for connecting to DSM. The default HTTP port is 5000 and 5001 for HTTPS. Only change this if you use a different port.
https: Set "true" to use HTTPS for secure connections. Make sure the port is properly configured as well.
username, password: The credentials for connecting to DSM.
Install

YAML Run ./scripts/deploy.sh run to install the driver. This will be a full deployment, which means you'll be building and running all CSI services as well as the snapshotter. If you want a basic deployment, which doesn't include installing a snapshotter, change the command as instructed below.

full: ./scripts/deploy.sh run


kubectl create namespace synology-csi

kubectl create secret -n synology-csi generic client-info-secret --from-file=client-info.yml


