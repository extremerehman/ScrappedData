# How to Answer Product Manager Technical Interview Questions?

*Source: https://www.mypminterview.com/p/how-to-answer-pm-technical-interview-questions*

---

How to Answer Product Manager Technical Interview Questions?

Here is a step by step guide on How to Answer Product Manager Technical Interview Questions with Examples

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share







Interviewers like to ask Product Manager Technical Interview Questions as a way to evaluate your ability to:

Understand the mechanics of a technology product.Communicate technical information effectively.Think about the edge cases and trade-offs in technical design decisions.Think analytically and take a systematic approach to problem-solving.

Understand the mechanics of a technology product.

Communicate technical information effectively.

Think about the edge cases and trade-offs in technical design decisions.

Think analytically and take a systematic approach to problem-solving.





Technical questions have different shapes and forms but at a high level, they usually belong to one of these categories:

System design questions (e.g. Design a data model for account hierarchy, how does Gmail work?)Algorithm-based questions (e.g. Design an algorithm for newsfeed on Facebook)Technical problem-solving questions (e.g. We see a sudden drop in traffic. Figure out why)  

System design questions (e.g. Design a data model for account hierarchy, how does Gmail work?)

Algorithm-based questions (e.g. Design an algorithm for newsfeed on Facebook)

Technical problem-solving questions (e.g. We see a sudden drop in traffic. Figure out why)  



This article focuses on how to answer system design and algorithm-based questions. 



Here is a step by step guide/framework, you should follow while answering product manager technical interview questions:



1. Understand the Question.

2. Describe the Product.

3. Describe the Product Attributes

4. Select a Goal 

5. Prioritize the key Attributes 

6. Design the Product

7. Think about the Trade-Offs

8. Summarize your Answer





Now, let’s go through each of the above points with an example and understand them in detail,





There is usually valuable information in the question statement. Ask a  few questions that help you narrow down the scope of the question as much as possible. Your objective in this step is to reach an agreement with the interviewer on the high-level requirements of the product you are going to be designing or analyzing.

If there is a particular path you’d like to take (e.g. “I’m going to focus on the sending and receiving aspect of How Facebook works”)  because you feel comfortable with that path, persuade the interviewer in that direction by stating your assumptions rather than asking for clarification and instead, ask the interviewer if they are comfortable with your assumptions.

This is your chance to understand the requirements and constraints of the product. Think of yourself here as the technical lead that is working with the product manager to understand the requirements. 





Describe your understanding of the product from both a UI and technical perspective. This is your chance to showcase your appreciation for the user experience and ability to connect it back to the technical challenges with creating a user-friendly product.

One way to complete this section is to describe the technical mechanics of a user journey. Walk the interviewer through the user journey as you describe how each part of the user journey works and communicates with other parts in the background. 

For the Facebook example, you can describe how Newsfeed works and list the key user behaviors that could exist. You can explain that Newsfeed is the part of the product that users spend most of their time on to discover new content and that interaction varies from a few seconds to many minutes. 

Users sometimes find interesting content in the Newsfeed and interact with the content by liking, posting a comment,  sharing, viewing, clicking on the content, etc. And as a user scrolls down their feed, the algorithm on the server-side determines what content should be presented next. Perhaps the content is also a function of the user’s past or very recent interactions. 

Some users scroll down fast and others scroll down slowly. Scrolling down fast can potentially impact the user experience if it takes time to load new content. It's important for all users to have a consistently good experience on this page as it's part of the product that users engage with the most.





It will be a good idea here to describe the key attributes of the product that are relevant to the technical question that has been asked. Here are some sample attributes that might apply to a question:

Speed (e.g. time to complete a task)Success rate (e.g. accuracy, completion rate, etc) Budget (e.g. cost) Relevance

Speed (e.g. time to complete a task)

Success rate (e.g. accuracy, completion rate, etc) 

Budget (e.g. cost) 

