### Mount new volume
[aws reference](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html)
1.  Create and Attack Volume
2. ssh to console
3. use **lsblk** to find newly attached volume, usually will be /dev/xvd[*]
	>sudo lsblk
4. create filesystem on the new volume
>sudo mkfs -t ext4 /dev/xvd[*]
5. make new directiory and mount to the new volume
>sudo mkdir /ext-1
>sudo mount /dev/xvd[*] /ext-1

### Automatically mount attached volume after reboot
1. Find the volume uuid
>sudo blkid
2. back up current /etc/fstab file
> sudo cp /etc/fstab /etc/fstab.orig
3. add new config of the uuid to /etc/fstab file
>UUID=aebf131c-6957-451e-8d34-ec978d9581ae /ext-1 ext4 defaults,nofail 0 2
4. Verify everything works
>sudo umountj /ext-1
>sudo mount -a
