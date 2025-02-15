# Estimate the storage space is required to host all the images of Google Street View

*Source: https://www.mypminterview.com/p/storage-space-to-store-google-street-view-images?s=w*

---

Estimate the storage space is required to host all the images of Google Street View

How much storage space is required to host all the images of Google Street View?

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share



In this product management interview question, the interviewer is assessing your ability to provide quick estimates related to a product. The estimation could be about revenue, the number of users, or something else. Why is the interviewer asking you to do this? Because as a product manager you may need to estimate the size of a new market or revenue, or any other business opportunity, to convince stakeholders of a new idea. Therefore, this is an essential skill.

The interviewer is evaluating you on the following:

Are you methodical and articulate when explaining your estimation approach?Is the interviewer able to follow you when you make calculations?Can you make calculations quickly?Do you explain your assumptions convincingly?

Are you methodical and articulate when explaining your estimation approach?

Is the interviewer able to follow you when you make calculations?

Can you make calculations quickly?

Do you explain your assumptions convincingly?

The key to answering estimation questions is to separate the “how-to” from the calculations. Separating operations from calculations prevents the interviewer and you from getting lost in calculations and losing track of what you are calculating. An estimation tree does this. Using an estimation tree allows you to explain your logic behind the operations first, to then focus solely on calculations.

Here is how to structure the answer:

Ask clarifying questions. Clarifying eliminates any ambiguity of what should include in your calculations.Make an equation. Consider edge cases or alternate sources of data and writing any facts that you know helps with calculations.Break down the equation into components. Write your assumptions next to the components. Doing this reminds you to explain the assumptions clearly to the interviewer.Do the math. Calculate the result of each component and compute the result.Do a sanity check. Do your results make sense? If not, recheck your equation, assumptions, and arithmetic.

Ask clarifying questions. Clarifying eliminates any ambiguity of what should include in your calculations.

Make an equation. Consider edge cases or alternate sources of data and writing any facts that you know helps with calculations.

Break down the equation into components. Write your assumptions next to the components. Doing this reminds you to explain the assumptions clearly to the interviewer.

Do the math. Calculate the result of each component and compute the result.

Do a sanity check. Do your results make sense? If not, recheck your equation, assumptions, and arithmetic.



Ask Clarifying Questions

Q) Should we focus on any particular country or the entire world? A) Consider entire World.

Q) Should we focus on any particular country or the entire world? A) Consider entire World.



To estimate the storage needed for all pictures, I need two pieces of information to help me come up with an estimate: 

Average size of an image.Number of images taken.

Average size of an image.

Number of images taken.



Let’s say each 360-degree image on Google Street View is 20MB. I’m picking a large number because Google Street View images are usually 360 degrees. And If they are not, we can assume that some of the images taken from one spot to cover all angles are 20MB.

Make an Equation:

To calculate the total number of images on Google Street View, I have to calculate, 

The total # of images per KM    X    # of KM’s covered in Google StreetView.



Break down the equation into components:



To estimate the number of images per KM, I think about my own experience using Google StreetView. I’ve noticed that the smallest move I can make to change my view of a street is about 10 meters. 

Let’s assume that on every 1km (1,000 meters), there are 1000/10 = 100 images.

Now, we need to calculate the number of KM’s of streets covered by Google StreetView.

Ideally, Google Street View can cover all streets around the world and that’s the direction that it’s going. So, I’m going to come up with the total distance of all streets worldwide for the 7 billion population on earth. 

Do the math:



Let’s assume 2billion people live in towns and 5 billion live in cities.



To estimate the total distance of streets in towns, we can look at the total distance for a 2,000-person town first and then multiply that number by 1million. 

Let’s assume all 2,000 people live in houses and the distance between houses is about 10 meters. 

So, if each house consisted of 4 people, we would have a total of 2,000/ 4 = 500 houses. 

If all houses were in one street on both sides of the street, we would have about 500 houses x 10 meters / 2 = 2,500 meters of street covering houses. 

So, for every 2,000 people in a small town, there is 2.5km of street.

I should mention that in reality all houses are not in one street and some might be in by an intersection, meaning they are connecting two streets but then there are also streets with no houses (e.g. commercial areas) so for the sake of this estimation, I will assume that for every 2,000 people in a town, there are about 2.5 km of street. 

In order words, for 2 billion people who live in towns, there are 2.5 million km of streets. 

This is a very rough estimate because in some small towns, there might be apartments and people might live in denser neighborhoods. But then there can also be places where the distance of houses is more than 10meters. 

So we’ll assume 10meters is the average distance between the houses in towns.



For cities, let’s break down the population into two groups: 

50% live in houses – 2.5 billion live in houses in cities. 

50% live in apartments – 2.5 billion live in apartments in cities. 

Let’s say that for those who live in houses, average people in a house is 3 and distance between houses is 10 meters.

 In other words, for 2.5 billion people who live in houses in cities, we have about (2.5 billion / 3) = 800million houses. 

Assuming the distance between houses is again 10 meters and houses are on both sides of the street, 

we have a total of 800 million x 10 meter / 2 = 4 billion meters or 40 million km of street.

To estimate street for 2.5 billion people who live in apartments, let’s say that on average every 100 people live in one building. And the distance between apartments is 100 meters. Assuming apartments are on both sides of the street, we can say that for every 100 people, we have 100 / 2 = 50 meters of street. 

In other words, for 2.5 billion people, we have 1.25 billion meter or 12.5 million km of street.

Now, people in cities usually work in offices and shops. Let’s say that on average 20% of people who live in cities work – 

Estimated population would be 20% of 2.5 billion = 500 million. 

And every office building includes 100 people and the distance between office buildings is 100 meters. 

Assuming office buildings are on both sides of the streets, for every 100 people, there are 100 / 2 = 50 meters of street for their office. 

In other words, for 500 million people living in cities, there are 250 million meter or 0.25 million km of street.

Now, let’s add all numbers together:2.5 million km (representing towns) + 40 million km (representing houses in cities) + 12.5 million km (resenting apartments in cities) + 0.25 million km (representing offices in cities) 

= 55.25 million km of street in total

Final Answer



Now, given each km includes 100 images and each image is 20MB, 

The total size of all StreetView images is:

55.25 million km x 100 images per km x 20MB of file 

= 110.5 million GB 

= 115 thousand TB.



The total size of all images to be stored on Google Street view would be 115 thousand TB.



Note:

We can also add street-view for unpopulated regions ( e.g. “highways”, ” National parks” etc.). Feel free to add their estimation in the comments below!



Share this post with a friendSince you liked this post, why not share it to help spread the word?Share