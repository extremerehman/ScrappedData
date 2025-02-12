# Drop in YouTube View Duration

*Source: https://www.mypminterview.com/p/drop-in-youtube-view-duration-root-cause-analysis*

---

[Share](https://www.mypminterview.com/p/drop-in-youtube-view-duration-root-cause-analysis?utm_source=substack&utm_medium=email&utm_content=share&action=share)



### Problem Statement:

You are the Product manager at YouTube. You see, there is a 30% drop in the Average View Duration. Do a Root Cause Analysis and Tell us what could have happened  to devise appropriate solutions.

### How are you being evaluated?

During this product execution interview question, the interviewer assesses your ability to approach problems in an organized and logical manner. The situation presented involves conflicting data that suggests a problem, and you are tasked with identifying the root causes and providing potential solutions. Your evaluation will focus on the following aspects:

1. Your thought process while diagnosing and solving a business problem: They are interested in how you approach complex situations, analyze data, and derive insights to address the issue.
2. Your ability to apply logical reasoning in identifying potential causes: The interviewer wants to see if you can logically connect the available information and consider various factors contributing to the problem.
3. Your ability to be exhaustive in listing possible causes: They want to assess if you can consider multiple angles and potential factors that might be influencing the observed outcomes.
4. Your ability to communicate clearly and concisely while delivering your analysis and recommendations: The interviewer wants to evaluate your ability to express your thoughts coherently, avoiding rambling or unnecessary tangents.

Your thought process while diagnosing and solving a business problem: They are interested in how you approach complex situations, analyze data, and derive insights to address the issue.

Your ability to apply logical reasoning in identifying potential causes: The interviewer wants to see if you can logically connect the available information and consider various factors contributing to the problem.

Your ability to be exhaustive in listing possible causes: They want to assess if you can consider multiple angles and potential factors that might be influencing the observed outcomes.

Your ability to communicate clearly and concisely while delivering your analysis and recommendations: The interviewer wants to evaluate your ability to express your thoughts coherently, avoiding rambling or unnecessary tangents.

First, take a minute to think and write down the structure and approach of the answer. Next,

### Describe the feature or product:

Once you are clear about the question, start by explaining your understanding of the product. Cover the following things about the product,

* What does the product do?
* Who uses it?
* How are they using it?
* What pain point is it solving for the users?

What does the product do?

Who uses it?

How are they using it?

What pain point is it solving for the users?

Youtube is an online entertainment cum video-sharing platform where users come to view, like, comment, share, upload, and monetize their video content. This platform not only entertains but also helps learners with its wide range and variety of subjective content. The primary target audience of YouTube involves information or knowledge seekers, children, music lovers, skill developers, entertainment lovers, Vlogs, or event followers.

Content Creators on YouTube can upload their content by creating channels and viewers who are interested in a particular topic can subscribe to such channels.

YouTube currently works in a freemium model by keeping most of its content free and showing a lot of ads. Users can, however, subscribe to YouTube Premium for ad-free content, which can be downloaded and watched in offline mode.

YouTube also offers YouTube Music (Video Music streaming service by YouTube), YouTube TV (Live TV with 100+ channels), and YouTube for Kids (Videos specifically made for Kids (<18 years) of different age group).

YouTube can be accessed from a desktop web, desktop app, mobile web, and mobile app (Android, IOS, Windows).

Some of the major competitors of YouTube (for viewers) are Facebook, Instagram, Snapchat, TikTok etc. and YouTube (for publishers) are Vimeo, Twitch, Hulu etc.

First, take a minute to think and write down the structure and approach of the answer. Next,

#### Sanity Check:

Q) Have we changed anything with the logs recently about how we log things or capture data? Is it possible that there is a logging error here?

A) No, we haven’t changed anything as far as logging is concerned.



### Ask Clarifying Questions:

1. Q: Has there been any significant change in content upload rates or the type of content uploaded?A: No significant change in content upload rate has been observed.
2. Q: Are there any issues related to the streaming quality, such as buffering, video resolution problems, or server outages?A: No such issues have been reported, and streaming quality remains consistent.
3. Q: Have there been any recent changes to the YouTube algorithm, such as content recommendations or ranking logic?A: No change has been made in the algorithm.
4. Q: Is there a pattern in the drop, such as sudden drop at specific times of day or gradual drop across the week ?A: The decline is consistent throughout the week.
5. Q: Is the drop in Average View Duration (AVD) uniform across all content types (shorts, live streams, long-form videos), or does it affect specific types of contentA: The drop is prominent in long-form videos compared to shorts content type.

