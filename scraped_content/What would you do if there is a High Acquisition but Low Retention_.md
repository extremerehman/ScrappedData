# What would you do if there is a High Acquisition but Low Retention?

*Source: https://www.mypminterview.com/p/product-execution-high-acquisition-low-retention*

---

What would you do if there is a High Acquisition but Low Retention?

A new signup flow led to an increase in additional profile information by 8%. However, 7-day retention decreased by 20%. What would you do?

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share





Problem Statement



You launched a new web application signup flow to encourage new users to add more profile information. A/B test results indicate that the number of people that added additional profile information increased by 8%. However, 7-day retention decreased by 20%. What do you do?



Answer Structure



This product management interview question is a problem-solving type of question in which there is a situation where data might be pointing to conflicting outcomes, and you are asked to discover what are the causes and how to manage this conflict. Asking clarifying questions at the beginning will help you narrow the scope, and following a structured approach to answering the question will help you think logically. One approach is the following:

Ask clarifying questions to narrow the scope.After narrowing the scope, restate what the problem is to the interviewer.Identify components that can help isolate causes of the problem presented.Provide hypotheses and explain how you would test those hypotheses.Wrap up.

Ask clarifying questions to narrow the scope.

After narrowing the scope, restate what the problem is to the interviewer.

Identify components that can help isolate causes of the problem presented.

Provide hypotheses and explain how you would test those hypotheses.

Wrap up.





Answer





Q) How did you define retention? Having this answer will help me identify what type of user actions would be considered as high or low retention.

A) We measure retention by the number of logged-in sessions per week.



Q) How do you measure signups?

A) We asked a variety of questions during the signup process, some are required and some are optional. Once the user has answered all the required questions, we count that as a sign-up. The user can complete or not complete the optional questions.



Q) What happens after the user finishes the signup process?

A) When the signup process is completed, the user is redirected to a page to start using the application.





The number of people in the test group signed up about 8% more than people using the current signup process, but the 7-day retention rate for this same group was 20% less than the current retention rate. So, even though percentage-wise more people signed up with the new flow, fewer people percentage-wise returned to use the application.



Take a few minutes to think about the possible causes for this conflicting data and possible explanations for them.



I have four hypotheses as possible causes for this apparently conflicting data.



Sign-up process has too many questions, user drops off - The first one is that the sign-up flow has too many questions and the user drops off at some point in the process. The data points to an increase in sign-ups, so the user must be answering all the required questions first but dropping off once they reach the optional questions. Q) Do the required questions come first and how many required questions versus optional questions are there?A) Yes, the required questions come first. And, there are four required questions and 10 optional.That points to the situation I described, in which most users finish answering the required questions but drop off when answering the optional questions because there may be too many and they get tired.To confirm that this is the reason for the drop offs, I would check if indeed the majority of the users dropped off after the required questions were answered, and what the maximum number of optional questions that they answered was. If you see that most dropped off after the third optional question for example, that is your threshold, and the application should not include more questions.User is put off by questions that ask for private information: The second hypothesis is that the user is being asked questions that are private and gets put off by it. So, I would identify those questions that a user finds too personal and see if those are the types of questions when users dropped off. Questions a user may consider private would be: age, phone number, friends in his email contacts book, last four digits of social security number, among others. If we find that this is true, then we can determine whether the application needs that kind of data in order to work properly. If the application does need that data, then we need to apply fundamental user experience principles, such as informing the user why the application needs certain data and how that data is going to be used; telling the user that his private data will be protected and not shared; and giving the user the option to opt-out from providing this data.Lousy first experience after signup, ends with cliffhanger: The third hypothesis is that the sign-up flow ends on an unexciting landing page that doesn’t show the user the value proposition of the application and doesn’t have a clear call to action. For example, the sign-up flow should end on a page that helps the user get started using the application. This would reinforce how the application will help the user achieve the goals the application promises to do. Without this, the user will most likely never come back. So, I would find out what the next step is after sign-up and check whether users are left hanging.

