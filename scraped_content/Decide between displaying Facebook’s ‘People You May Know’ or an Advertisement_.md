# Decide between displaying Facebook’s ‘People You May Know’ or an Advertisement?

*Source: https://www.mypminterview.com/p/facebook-people-you-may-know-or-advertisement*

---

A/B Test: Decide between displaying Facebook’s ‘People You May Know’ or an Advertisement?

You are the Product Manager of Facebook News Feed and have to instruct your team on how to decide whether to display the ‘People You May Know feature’ feature or an advertisement. How do you choose?

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share



This product management interview question tests your ability to frame a trade-off problem in a clear way and how to evaluate it. Product managers have to make trade-off decisions frequently and guide their teams on how to make these decisions.

The interviewer is evaluating you on the following:

Are you able to frame the trade-off problem clearly?Are you logical when explaining your thinking?

Are you able to frame the trade-off problem clearly?

Are you logical when explaining your thinking?



How to Answer a Trade-off Question?





The key to answering this question is deciding which feature to choose by evaluating the impact of each feature on a common metric.

Keep in mind that each feature may target different user segments, so you will need to compare each feature’s impact across these segments.

Each feature will solve different user problems, have different product goals, and use a different metric of success or North Star (an indicator of user value + business impact).

When explaining why you need to define a common metric, pose the trade-off: “If I choose A instead of B, then metric A goes up. If I choose B, then metric B goes up.” You cannot decide based on two different metrics, because you need to compare apples to apples. This is why you need to define a common metric.

Defining North Stars before arriving at a common metric helps clarify why you need to establish a common metric to evaluate the trade-off between doing A or B.

Once you define a common metric, then you can re-frame the trade-off: “Choosing between A or B depends on which has a higher impact on their common metric for each different segment.”

You can measure the impact of features X and Y on their common metric by running A/B tests. And repeating an A/B test for every segment of interest. Then you can evaluate if feature X will have a lift on the metric when shown to a particular segment versus not showing it. Similarly, you can run A/B tests to test if feature Y will have a lift on the metric when shown to particular segments versus not showing it. After completing the test, you can compare feature X vs. feature Y based on their lift for each segment and pick the one with the greater lift.

The A/B test results will tell you when to show which feature in the News Feed. Depending on which segment a user falls in, you will display the winner feature from your A/B test.





How do you define a common metric, when feature X and feature Y may solve different user problems, and therefore have different product goals?

Here is how:

Define the product goal and metric of success, North Star, for X.Define the product goal and metric of success, North Star, for Y.Convert both metrics into a single common metric that measures a common business impact.

Define the product goal and metric of success, North Star, for X.

Define the product goal and metric of success, North Star, for Y.

Convert both metrics into a single common metric that measures a common business impact.

For example:

North star metric for X: “time spent on feature X while doing something.”North star metric for Y: “time spent watching a video using feature Y.”The single common metric that measures a common business impact: “ad revenue.”

North star metric for X: “time spent on feature X while doing something.”

North star metric for Y: “time spent watching a video using feature Y.”

The single common metric that measures a common business impact: “ad revenue.”

Time spent on Facebook correlates to the number of ads a user sees. And that is directly correlated to ad revenue. Therefore we can use ad revenue as the common metric.





Small Description: The ‘People You May Know’ (PYMK) feature appears on News Feed from time to time suggesting new people for me to connect with.



Q) Should I assume the PYMK feature and the advertisement are regular posts in the News Feed? I ask because I’m trying to determine if the placement of the features will impact user engagement.

A) Yes, display both as posts in the News Feed.



To decide between the two features, I need to compare each feature’s impact towards a common goal. Different features may solve numerous user problems, and therefore have various product goals. But they all need to have a positive impact on the business. If we can measure that impact, we can define a common metric.

To do that, I want to identify the user problems these features solved, and how solving these problems impacts the business.





I will start by identifying the product goal of the PYMK feature.

