# Drop in App Open Rate of Instagram

*Source: https://www.mypminterview.com/p/drop-in-app-open-rate-of-instagram-prodexecution*

---

#### Share this post

# Drop in App Open Rate of Instagram - Product Execution

### You are the product manager for Instagram App. You see there is a 15% drop in the App Open Rate. Find the Root Cause and Tell us what could have happened.

#### Share this post

### Problem Statement:

You are the Product Manager for Instagram App. You see there is a 15% drop in the App Open Rate. Do a Root Cause Analysis and Tell us what could have happened  in order to devise appropriate solutions.

### How are you being evaluated?

During this product execution interview question, the interviewer is assessing your ability to approach problems in an organized and logical manner. The situation presented involves conflicting data that suggests a problem, and you are tasked with identifying the root causes and providing potential solutions. Your evaluation will focus on the following aspects:

1. Your thought process while diagnosing and solving a business problem: They are interested in how you approach complex situations, analyze data, and derive insights to address the issue at hand.
2. Your ability to apply logical reasoning in identifying potential causes: The interviewer wants to see if you can logically connect the available information and consider various factors that may contribute to the problem.
3. Your ability to be exhaustive and thorough in listing possible causes: They want to assess if you can consider multiple angles and potential factors that might be influencing the observed outcomes.
4. Your ability to clearly and concisely communication while delivering your analysis and recommendations: The interviewer wants to evaluate your ability to express your thoughts coherently, avoiding rambling or unnecessary tangents.

Your thought process while diagnosing and solving a business problem: They are interested in how you approach complex situations, analyze data, and derive insights to address the issue at hand.

Your ability to apply logical reasoning in identifying potential causes: The interviewer wants to see if you can logically connect the available information and consider various factors that may contribute to the problem.

Your ability to be exhaustive and thorough in listing possible causes: They want to assess if you can consider multiple angles and potential factors that might be influencing the observed outcomes.

Your ability to clearly and concisely communication while delivering your analysis and recommendations: The interviewer wants to evaluate your ability to express your thoughts coherently, avoiding rambling or unnecessary tangents.



## How to Answer Product Execution Questions? - Product Execution





First, take a minute to think and write down the structure and approach of the answer. Next,

### Describe the feature or product:

Instagram is a photo and video-sharing social networking service that enables users to capture, edit, and share moments from their lives through visually captivating content. Whether it's a stunning landscape, a mouth-watering meal, or a joyful gathering, Instagram provides a platform for users to express themselves artistically and engage with others through images and videos.

Instagram's mission is to "bring you closer to the people and things you love." The platform aims to create a space where people can connect, share, and discover meaningful content with their friends, family, and communities. Instagram's mission centres around fostering connections, inspiring creativity, and providing a platform for individuals to express themselves, discover new ideas, and build relationships through visual storytelling. By enabling users to capture and share moments from their lives, Instagram strives to enhance the sense of belonging, creativity, and inspiration in the online social landscape.

Instagram can be accessed from a desktop web, mobile web, and mobile app (Android, IOS).

Some of the major competitors of Instagram are TikTok, Snapchat, Facebook (including Facebook Stories and Facebook Live), YouTube, Pinterest, Twitter, LinkedIn, etc.

### Ask Clarifying Questions:

1. Q) What do we mean by App open rate ? do we mean users not even opening once a day (decrease in active users) OR  users not opening multiple times a day (decrease in repeat opens)?A) Users not opening app even once a day i.e decrease in Active Users, DAU & Rentention.
2. Q) Since it’s a major drop of 15%, (considering the scale at which we are operating) is it a steep drop or a gradual drop over a period of days?A) Yes it is happening for a period of last 7 days.
3. Q) Is the drop Device (mobile or desktop) and OS (Android, IOS) specific?A) Yes, the drop is majorly from Mobile devices however, it’s not OS specific.
4. Q) Did the decrease in the  number of App open happen from any specific touchpoint like notifications, organic, ads, links?A) No, general drop across.
5. Q) Have there been any changes in user behavior, such as a decrease in the number of photos/videos uploaded per day? A) Yes, due decrease in app open rate the rate of content uploads is also decreasing simultaneously.
6. Q) Have we changed anything with the logs recently about how we log things or capture data? Is it possible that there is a logging error here?A) No, there haven't been any recent changes in logging practices or data capture methods.