Sign-up process has too many questions, user drops off - The first one is that the sign-up flow has too many questions and the user drops off at some point in the process. The data points to an increase in sign-ups, so the user must be answering all the required questions first but dropping off once they reach the optional questions. Q) Do the required questions come first and how many required questions versus optional questions are there?



A) Yes, the required questions come first. And, there are four required questions and 10 optional.



That points to the situation I described, in which most users finish answering the required questions but drop off when answering the optional questions because there may be too many and they get tired.



To confirm that this is the reason for the drop offs, I would check if indeed the majority of the users dropped off after the required questions were answered, and what the maximum number of optional questions that they answered was. If you see that most dropped off after the third optional question for example, that is your threshold, and the application should not include more questions.



User is put off by questions that ask for private information: The second hypothesis is that the user is being asked questions that are private and gets put off by it. So, I would identify those questions that a user finds too personal and see if those are the types of questions when users dropped off. Questions a user may consider private would be: age, phone number, friends in his email contacts book, last four digits of social security number, among others. If we find that this is true, then we can determine whether the application needs that kind of data in order to work properly. If the application does need that data, then we need to apply fundamental user experience principles, such as informing the user why the application needs certain data and how that data is going to be used; telling the user that his private data will be protected and not shared; and giving the user the option to opt-out from providing this data.

Lousy first experience after signup, ends with cliffhanger: 



The third hypothesis is that the sign-up flow ends on an unexciting landing page that doesn’t show the user the value proposition of the application and doesn’t have a clear call to action. For example, the sign-up flow should end on a page that helps the user get started using the application. This would reinforce how the application will help the user achieve the goals the application promises to do. Without this, the user will most likely never come back. So, I would find out what the next step is after sign-up and check whether users are left hanging.

Bugs or poor UI design: The fourth hypothesis is that there is something wrong with the UI design or functionality. Perhaps some controls are not working properly and the user gets frustrated and leaves. If this is the case, I would add if not already there, an easy way for the user to provide feedback right on the application. For example, the Zeplin web application does this very effectively, by displaying a very visible chat icon that a user can click anytime to provide feedback.

Bugs or poor UI design: The fourth hypothesis is that there is something wrong with the UI design or functionality. Perhaps some controls are not working properly and the user gets frustrated and leaves. If this is the case, I would add if not already there, an easy way for the user to provide feedback right on the application. For example, the Zeplin web application does this very effectively, by displaying a very visible chat icon that a user can click anytime to provide feedback.

Summary

To summarize, I think the conflicting situation of higher acquisition but low retention rates with the new sign-up flow can be explained in several ways. I described four hypotheses that can explain this apparent discrepancy, suggested how to confirm or deny those hypotheses, and provided recommendations on how to solve the problems. The first explanation is that the signup process is too long and users drop off after answering just the required questions; the second explanation is that users could be put off by questions they may deem too private; the third explanation is that the signup process ends without showing the user how the app can help him or what to do next; and the fourth explanation is poor UI design or bugs.



Product ExecutionHow to Answer Problem Solving Questions?Product Execution: Decline in TikTok UsageProduct Execution - Decline in Flipkart's Cart AdditionsProduct Execution: Uber Product Manager Interview - Increase in Cancel RatesProblem Execution - Decline in Facebook Groups UsageCommon Mistakes to avoid while Answering Product Manager Problem-Solving Questions

Product Execution

How to Answer Problem Solving Questions?Product Execution: Decline in TikTok UsageProduct Execution - Decline in Flipkart's Cart AdditionsProduct Execution: Uber Product Manager Interview - Increase in Cancel RatesProblem Execution - Decline in Facebook Groups UsageCommon Mistakes to avoid while Answering Product Manager Problem-Solving Questions

How to Answer Problem Solving Questions?

Product Execution: Decline in TikTok Usage

Product Execution - Decline in Flipkart's Cart Additions

Product Execution: Uber Product Manager Interview - Increase in Cancel Rates

Problem Execution - Decline in Facebook Groups Usage

Common Mistakes to avoid while Answering Product Manager Problem-Solving Questions



Share this post with a friendSince you liked this post, why not share it to help spread the word?Share