The PYMK feature helps users grow their network of friends to increase their enjoyment on the platform. Most Facebook features depend on fun interactions with friends. Therefore the product goal of PYMK is to help users grow their network of friends to increase their enjoyment on the platform. Doing this is also good for Facebook because the more time users spend on the platform, the more ad impressions they are likely to see, increasing ad revenue. Therefore the business goal is to increase ad revenue.

A North Star metric for PYMK that is an indicator of user value and business impact could be “time spent engaging with new PYMK friends and posts or activities associated with them.”Spending time with new friends tells me we are providing user value, but it also tells me we are impacting the business because time spent correlates with the number of ad impressions.

PYMK may not have the same effect for all users. For example, active users with hundreds of friends may ignore this feature because they are already very active with current friends. But PYMK could be especially effective in increasing the number of friends of people recently registered on the platform.





Now, let’s switch to the advertisement. An ad serves two users: advertisers and the end-user. Ads enable advertisers to convert users. And, ads help users to discover new things to buy or read. So,

The product goal relative to advertisers is to enable advertisers to promote their products to interested users.The product goal relative to users is to help users discover and consume interesting things.The business goal is to increase ad revenue.

The product goal relative to advertisers is to enable advertisers to promote their products to interested users.

The product goal relative to users is to help users discover and consume interesting things.

The business goal is to increase ad revenue.

A North Star metric that indicates user value and business impact is the “number of views per ad or clicks per ad.” Viewing and clicking indicate users are interested (user value), and advertisers are getting conversions (user value). The number of clicks and views also indicates an increase in advertisement revenue (business impact).



So we have two different metrics that measure the success of PYMK and an advertisement. But because their product goals and North Star metrics are different, we cannot compare which one would be more important to show. To evaluate which one is better to display, we need to find a common goal to measure with a single metric. The common goal they share is to impact the business, so we need to find a common metric that measures that impact.

For the PYMK feature, the “time spent” metric translates into the number of ad impressions seen during that time. And that translates to “total revenue” from ad impressions seen during that time or an average, “$/ad.”

For the advertisement, the “number of views or clicks per ad” metric translates to “total revenue” from all ads displayed during a period of time or an average, “$/ad.”

Now, we have two common metrics we can use, either “$ earned during a period of time” or “$/ad.” So we can use one of these metrics to test the impact of PYMK vs. an advertisement on this metric using an A/B test.

Since it may take some time to see the PYMK feature’s effect on increased activity, especially for new users, we need to pick a test duration that is long enough to see the results. The period could be from two weeks to a couple of months. I would consult with my data scientist team to pick the correct period.

There is also the issue of PYMK being better for some segments than others. PYMK is better for new users who have few friends, but probably not so much for active users who already engage with lots of existing friends. And we have a similar situation with ads, for example. If a user is too new, the platform may not have sufficient profile information to target relevant advertisements to the user. Therefore, we need to test the business impact of PYMK and an advertisement across different segments of users from very new to less new.

Otherwise, if we do not segment, the impact on ad revenue by the PYMK feature and advertisement will be averaged, and their difference may not be discernible. This is because PYMK is best for newly registered users, while the advertisement is best for existing users. Therefore, while one feature has a significant revenue impact on one half of the group, it has low impact on the other half. These opposing revenue effects will result in an average revenue impact for both features, if shown to a group with equal numbers of ‘new registered’ users and existing users.

Therefore, we need to run A/B tests across different segments, from new to older users.

A/B tests are expensive in terms of time and cost. So, I would define the least number of segments possible. I would consult with my data science team and recommend starting with three segments:

“new users with few friends,”“semi-new users with more friends,” and“existing users with more friends.”

“new users with few friends,”

“semi-new users with more friends,” and

“existing users with more friends.”

I would suggest two attributes to define these segments:

“the number of days passed since they registered” and“the number of friends.”

“the number of days passed since they registered” and

“the number of friends.”

The idea is to segment users from “very new” to “less new” to distinguish which user group responds to the PYMK feature or an advertisement in terms of increasing ad revenue. The specific values for “number of days passed since registered” and “number of friends” that will determine the segmentation of the users would require consulting with the data science team.

Alternatively, we can use machine learning algorithms to classify users into segments, but that could take more time then running A/B tests.