Relevance



Selecting the right attributes is very important here. If you think you need some time to think about the relevant attributes of the product, ask for a moment to think about the attributes before giving an answer.

An important note to keep in mind here is that each product  (especially in the case of products offered by large tech companies) has many different attributes and edge cases and you might not have the time to cover all of them during the interview. It is recommended to acknowledge other attributes just so that you communicate to the interviewer that you do realize that there is more to the product than what you have highlighted but due to the limited time, you have decided to highlight the attributes that you think are more relevant to the question and the scope of the question.



For the Facebook example, you can highlight the following attributes: 

Time to load contentCost of Server to compute which content to present and cost of bandwidthRelevancy of the content Real-time update of the content (e.g. increase in the number of likes)There are more attributes you can highlight but the above encapsulates some of the key attributes of Newsfeed.

Time to load content

Cost of Server to compute which content to present and cost of bandwidth

Relevancy of the content 

Real-time update of the content (e.g. increase in the number of likes)

There are more attributes you can highlight but the above encapsulates some of the key attributes of Newsfeed.





You can think of this step as the step that describes what’s important in the design of the product from a user experience perspective. You can think of it as a user story that describes what’s important. The sentence you want to come up with it: “As a user of this product, I want to …., so that I can ….”.

The necessity of this step depends on the type of technical interview question being asked. If the question was about designing a system or an algorithm, then you must select a goal that helps you in deciding which attributes are important for you. In the case of Facebook example,  you can highlight that it’s important that the content gets loaded fast since users are usually on their phones and are used to quickly scrolling down and still seeing all the content (text, images, videos,  etc) right away without having to wait.  

The goal here is usually derived from the user experience and user goals. This is your chance to also show that you start with the user and are able to keep the user perspective in mind while thinking about the design of the product.





This is where you determine which of the attributes you’ve listed earlier are going to be the focus of your design.

For our Facebook example, you can say that the speed and high success rate of no delay in the loading of content is going to be the focus of your design given the goal you described earlier.  

Note that technical interview questions are usually very conversational. The interviewer might try to take you in various directions as you’re giving your answer. You should be comfortable with probing by the interviewer and having a conversation.  



Now that you have a good idea about the goal of the product and the attributes that matter to you, you can start thinking about designing the technical side of the product and its mechanics. Or if the question was a “how does it work” question type, you can start describing how you think the engineers have designed the product.

Your goal here is to describe the product based on the goal you selected and the attributes that you have prioritized. You will be using the attributes as a guide in your design decisions (e.g. In the  Facebook example, should the next content be loaded before the user scrolls down? Possibly yes since it will guarantee a smoother experience and no delay).   

It usually makes sense to use a whiteboard here to design the product and show how the system will work at a high level.



Remember that whatever technical decisions you make will include some trade-offs. There is always a trade-off between a better user experience and more resources required to deliver that better user experience. By highlighting the design trade-offs, you are acknowledging the concerns that the interviewer might have about your design decisions.  

For the Facebook page load example, you can explain that loading the next content can result in more bandwidth cost for Facebook which can be expensive but you can address this over time by optimizing the amount of content loaded based on each particular user’s speed of scrolling  (e.g. calculate how much content must be loaded for each user based on their speed of scrolling).



If there is time, provide a brief summary of the answer you’ve provided. Describe the important attributes of the product based on the goal you have selected, review the design at a high level, and describe the trade-offs.



Share

Important Links:

Product Improvement  - Complete list of all Questions and Answers

Guess Estimation - Complete list of all Questions with Answers

Behavioral - Complete list of all Questions and Answers

Product Metrics - Complete list of all Questions and Answers

Product Manager Interview Experiences at Top Companies - Question and Answers

How to Answer Product Launch Questions?

How to Answer Product Design Questions?

How would you price a Product?

Frameworks for Structured Product Thinking

100+ Product Manager Interview Questions 

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share