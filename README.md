#command line
  users add            Generate a user invitation token [Teleport DB users only]
  users update         Update user account
  users ls             Lists all user accounts.
  users rm             Deletes user accounts
  users reset          Reset user password and generate a new token [Teleport DB users only]
  nodes add            Generate a node invitation token
  nodes ls             List all active SSH nodes within the cluster
  tokens add           Create a invitation token
  tokens rm            Delete/revoke an invitation token
  tokens ls            List node and user invitation tokens
  auth export          Export public cluster (CA) keys to stdout
  auth sign            Create an identity file(s) for a given user
  auth rotate          Rotate certificate authorities in the cluster
  auth ls              List connected auth servers
  status               Report cluster status
  top                  Report diagnostic information
  requests ls          Show active access requests
  requests get         Show access request by ID
  requests approve     Approve pending access request
  requests deny        Deny pending access request
  requests create      Create pending access request
  requests rm          Delete an access request
  requests review      Review an access request
  apps ls              List all applications registered with the cluster.
  db ls                List all databases registered with the cluster.
  kube ls              List all Kubernetes clusters registered with the cluster.
  windows_desktops ls  List all desktops registered with the cluster.
  lock                 Create a new lock.
  bots ls              List all certificate renewal bots registered with the cluster.
  bots add             Add a new certificate renewal bot to the cluster.
  bots rm              Permanently remove a certificate renewal bot from the cluster.
  inventory status     Show inventory status summary
  inventory list       List teleport instance inventory
  inventory ping       Ping locally connected instance
  recordings ls        List recorded sessions.
  alerts list          List cluster alerts
  alerts create        Create cluster alerts
  alerts ack           Acknowledge cluster alerts
  alerts ack ls        List acknowledged cluster alerts
  proxy ls             Lists proxies connected to the cluster.
  create               Create or update a Teleport resource from a YAML file
  update               Update resource fields
  rm                   Delete a resource
  get                  Print a YAML declaration of various Teleport resources
  edit                 Edit a Teleport resource
  sso configure github Configure GitHub auth connector.
  sso test             Perform end-to-end test of SSO flow using provided auth connector definition.
  version              Print the version of your tctl binary