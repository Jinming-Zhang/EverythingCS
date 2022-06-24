# Install Softwares
- jenkins
- nginx
- git
- nodejs
- python

# Setup Nginx
- Copy [[linux-webserver-config/nginx_config/Index|template]] nginx.conf file to `/etc/nginx/nginx.conf`
- Add and start nginx to service
	```
	$ sudo systemctl enable nginx
	$ sudo systemctl start nginx
	```
	
#  Create Service for Webserver
- Create a [[ServiceFileTemplate|service file]] inside `/lib/systemd/system`, i.e. 
	Note the user in the template should be `jenkins` if the service will be started by jenkins.
	```
	sudo vim /lib/systemd/system/wolfy.service
	```
- Reload and start system services when project is ready:
	```
	sudo systemctl daemon-reload
	sudo systemctl enable wolfy.service
	sudo systemctl start wolfy.service
	```
# Set up Jenkins
> Jenkins Admin password default location:
> ```
>$JENKINS_HOME/secrets/initialAdminPassword
> ```
> i.e.
> `/var/lib/jenkins/secrets/initialAdminPassword`

## Change Jenkins Home Directory

- stop jenkins service
- make a new directory and change its owner
	```
	mkdir ~/jenkins_home
	chown jenkins:jenkins ~/jenkins_home
	```
- copy existing jenkins file to new home directory
	```
	cp -prv /var/lib/jenkins ~/jenkins_home
	```
- change the `jenkins` user home to new home directory
	```
	usermod -d ~/jenkins_home jenkins
	```
- update $JENKINS_HOME variable in jenkins config file to the new home directory
	```
	vim /etc/default/jenkins
	```
- start jenkins service
## Allow Jenkins to Run sudo Commands
![[User Permissions#To Allow a user run a sudo command without password]]