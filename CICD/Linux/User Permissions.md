# User
creater of the file/directory

Each user has it's own group.

After adding a user to a group, the user needs to re-login for the change to take effect.


# To Allow a user run a sudo command without password
1. create a file of user name inside directory `/etc/sudoers.d/<filename>`, i.e:
	```
	touch /etc/sudoers.d/wolf
	```
2. add in the file content each command needed to run as sudo for that user
	```
	%wolf ALL= NOPASSWD: /bin/systemctl start my_app
	%wolf ALL= NOPASSWD: /bin/systemctl stop my_app
	%wolf ALL= NOPASSWD: /bin/systemctl restart my_app
	```