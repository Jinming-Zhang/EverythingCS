## chmod
three types of users:
u,g,o
three types of accesses:
r,w,x

Example:
>// add read permission to owner user
> chmod u+r

>// remove write permission to group user
>chmod g-w

>// remove execute permission to other user, add execute permission to owner and group users
>chmod o-x, ug+x 