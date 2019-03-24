# EmailAPI

Tested on: Fedora 26 and CentOS 7.
Working on port 5000 as default

## requirements

 * Python >= 2.7.10

## GNU/Linux (systemd) installation
```
cd /opt
git clone https://github.com/d0nth4x/py-email-api.git
cd py-email-api
python setup.py install


mv emailapi.service.example /etc/systemd/system/emailapi.service
systemctl enable emailapi
systemctl start emailapi
```

### Tips
* change owner to non-root
* use only one interface in main.py instead '0.0.0.0'
