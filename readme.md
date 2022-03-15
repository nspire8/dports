# DPorts

Find all docker ports in use on your host and provide a simple web ui to view. Used to find what
ports are available when you spin up new containers.

### Usage
- Edit `ports-cron.sh` to point at `{PUT DPORTS REPO PATH HERE}/ports.txt`
- Drop something like this into your crontab:
```
*/5 * * * * /bin/bash {PUT DPORTS REPO PATH HERE}/ports-cron.sh
```
- `docker-compose up -d` gogo

