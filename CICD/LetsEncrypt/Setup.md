# Set up LetsEncrypt With Nginx
1. Install dependencies.
```
$ apt-get update
$ sudo apt-get install certbot
$ apt-get install python3-certbot-nginx
```

2. Make sure to configure `nginx.conf` with **server** blocks that contain the **server_name** that certbot is certifying.

3. run command for each domain name that needs to be certified
```
$ sudo certbot --nginx -d example.com -d www.example.com
```