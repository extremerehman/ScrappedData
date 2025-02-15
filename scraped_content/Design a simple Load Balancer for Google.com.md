# Design a simple Load Balancer for Google.com

*Source: https://www.mypminterview.com/p/design-load-balancer-for-google-com*

---

Design a simple Load Balancer for Google.com

Product Management Technical Question - Design a simple Load Balancer for Google.com. What data structures would you use?

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share





A load balancer is a technical component that sits between a user's browser and the front end servers of a service, such as Google. 

Its main purpose is to,

Distribute traffic evenly among the next stage servers, in order to avoid uneven resource utilization.Dynamically respond to changes in server availability. 

Distribute traffic evenly among the next stage servers, in order to avoid uneven resource utilization.

Dynamically respond to changes in server availability. 



To achieve this, a load balancer can implement different load balancing strategies, such as, 

Round RobinLeast Traffic FirstLeast Utilization First.

Round Robin

Least Traffic First

Least Utilization First.



Round Robin is a load balancing strategy that involves maintaining,

A list of available servers.Index for the next server. 

A list of available servers.

Index for the next server. 

Every time a new request is received, it is allocated to the server pointed to by the index, and the index is then moved to the next server in the list. If a server becomes unavailable, it is removed from the list of available servers. Round robin kind uses a linked-list.



Least Traffic First is a load balancing strategy that involves,

Maintaining a list of available servers, along with their corresponding network bandwidth usage percentages.These percentages are reported to the load balancer by the servers through a regular handshake. 

Maintaining a list of available servers, along with their corresponding network bandwidth usage percentages.

These percentages are reported to the load balancer by the servers through a regular handshake. 

When a new request is received, it is allocated to the server with the lowest bandwidth usage percentage.



Least Utilization First is similar to Least Traffic First, except that the percentage of network bandwidth usage is replaced by the percentage of memory or CPU usage.

There are several reasons why a load balancer is necessary. 

Firstly, it ensures high availability of the service by distributing traffic evenly among servers and responding dynamically to changes in server availability. Secondly, it ensures that the nodes are not overstressed by distributing the load evenly among them. Finally, a healthy system is maintained by ensuring that resources are used efficiently and effectively.

Firstly, it ensures high availability of the service by distributing traffic evenly among servers and responding dynamically to changes in server availability. 

Secondly, it ensures that the nodes are not overstressed by distributing the load evenly among them. 

Finally, a healthy system is maintained by ensuring that resources are used efficiently and effectively.

A simple load balancer strategy would be a combination of Round Robin and Least Connection Used. The Least Connection strategy involves checking which server is free based on the number of active connections it is serving. This information is reported to the server through a health check or notification mechanism, such as regular pings or a pull model to check the number of active connections.

In the Least Connection load balancing strategy, a data structure such as a hashmap can be used to store the server ID and the number of connections for each server. This information can then be used to determine which server is free based on the number of active connections it is serving.

The heap sort data structure can also be used in this strategy. A max heap can be used to store the server with the least number of connections, while a min heap can be used to store the server with the most number of connections. By using a heap sort data structure, the servers can be stored in a sorted order, making it easier to identify the server that can handle a new request.

Overall, the use of these data structures helps the load balancer to effectively manage the distribution of traffic among the servers and ensure that resources are used efficiently.

In reality, there is a combination of strategy, ideally by load balancer (to distribute traffic across network) and CDN to distribute content based on geography for faster response time solves the availability problem. 

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share