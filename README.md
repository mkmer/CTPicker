A tool to play various sounds based on i/o inputs, RTCM's, and connected nodes via the AMI interface
requires this API : https://pypi.org/project/asterisk-ami/

`pip install asterisk-ami`

We run this as a service created in systemd:
<ctpicker.service>

```[Unit]
Description="CTPicker task"
After=network.target

[Service]
ExecStart=/usr/local/bin/voter/CTPicker &
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```
