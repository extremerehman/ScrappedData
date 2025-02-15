# What happens when you type a URL in the browser?

*Source: https://www.mypminterview.com/p/technical-pm-type-url-in-browser*

---

Technical - What happens when you type a URL in the browser?

Technical Product Management Interview Question - What happens when you type a URL in the browser?

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share





This question tests your technical understanding of networks. We recommend reviewing this list in detail, but also recognize that your interviewer may be looking for a simpler, briefer explanation. 

In this answer, we'll walk through the exact steps that happen when a URL is typed into a browser.



1. Typing in the URL



URLs stand for "Uniform Resource Locator" which contains a domain name. In this example, let's assume we're searching for "www.mypminterview.com"

The first step, before all of this happens, is that the browser will check its cache to determine if the URL is considered "fresh" and in the cache. For the sake of speed, browsers will often store DNS records to find the associated IP address. If the cache entry doesn't exist (you're visiting a URL you have never visited before) or it has expired (the browser determines it needs to re-check the IP address with the DNS), then the browser needs to find the DNS record. In this answer, let's assume the DNS record is not cached.



DNS stands for "Domain Name Service" and contains a list of mappings from the domain name to the IP address of the server. DNS records are distributed across several servers, which helps in the case that a particular DNS service goes down.

2. DNS Query



Now, we need to get the correct IP Address for the given domain name using the DNS. First, your browser will check the hosts file on your computer, which is a locally stored file in the computer's operating system that maps domain names to IP addresses. Without an entry in the hosts file, the browser then checks the router's cache to see if the DNS record exists there.

Usually, the DNS Server will have the right information and you'll end up getting back the correct IP address. However, if there is still not a resolution of the DNS query, then the browser needs to use the ISP (Internet service provider) to check for the IP address in its cache.

When all else fails, the browser then must query the TLD (Top-level domain) nameservers via the root server.



You know them from the extensions at the end of URLs (e.g. ".com", ".org", ".gov"). Each TLD has its own nameservers that can redirect to the appropriate servers with information about the DNS records.

Now, the TLD nameservers redirect the request to the IP address of the "second-level" domain server and pull the correct IP address

You can think about these systems analyzing the URL from the end to the beginning, where first, we start at the TLD (".com" in this case) and then move back to the "mypminterview" domain name, where the "root" server can help direct to TLD servers, and TLD servers redirect to second-level domain servers.

If needed, the server would also redirect to a third-level domain server (e.g. "blog" in "blog.mypminterview.com").

Great! We've now looked up the IP address for the given URL. Along the way, these services will cache the entry appropriately to ensure we don't have to go through the entire process each time.

3. HTTP Request



Now that our browser knows the correct IP address, it needs to connect to that server. Browsers most often use TCP connections for an HTTP request.



TCP stands for "Transmission Control Protocol" and is a protocol for allowing two hosts to establish connections and exchange data streams. The protocol includes behavior like a "three-way handshake" which are certain bytes sent over to indicate specific connections. Think of it as a language protocol for how to initiate a conversation and carry on a conversation.



In the case of an HTTPS connection, things are a bit more complex, but we'll stick to HTTP requests for this explanation. 



HTTP stands for HyperText Transfer Protocol and is another protocol for determining the formatting and style of messages being sent back and forth over TCP. Most commonly, there are GET and POST requests for getting and sending information, respectively.

The browser will now initiate an HTTP request to MyPMInterview's server. The browser sends a GET request, along with additional information like the user-agent details (e.g. Chrome Mac OSX) to ask MyPMInterview's server to send back the website page.

4. HTTP Response



On MyPMInterview's server, it now has received a GET request, asking for information. The server will compute factors on its end to understand what to send back to the client's computer (e.g. perhaps on Chrome browsers, MyPMInterview should display a different text than on Firefox browsers).

HTTP Responses always contain an HTTP header, with a status message. The most common (and ideal) response to receive is a 200 response, which means the page was sent back correctly. However, another common response is the 404 response, which means the page wasn't found. This could happen, for instance, if someone typed in "mypminterview.com/blah" and MyPMInterview's server didn't know what to return, since there isn't a page there.

5. Rendering

Now, it's up to the browser to render the content it received from MyPMInterview's server. There may need to be multiple back and forth GET and POST requests to pull all the information, such as CSS styling. After the browser has all the information, it fully renders the page, and now you can see MyPMInterview's website!



Share this post with a friendSince you liked this post, why not share it to help spread the word?Share