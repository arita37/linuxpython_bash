[Unit]
Description=Running django service when crash or restart
After=network.target

[Service]
TimeoutStopSec=4
Restart=always
User=handry
Group=handry

ExecStart=/usr/bin/django-run
ExecStop=/bin/kill -s TERM $MAINPID

[Install]
WantedBy=multi-user.target
Alias=djangorun.service