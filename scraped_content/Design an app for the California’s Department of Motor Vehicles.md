# Design an app for the California’s Department of Motor Vehicles

*Source: https://www.mypminterview.com/p/google-product-design-app-california-dmv*

---

Design an app for the California’s Department of Motor Vehicles | Google PM Interview

Product Design - Google Product Manager Interview Question: How would you design an app for the California’s Department of Motor Vehicles.

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share



Let’s get started with the solution (remember to follow the framework),



I will start by asking clarifying questions to ensure I have a solid understanding as it relates to the problem statement and design goals.

Second, I will brainstorm a list of user groups and pick one to focus on, ID their user needs, then prioritize them 

Lastly, I will brainstorm solutions to address the design goal and the needs of the user group I am designing the product for, ID metrics to track success, and summarize the solution.



I would first ask the interviewer if they have a particular goal in mind in the design of the app or if I can choose mine. There are a few goals that I can think of:

Reduce the number of calls made to DMV support line.Reduce the number of visits made to DMV office.Reduce the average time spent per visit by citizens at the DMV.

Reduce the number of calls made to DMV support line.

Reduce the number of visits made to DMV office.

Reduce the average time spent per visit by citizens at the DMV.

For the purpose of this interview, I’d ask the interviewer if it’s ok for me to focus on reducing the average time spent per visit at the DMV. 

Let’s assume they agree with my goal.





There are a few different persona’s that could benefit from a DMV app:

DMV employee.Government officer seeking information.Citizen seeking service from the DMV

DMV employee.

Government officer seeking information.

Citizen seeking service from the DMV

I’m going to ask the interviewer if it’s ok to focus on building an app for the citizen who would be using the DMV app. Let’s assume they agree.





Next, I want to think about the use cases of a citizen who’s seeking service from the DMV:

Visiting the DMV help desk to explain the reason for their visit and ask to see a DMV officer. They usually get a number at this point.Wait for their number to be called.Visit an officer and provide documents to identify themselves.Explain the reason for the visit and provide documents needed for the request (e.g. renewing your driver’s license, registering a car, taking a driver’s license test, et).Pay for service with their credit card.Wait for a few days/weeks to receive new documents/letters from DMV.

Visiting the DMV help desk to explain the reason for their visit and ask to see a DMV officer. They usually get a number at this point.

Wait for their number to be called.

Visit an officer and provide documents to identify themselves.

Explain the reason for the visit and provide documents needed for the request (e.g. renewing your driver’s license, registering a car, taking a driver’s license test, et).

Pay for service with their credit card.

Wait for a few days/weeks to receive new documents/letters from DMV.

There are other use cases. Here, I’ve highlighted some of the most important and time-consuming ones. 



Here are a few ideas to reduce time spent per visit:

Book your visit in advance and present wait times at different hoursProvide real-time information on where you are in the queue to visit a DMV officer.Enable users to select a reason for a visit from the app. Provide a list of required documents and ask the user to confirm that they will bring all the requested documents to the DMV.Enable users to upload required documents in advance.Accept payment via phone in advance.Provide status updates on the request. Help user see if the card / license / registration document has been created / mailed / delivered.

Book your visit in advance and present wait times at different hours

Provide real-time information on where you are in the queue to visit a DMV officer.

Enable users to select a reason for a visit from the app. Provide a list of required documents and ask the user to confirm that they will bring all the requested documents to the DMV.

Enable users to upload required documents in advance.

Accept payment via phone in advance.

Provide status updates on the request. Help user see if the card / license / registration document has been created / mailed / delivered.



I would now want to evaluate these ideas against each other based on impact on DMV, impact on the end-user, and cost of implementation.

Medium impact on the DMV. This can help DMV encourage users to book appointments at slower times of the day. High impact on the user since it reduces their wait time and gets rid of the first step (getting a #). Implementation cost is medium as you will need to develop a process that connects inside office and mobile data to each other.Low impact on the DMV. Medium impact on the user as they can use the wait time to get something done (e.g. shopping) while waiting and still be back before it’s their turn. Low cost since the app just needs to connect to the queue data.Medium impact on the DMV since many people do their own research to ensure they do have the required documents. High impact on the user as it makes it easier for them to understand what’s needed. Low cost of implementation.Low impact for the DMV since they might have concerns around fraud. Medium impact on the consumer since they now have to take out their phones and take pictures. High cost of implementation since the development of such service requires some special capabilities (e.g. eliminating blurry images, fraud detection, etc)High impact for the DMV as it helps them reduce the number of payment terminals needed at the DMV offices. It also helps them speed up the service. High impact for the consumer as they don’t have to take their wallet and pay in the office. Medium implementation cost to connect payment on the app to DMV’s financial systemLow impact for the DMV. Medium impact for the user (not critical information). Medium cost of implementation since DMV has to connect to its backend to get access to the status of a request.

Medium impact on the DMV. This can help DMV encourage users to book appointments at slower times of the day. High impact on the user since it reduces their wait time and gets rid of the first step (getting a #). Implementation cost is medium as you will need to develop a process that connects inside office and mobile data to each other.

Low impact on the DMV. Medium impact on the user as they can use the wait time to get something done (e.g. shopping) while waiting and still be back before it’s their turn. Low cost since the app just needs to connect to the queue data.

Medium impact on the DMV since many people do their own research to ensure they do have the required documents. High impact on the user as it makes it easier for them to understand what’s needed. Low cost of implementation.

Low impact for the DMV since they might have concerns around fraud. Medium impact on the consumer since they now have to take out their phones and take pictures. High cost of implementation since the development of such service requires some special capabilities (e.g. eliminating blurry images, fraud detection, etc)

High impact for the DMV as it helps them reduce the number of payment terminals needed at the DMV offices. It also helps them speed up the service. High impact for the consumer as they don’t have to take their wallet and pay in the office. Medium implementation cost to connect payment on the app to DMV’s financial system

Low impact for the DMV. Medium impact for the user (not critical information). Medium cost of implementation since DMV has to connect to its backend to get access to the status of a request.

Based on what’s discussed above, I suggest that we first prioritize building features 1, 3, and 5 as the initial features of the app. User can book their visit in advance and pick a time that suits them the most while knowing the traffic at the DMV office at different times of the day. Feature 3 helps them ensure that they do possess all the information they need to complete the job they are visiting the DMV office for. It also helps DMV officers know immediately the reason for the visit And feature 5 ensures no time is wasted for payment in the DMV office.

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share