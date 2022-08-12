[ref](http://nginx.org/en/docs/http/request_processing.html)
# Server Block
A virtual server block config, a nginx.conf file can contain multiple virtual server blocks.
`server_name` directive will be used to match the **Host** header field to determine which virtual server the request will be routed to.
```nginx
server{
listen 80;
server_name domain.com www.domain.com ~^www.examples\d+.com;
root /
}
```

- wild card `*` can be used at either start or end of a server name.
- regex can be used by starting a server name with `~`
### Server name selection order
1.  exact name
2.  longest wildcard name starting with an asterisk, e.g. “`*.example.org`”
3.  longest wildcard name ending with an asterisk, e.g. “`mail.*`”
4.  first matching regular expression (in order of appearance in a configuration file)