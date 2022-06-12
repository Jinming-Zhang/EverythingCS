[Reference](https://itsfoss.com/free-up-space-ubuntu-linux/)
## sudo apt-get autoremove
Removes libs and packages that were installed automatically to satisfy the dependencies of an installed package. If that package is removed, these automatically installed packages are useless in the system.

It also removes old Linux kernels that were installed from automatically in the system upgrade.

##  sudo apt-get autoclean / sudo apt-get clean 
Clean up APT cache in Ubuntu
use 

> sudo du -sh /var/cache/apt

to check the space used in the cache

