Install tool `apache2-utils`
```
sudo apt-install apache2-utils
```

Generate user password file

``` bash
# remember sudo
sudo htpasswd -c /etc/nginx/.htpasswd <username>
```

Add `basic_auth` directive in desired nginx block :
```ngnix
events{
	worker_connections 4096;
}
http{
	server {

		listen 80;

		location / {
			proxy_pass http://localhost:3000/;
		}
	}

	server {

		listen 6969;

		location / {
			auth_basic "Who the Hell Are You?!";
			auth_basic_user_file /etc/nginx/.htpasswd;
			
			proxy_set_header   Authorization "";
			proxy_pass http://localhost:8080/;
		}
	}
}
```