With the common metric and the segments defined, I would conduct A/B tests in the following way.





Test metric:

Total ad revenue ($)

Total ad revenue ($)

Hypotheses:

Revenue $x from PYMK is greater than revenue $p from the controlled experienceRevenue $y from the ad is greater than revenue $p from the controlled experience

Revenue $x from PYMK is greater than revenue $p from the controlled experience

Revenue $y from the ad is greater than revenue $p from the controlled experience

Duration:

n weeks

n weeks

We are testing whether to show the PYMK feature or an advertisement in a user’s News Feed. The group undergoing the controlled experience will see the News Feed in the default manner they do today, scrolling through the News Feed and seeing advertisements once in a while. We are trying to answer the question: Will the PYMK feature have a higher lift in ad revenue, or will a new advertisement?

To find an answer, I will run three experiences for each segment:

A controlled experience which is the default News Feed (no PYMK feature nor advertisement).An experience showing the PYMK feature.And, an experience displaying a new advertisement.

A controlled experience which is the default News Feed (no PYMK feature nor advertisement).

An experience showing the PYMK feature.

And, an experience displaying a new advertisement.

We will test two hypotheses:

The experience with the PYMK feature will bring more revenue than the controlled experience (PYMK revenue $x > Controlled experiment revenue $p).The experience with the advertisement will bring more revenue than the controlled experience (Ad revenue $y > Controlled experiment revenue $p).

The experience with the PYMK feature will bring more revenue than the controlled experience (PYMK revenue $x > Controlled experiment revenue $p).

The experience with the advertisement will bring more revenue than the controlled experience (Ad revenue $y > Controlled experiment revenue $p).

We will run these A/B tests across all segments and fill out the table with the total revenue earned by the controlled experience, the PYMK feature experience, and the ad experience.

The tests will run until we reach statistical significance. We can get an estimate of when this will happen from the data science team.

Once we’ve reached statistical significance for all tests, we can determine whether PYMK or the advertisement resulted in larger revenue than the controlled experiment per segment. Then we can select the feature that generated higher revenue as the winner for each segment. If neither the PYMK nor the ad increased revenue relative to the controlled experiment, there would be no winner.

To put our results in practice, I would advise the team to adjust the News Feed algorithm to detect when users belong to each segment and show them the winning feature.

Question: Your tests will tell you if the PYMK feature or the advertisement generated higher revenue than the controlled experiment. And for each segment, you pick the feature with the largest revenue as the winner. But what if the difference in revenue lift is minimal between the two features? How sure are you that this small difference is not just due to randomness?

Your Answer) We could introduce a new hypothesis that tests whether “PYMK revenue – Ad revenue > 0” with a confidence level of 95%. Or, we can be more aggressive and say that if PYMK doesn’t bring at least X more dollars than the advertisement, then we don’t bother with it. Instead of comparing the difference between PYMK revenue and Ad revenue with 0, we compare it with X dollars.

Summary



To understand the consequences of choosing between displaying the PYMK feature or an advertisement, I compared their impact against a common business goal or metric. To do this, I started by understanding what each product does, its individual goals, and its north star metrics. After realizing their metrics are different, I normalized them into a common business metric, ad revenue. Using this common business metric, we can run A/B tests for each (PYMK feature and advertisement) against the default user experience of the News Feed.

And I introduced the segmentation of users from new to less new, to better identify which feature (PYMK or Advertisement) will have more revenue impact on each segment. The winner per segment is the feature with an increased lift in revenue relative to the controlled experience. To be more confident about our choice, we can run an additional A/B test comparing the difference in revenue brought by the PYMK feature and the advertisement.

I’ve only touched the surface when it comes to different ways of segmenting the users. We could segment users by different attributes or behaviors. Attributes can be geography, the type of platform used, or the time of day. Behaviors are actions users perform on the platform, such as reacting to posts or saving a post.

As you can see, it can get really complex. So, I would recommend using machine learning algorithms instead of A/B tests if the number of attributes becomes too large. The machine learning algorithms could continuously learn which segments respond better to the different features to maximize ad revenue.

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share