# How does TinyURL work?

*Source: https://www.mypminterview.com/p/technical-pminterview-how-does-tinyurl-work*

---

How does TinyURL work? - Google PM Interview

Google PM Interview: Technical PM Interview - How does TinyURL work?

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share





Clarifying Questions:

Q) Would you like me to describe the technical journey behind a user entering `tinyurl.com/hashkey` into their browser and ending up at `example.com/reallylongurlhere`A) Yes

Describe the Product:

To make sure you and the interviewer are on the same page, explain your understanding of the product:TinyURL is a URL shortening service where a user can enter a lengthy URL such as `example.com/reallylongurlhere` and get `tinyurl.com/hashkey` in return.

e.g. `google.com/photos/album/12312/ → tiny.url/123`

And when someone puts `tinyurl.com/hashkey` into their browser they would get redirected to `example.com/reallylongurlhere`.

e.g. `tiny.url/123 → google.com/photos/album/12312/`

Technical Answer:

User flow for generating TinyURL,

Users can generate a TinyURL on the website or via API.  The lengthy URLs is changed into a hash key by using a hashing algorithm.The hash-key prior generation would be checked for uniqueness.  This hashkey is stored as a lookup key that returns the long URL.  To speed retrieval, the hash key can be stored in an indexed manner.  The hash key is used as the main identifier in the url. e.g. Tinyurl.com/hashkey

Users can generate a TinyURL on the website or via API.  

The lengthy URLs is changed into a hash key by using a hashing algorithm.

The hash-key prior generation would be checked for uniqueness.  

This hashkey is stored as a lookup key that returns the long URL.  

To speed retrieval, the hash key can be stored in an indexed manner.  The hash key is used as the main identifier in the url. e.g. Tinyurl.com/hashkey

Flow after user enters the TinyURL into their browser,

The user enters tinyurl.com/hashkey into their browser.The browser sends that request to the user’s ISP where a domain server translates the text into an IP address. An IP address is a string of numbers that uniquely identifies where that web request should be routed.  In this case, the user is routed to TinyURL.com.Tinyurl must return the data very quickly so the request is sent into a load balancer that accounts for both the user’s geographic location and server load and routes the request to a close server with capacity.The hashkey is likely stored in a memory-based cache layer – or at least those URLs (hashkey) that have been used recently. This eliminates the need for a disk or origin lookup.If not in cache then the hash is looked up in the DB. The hashkey is associated with the full url and the user is redirected to the full url. After finding the corresponding long URL in their DB, TinyURL will issue a 302 redirect.

The user enters tinyurl.com/hashkey into their browser.

The browser sends that request to the user’s ISP where a domain server translates the text into an IP address. 

An IP address is a string of numbers that uniquely identifies where that web request should be routed.  

In this case, the user is routed to TinyURL.com.

Tinyurl must return the data very quickly so the request is sent into a load balancer that accounts for both the user’s geographic location and server load and routes the request to a close server with capacity.

The hashkey is likely stored in a memory-based cache layer – or at least those URLs (hashkey) that have been used recently. This eliminates the need for a disk or origin lookup.

If not in cache then the hash is looked up in the DB. The hashkey is associated with the full url and the user is redirected to the full url. 

After finding the corresponding long URL in their DB, TinyURL will issue a 302 redirect.

This direct redirect is important. If you were to use files or first load HTML and then redirect, the browser would add TinyUrl to the history, which is not what you want. Also, the site that is redirected to will see the referrer (the site that you originally come from) as being the site the TinyUrl link is on (i.e., twitter.com, your own site, wherever the link is). This is just as important, so that site owners can see where people are coming from. This too, would not work if a page gets loaded that redirects.

PS: there are more types of redirect. HTTP 301 means: redirect permanent. If that would happen, the browser will not request the bit.ly or TinyUrl site anymore and those sites want to count the hits. That's why HTTP 302 is used, which is a temporary redirect. The browser will ask TinyUrl.com or bit.ly each time again, which makes it possible to count the hits for you (some tiny url services offer this).

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share