Q: Has there been any significant change in content upload rates or the type of content uploaded?A: No significant change in content upload rate has been observed.

Q: Are there any issues related to the streaming quality, such as buffering, video resolution problems, or server outages?A: No such issues have been reported, and streaming quality remains consistent.

Q: Have there been any recent changes to the YouTube algorithm, such as content recommendations or ranking logic?A: No change has been made in the algorithm.

Q: Is there a pattern in the drop, such as sudden drop at specific times of day or gradual drop across the week ?A: The decline is consistent throughout the week.

Q: Is the drop in Average View Duration (AVD) uniform across all content types (shorts, live streams, long-form videos), or does it affect specific types of content

A: The drop is prominent in long-form videos compared to shorts content type.

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
5. Q) Is there any content being posted that hurts people's religious sentiments/beliefs thus leading to a boycott?A) Based on our initial analysis, there are no major concerns raised against any particular content.
6. Q) Is it that a major ISP has accidentally blacklisted the website?A) No, we checked with major ISPs. They are working fine.
7. Q) The platform might be dependent upon multiple third-party services like Cloudflare and an outage in a third-party service can lead to such issues.A) We didn’t get any such alerts till now.
8. Q) Since the drop majorly came from mobile, is there any new iOS version or Android OS update that came out that caused the apps to not work.A) No new updates that we are aware of.

Q) Has there been any new product/feature launches or new marketing announcements by our competitors?A) Not aware of any such public announcements.

Did a new competitor enter the market?A) New competitors enter market every other day. However we don’t have any major news about them.

Q) Any negative PR, News or government regulations that we are aware of?A) No, those would have created a sudden drop and not a gradual drop.

Q) Is there any pattern or seasonality to this decline? In the past 6 months have we seen a decline that looks similar to this in terms of duration and deflation of users?A) This decline is not seasonally related to anything we have seen before.

Q) Is there any content being posted that hurts people's religious sentiments/beliefs thus leading to a boycott?A) Based on our initial analysis, there are no major concerns raised against any particular content.

Q) Is it that a major ISP has accidentally blacklisted the website?A) No, we checked with major ISPs. They are working fine.

Q) The platform might be dependent upon multiple third-party services like Cloudflare and an outage in a third-party service can lead to such issues.A) We didn’t get any such alerts till now.

Q) Since the drop majorly came from mobile, is there any new iOS version or Android OS update that came out that caused the apps to not work.A) No new updates that we are aware of.

### Demographics Factors:

Q) Has it affected any particular demographic customer segment? (Gender / Age / Location, Persona) like is the Decline is from a certain city/region or in a certain gender segment?A) No, we didn’t find any such demographic changes. The decline is uniform across different locations, gender, and age groups. It’s a uniform distribution.

### Internal Factors:

1. Q) Were there any recent tech releases or design changes?A) YouTube conducts releases frequently, but no reported issues or updates directly correlate with this decline. No major design changes occurred recently.
2. Q) Have there been any reported issues or system outages at the data center? A) No, all systems are functioning properly, and we haven't experienced any outages.
3. Q) Was there any increase in Crash reports, ANR (App Not Responding) or Home screen load time?A) No, we did not observe any spike in these numbers.
4. Q) Any recent App updates or major releases that happened?A) No we have not sent update recently.
5. Q) Any increase in the number of incidents, bugs, uninstalls or Playstore ratings and reviews reported from customers in the last 7 days? A) No, we didn’t find anything unsual there.Share

Q) Were there any recent tech releases or design changes?A) YouTube conducts releases frequently, but no reported issues or updates directly correlate with this decline. No major design changes occurred recently.

Q) Have there been any reported issues or system outages at the data center?

A) No, all systems are functioning properly, and we haven't experienced any outages.

Q) Was there any increase in Crash reports, ANR (App Not Responding) or Home screen load time?A) No, we did not observe any spike in these numbers.

Q) Any recent App updates or major releases that happened?A) No we have not sent update recently.

Q) Any increase in the number of incidents, bugs, uninstalls or Playstore ratings and reviews reported from customers in the last 7 days? A) No, we didn’t find anything unsual there.

[Share](https://www.mypminterview.com/p/drop-in-youtube-view-duration-root-cause-analysis?utm_source=substack&utm_medium=email&utm_content=share&action=share)

### User Journey:

Next, we will go through the user journey and see if there is any glitch/bug in the journey for users accessing and watching videos on YouTube:

