# Decline in Flipkart's Cart Additions

*Source: https://www.mypminterview.com/p/decline-in-flipkart-cart-additions*

---

Decline in Flipkart's Cart Additions | Product Execution

You are a PM at Flipkart and you observed that there is a 10% decline in Flipkart's cart additions in the last 7 days. How would you find the root cause of the issue?

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share







Problem Statement - 

You are a PM at Flipkart and you observed that there is a 10% decline in Flipkart's cart additions in the last 7 days. How would you find the root cause of the issue?





Interview Tip: Ask Clarifying Questions to understand the scope of the problem.



Before jumping onto the finding the problem, I have some clarifying questions,





Q) What do we define as cart additions?

A) User clicks on Add to Cart button and an item is added to their shopping cart.



Q) Is this a generic decline or are we noticing this in the App or Web?

A) We are noticing this issue on the mobile App. - Android only.



Q) Is it on Android or IOS or both?

A) Android only.



Q) Have we checked whether the analytics tool we are using is working correctly in the last 7 days? Any change in the way we capture data? 

A) Yes, the data is correct no issues with that.







Now, that I have all of that answered, I will share the outline of the framework that I will follow to arrive at the root cause,  





I will first look at the,



External Factors (Competitor, New Product Launch, etc.), followed byDemographics features ( Impact on any particular demographics customer segment).Next, I would look at the Internal Factors (Tech Release, Design Change or any other Business Decisions, etc.).Next, I will go through the User Journey on the mobile app. (Step by Step journey on the App).

External Factors (Competitor, New Product Launch, etc.), followed by

Demographics features ( Impact on any particular demographics customer segment).

Next, I would look at the Internal Factors (Tech Release, Design Change or any other Business Decisions, etc.).

Next, I will go through the User Journey on the mobile app. (Step by Step journey on the App).





External Factors - 

Q) Has there been any new product launches or new marketing announcements by our competitors?

A) No new public announcement that we are aware of.

Q) Any negative PR that we are aware of?

A) No.



Q) Any News or Seasonality impact which might impact the overall purchasing behavior?

A) No we didn’t notice any such behavior.



Demographics Factors - 

Q) Has it affected any particular demographic customer segment? (Gender / Age / Location)like is the Decline is from a certain city/region or in a certain gender segment, who were purchasing before but has stopped now?A) No, we didn’t find any such demographic changes. The decline is uniform across different locations, gender, and age groups. It’s a uniform distribution.



Internal Factors - 



Q) Any new campaigns or product launches or subsidiaries that might have taken users’ attention away from the mobile app? 

A) We launch campaigns all the time and it’s not clear if any such campaigns would take users’ attention away from the mobile app.



Q) Any particular kind of products or product categories that has seen a decline in cart additions? 

A) No, it’s uniform across product categories.



Q) Any recent App updates? 

A) Yes we have done a major update recently.



Q) Is that change related to cart addition flow? 

A) Yes, we have made changes to the whole shopping cart flow.



Q) Any Design changes to increase discoverability of products or an easier checkout journey or have we changed the look and feel of the Add to Cart button?

A) We have improved the checkout flow to make it more seemless and improve the conversion rate.



Q) Any incidents and bugs report from customers on the recent rollout changes?

A) There are not many bug reports since it’s only 7 days. But we have seen an increase in reports related to payment and checkout. 



User Journey in the mobile App -

 

Next, we will go through the user journey and see if there is any glitch/bugs in the journey till cart addition - 

From, searching a product -> viewing the product -> clicking on Add to Cart -> the product showing up on the Shopping cart.



We checked the flow and found that there is no issue in the App installs, Signups, and no issue with product discoverability. 



Next, I feel we should analyze the Add to Cart button.

In the android app, We should check how many customers are clicking on add to cart and how many products are not getting added to the cart.



Q) Do we have events data that confirms this flow is getting completed?

A) We are seeing a huge drop in cart additions for the latest android app version.



Hence, the problem is with the Add to Cart button in the latest android app version that was released.

Here are some Problem-Solving Interview Questions and Answers for you to practice-

Problem Solving: Uber Product Manager Interview - Increase in Cancel RatesProblem Solving - Decline in Facebook Groups UsageCommon Mistakes to avoid while Answering Product Manager Problem-Solving Questions

Problem Solving: Uber Product Manager Interview - Increase in Cancel Rates

Problem Solving - Decline in Facebook Groups Usage

Common Mistakes to avoid while Answering Product Manager Problem-Solving Questions

Share



Share this post with a friendSince you liked this post, why not share it to help spread the word?Share