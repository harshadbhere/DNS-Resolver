# DNS-Resolver

A DNS resolver written using Python based on John Crickett's [coding challenge](https://codingchallenges.fyi/challenges/challenge-dns-resolver/).

For example, to find the IP address of [geeksforgeeks.org](geeksforgeeks.org):
```
Querying 192.203.230.10 for geeksforgeeks.org
Querying 199.19.56.1 for geeksforgeeks.org
Querying 199.249.112.1 for geeksforgeeks.org
Querying 199.19.54.1 for geeksforgeeks.org
Querying 199.249.120.1 for geeksforgeeks.org
Querying 199.19.53.1 for geeksforgeeks.org
Querying 199.19.57.1 for geeksforgeeks.org
Querying 205.251.197.240 for geeksforgeeks.org
34.218.62.116
```
We get the IP address as: 34.218.62.116

Now, let's cross check with Windows nsloopup command:
```
nslookup geeksforgeeks.org
Name:    geeksforgeeks.org
Address:  34.218.62.116
```
We get the same IP address!

To know more about, DNS requests, responses, etc, check this website [RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035#section-4.1.1)
