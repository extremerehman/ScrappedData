# Decline in TikTok Usage

*Source: https://www.mypminterview.com/p/product-execution-decline-in-tiktok-usage*

---

Decline in TikTok Usage | Product Execution

You are a PM at TikTok and you observed that there is a decline in TikTok's viewership. How would you find the root cause of the issue?

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share



Product Execution questions are all about dealing with a live issue in a technology platform. How would you diagnose the issue? What would you do to investigate further? Here, we'll break down the execution question and show you detailed examples of how to ace the Execution PM Interview Questions.



Problem Statement



You are a PM at TikTok and you observed that there is a 10% decline in TikTok's viewership. How would you diagnose and find the root cause of the issue?



How are you being evaluated?



The interviewer is testing to see if you have an organized and logical approach to solving problems. In this product execution interview question, there is a situation where data could be pointing to a problem or outcomes that conflict with each other. You are asked to discover what the causes are and explain how to solve the problem.

The interviewer is evaluating you on the following:

What is your thought process when diagnosing and solving a business problem?Are you logical?Are you exhaustive in listing the possible causes?Are you articulate in your delivery or do you tend to ramble?

What is your thought process when diagnosing and solving a business problem?

Are you logical?

Are you exhaustive in listing the possible causes?

Are you articulate in your delivery or do you tend to ramble?



First, take a minute to think and write down the structure and approach of the answer. Next,





Have we changed anything with the logs recently about how we log things or capture data? Is it possible that there is a logging error here?A) No, we haven’t changed anything as far as logging is concerned.Is there any pattern or seasonality to this decline? In the past 6 months have we seen a decline that looks similar to this in terms of duration and deflation of users?A) This decline is not seasonally related to anything we have seen before.

Have we changed anything with the logs recently about how we log things or capture data? Is it possible that there is a logging error here?

A) No, we haven’t changed anything as far as logging is concerned.

Is there any pattern or seasonality to this decline? In the past 6 months have we seen a decline that looks similar to this in terms of duration and deflation of users?

A) This decline is not seasonally related to anything we have seen before.

Now that we have eliminated the option of seasonality and logging issue, let jump into diagnosing what could be going wrong here. 

The framework that I'll be using to walk through this is, first I would check for any human factor and then followed by investigating if there are hardware or operating system errors, if there are app errors and if there are any network or server errors.



Let’s start with the Human factor: 

Is there any world event going on or something that might be affecting our viewership in any way?A) I'm not super aware of any major events that are going on right now, do you have any ways we could maybe detect that or figure that out?

Is there any world event going on or something that might be affecting our viewership in any way?

A) I'm not super aware of any major events that are going on right now, do you have any ways we could maybe detect that or figure that out?



One way to check it is to look for patterns in new and trending hashtags or topics on TikTok. I would look at the top 20 hashtags in different areas and regions to see if there's a certain region that's having a decline. 

Could you tell me whether or not there are new hashtags that spiked recently  in TikTok?A) We're not seeing any sort of regional variation that could indicate any problem.

Could you tell me whether or not there are new hashtags that spiked recently  in TikTok?

A) We're not seeing any sort of regional variation that could indicate any problem.



Let’s move on to the Hardware & Software part,

Do we see any pattern across the hardware versions? For example, it can happen that the latest version of the iPhone is no longer operable with TikTok.A) We're seeing a similar decline across all the versions on different platforms and devices.

Do we see any pattern across the hardware versions? For example, it can happen that the latest version of the iPhone is no longer operable with TikTok.

A) We're seeing a similar decline across all the versions on different platforms and devices.



Can we do the same thing for operating systems? like, maybe the latest version of Android or IOS is no longer operable with TikTok.A) We're not seeing any major pattern there.If we slice by App version do we see any pattern of that viewership decline across App versions?A) We're seeing a similar decline across app versions as well.

Can we do the same thing for operating systems? like, maybe the latest version of Android or IOS is no longer operable with TikTok.

A) We're not seeing any major pattern there.

If we slice by App version do we see any pattern of that viewership decline across App versions?

A) We're seeing a similar decline across app versions as well.