Q) What do we mean by App open rate ? do we mean users not even opening once a day (decrease in active users) OR  users not opening multiple times a day (decrease in repeat opens)?A) Users not opening app even once a day i.e decrease in Active Users, DAU & Rentention.

Q) Since it’s a major drop of 15%, (considering the scale at which we are operating) is it a steep drop or a gradual drop over a period of days?A) Yes it is happening for a period of last 7 days.

Q) Is the drop Device (mobile or desktop) and OS (Android, IOS) specific?A) Yes, the drop is majorly from Mobile devices however, it’s not OS specific.

Q) Did the decrease in the  number of App open happen from any specific touchpoint like notifications, organic, ads, links?A) No, general drop across.

Q) Have there been any changes in user behavior, such as a decrease in the number of photos/videos uploaded per day?

A) Yes, due decrease in app open rate the rate of content uploads is also decreasing simultaneously.

Q) Have we changed anything with the logs recently about how we log things or capture data? Is it possible that there is a logging error here?A) No, there haven't been any recent changes in logging practices or data capture methods.

Now, that I have all the clarifying questions answered, I will share the outline of the framework that I will follow to arrive at the root cause,

I will first look at the,

1. External Factors (Competitor, New Product Launch, etc.), followed by
2. Demographics features ( Impact on any particular demographics customer segment).
3. Next, I would look at the Internal Factors (Tech Release, Design Change or any other Business Decisions, etc.).

External Factors (Competitor, New Product Launch, etc.), followed by

Demographics features ( Impact on any particular demographics customer segment).

Next, I would look at the Internal Factors (Tech Release, Design Change or any other Business Decisions, etc.).

Next, I will go through the User Journey on the mobile app. (Step by Step journey on the App).

### External Factors:

1. Q) Has there been any new product/feature launches or new marketing announcements by our competitors?A) Not aware of any such public announcements.
2. Did a new competitor enter the market?A) New competitors enter market every other day. However we don’t have any major news about them.
3. Q) Any negative PR, News or government regulations that we are aware of?A) No, those would have created a sudden drop and not a gradual drop.
4. Q) Is there any pattern or seasonality to this decline? In the past 6 months have we seen a decline that looks similar to this in terms of duration and deflation of users?A) This decline is not seasonally related to anything we have seen before.
5. Q) As this is a social media platform, is there any content being posted that hurts people's religious sentiments/beliefs thus leading to a boycott?A) Based on our initial analysis, there are no major concerns raised against any particular content.
6. Q) Is it that a major ISP has accidentally blacklisted the website?A) No, we checked with major ISPs. They are working fine.
7. Q) The platform might be dependent upon multiple third-party services like Cloudflare and an outage in a third-party service can lead to such issues.A) We didn’t get any such alerts till now.
8. Q) Since the drop majorly came from mobile, is there any new iOS version or Android OS update that came out that caused the apps to not work.A) No new updates that we are aware of.

Q) Has there been any new product/feature launches or new marketing announcements by our competitors?A) Not aware of any such public announcements.

Did a new competitor enter the market?A) New competitors enter market every other day. However we don’t have any major news about them.

Q) Any negative PR, News or government regulations that we are aware of?A) No, those would have created a sudden drop and not a gradual drop.

Q) Is there any pattern or seasonality to this decline? In the past 6 months have we seen a decline that looks similar to this in terms of duration and deflation of users?A) This decline is not seasonally related to anything we have seen before.

Q) As this is a social media platform, is there any content being posted that hurts people's religious sentiments/beliefs thus leading to a boycott?A) Based on our initial analysis, there are no major concerns raised against any particular content.

Q) Is it that a major ISP has accidentally blacklisted the website?A) No, we checked with major ISPs. They are working fine.

Q) The platform might be dependent upon multiple third-party services like Cloudflare and an outage in a third-party service can lead to such issues.A) We didn’t get any such alerts till now.

Q) Since the drop majorly came from mobile, is there any new iOS version or Android OS update that came out that caused the apps to not work.A) No new updates that we are aware of.

### Demographics Factors:

## This post is for paid subscribers

