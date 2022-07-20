[Reference](https://nodesource.com/blog/running-your-node-js-app-with-systemd-part-1/)
Location:
`/lib/systemd/system`


1. Create a file with `.service` extension with following content.

note WorkingDirectory has to be absolute path, adjust accordingly when copy

```javascript

[Unit]

Description=NodeJS server, NextJS public frontend

After=network.target

  

[Service]

Type=simple

User=jenkins

Group=jenkins

Restart=on-failure

RestartSec=10

WorkingDirectory=/home/wolf/jenkins_home/jenkins/personal-react-dev

ExecStart=/usr/bin/npm run deploy

  

[Install]

WantedBy=multi-user.target

  

```

  

2. put the file into directory `/lib/systemd/system`