I'd like to investigate the network, to see if there are any network issues,

Can we slice by carriers  to see if there's any like relationship with the carrier and the decline in viewership?A) We are not seeing any differences there either, it's sort of an overall decline.

Can we slice by carriers  to see if there's any like relationship with the carrier and the decline in viewership?

A) We are not seeing any differences there either, it's sort of an overall decline.



Now that we have eliminated the hardware, operating system, App, and network. Let’s now look at the server or the data center.

Is there any issue reported at the data center? like an outage?A) All systems are green and seem to be fine. We haven't noticed any outages or anything like that however, we're seeing space utilization is not growing quite as fast.

Is there any issue reported at the data center? like an outage?

A) All systems are green and seem to be fine. We haven't noticed any outages or anything like that however, we're seeing space utilization is not growing quite as fast.

So that indicates that TikTok is not storing as much information or data or the growth might be slowing down.

Has there been any change in the number of video uploads per day for TikTok?A) Yeah, there does seem to be some pattern here where video uploads are slowing down at the same time when the viewership is declining.

Has there been any change in the number of video uploads per day for TikTok?

A) Yeah, there does seem to be some pattern here where video uploads are slowing down at the same time when the viewership is declining.

There could be 2 possible cause I can think of, for people to stop uploading videos,  one is, 

External causes, like maybe people have decided to not upload videos maybe people are stuck at home and have nothing to upload (which is probably not the case because TikTok has exploded over in the COVID period).Internal issues can be TikTok has created some bugs or problems.

External causes, like maybe people have decided to not upload videos maybe people are stuck at home and have nothing to upload (which is probably not the case because TikTok has exploded over in the COVID period).

Internal issues can be TikTok has created some bugs or problems.

Next, I want to check is, 

Is there any increase in feedback reports to TikTok? (like in terms of the total number of tickets filed for support issues)A) Yes, we are seeing an increase in support tickets.Not sure on the level of granularity of these support tickets, but do we have any idea about the type of issues that are reported? (Like is it a bug or an error state)A) We are seeing reports of bugs.

Is there any increase in feedback reports to TikTok? (like in terms of the total number of tickets filed for support issues)

A) Yes, we are seeing an increase in support tickets.

Not sure on the level of granularity of these support tickets, but do we have any idea about the type of issues that are reported? (Like is it a bug or an error state)

A) We are seeing reports of bugs.

I'm going to try to view it on the see it from the uploader perspective. 

Can we slice by hardware or operating system to see if the video upload quantity has deviated at all across hardware versions or operating system versions?A) By hardware and operating system versions we're not seeing any major differences in view uploadsCan we check the app version next and if there's any deviation there?A)  Yes, so we checked the app versions and there's a deviation in the latest app version for video uploads.Is it the latest app version that has the issue? A) Yes, it seems to be the latest one where the rate of upload seems to be decreasing.

Can we slice by hardware or operating system to see if the video upload quantity has deviated at all across hardware versions or operating system versions?

A) By hardware and operating system versions we're not seeing any major differences in view uploads

Can we check the app version next and if there's any deviation there?

A)  Yes, so we checked the app versions and there's a deviation in the latest app version for video uploads.

Is it the latest app version that has the issue? 

A) Yes, it seems to be the latest one where the rate of upload seems to be decreasing.

To confirm our hypothesis here, the next few things I would check are,

I would go through the support tickets to identify the actual cause here.I would go through the video upload journey or flow to see if something is wrong here.If we have done a staged rollout, I would check the data to identify if the decline in viewership started after the release of the app version.

I would go through the support tickets to identify the actual cause here.

I would go through the video upload journey or flow to see if something is wrong here.

If we have done a staged rollout, I would check the data to identify if the decline in viewership started after the release of the app version.

A) When we looked at that we do see that this decline seemed to precede the official launch of this app version so it does seem to be related to this particular app version so I think we've confirmed that.



Summary



Just to recap, I was first investigating the logging errors and then went through to see if there's any issues on the viewership side, then investigating the video upload side and figuring out what was affecting that video upload speed that then affected the viewership.

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share