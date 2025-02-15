# How much storage space do you need to store all the information from Google maps?

*Source: https://www.mypminterview.com/p/estimation-storage-space-to-store-google-maps*

---

Estimation: Storage Space required to store all the information from Google maps?

How much storage space do you need to store all the information from Google maps?

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share



In estimation questions, interviewers are evaluating your problem-solving and quantitative skills. They are looking for a ballpark number, not an accurate number.

This product management interview question tests whether you are logical, can explain all your assumptions clearly, are organized in your work, and good with numbers.



How to structure an answer:



Ask clarifying questions. This will eliminate any ambiguity of what should be included in your calculations.Make an equation. Consider edge cases or alternate sources of data and write down any facts that you know will help with calculations.Break down the equation into components. Write down any assumptions next to the components so you don’t forget to explain them clearly to the interviewer.Do the math. Calculate the result of each component and compute the result.Do a sanity check. Do your results make sense? If not, recheck your equation, assumptions and arithmetic.

Ask clarifying questions. This will eliminate any ambiguity of what should be included in your calculations.

Make an equation. Consider edge cases or alternate sources of data and write down any facts that you know will help with calculations.

Break down the equation into components. Write down any assumptions next to the components so you don’t forget to explain them clearly to the interviewer.

Do the math. Calculate the result of each component and compute the result.

Do a sanity check. Do your results make sense? If not, recheck your equation, assumptions and arithmetic.





Ask Clarifying Questions:



Q) Is this estimation for the US alone or the world?

A) For the world.



Based on my experience with Google maps, it provides information about:

Street namesHomesPublic buildingsBusinessesTrafficNon-urban areas, like mountainous terrains

Street names

Homes

Public buildings

Businesses

Traffic

Non-urban areas, like mountainous terrains

The reason I am differentiating between homes, public buildings, and businesses are because I have seen that Google maps display more photos for buildings and business locations than for homes. Therefore, public buildings and businesses will require more storage than homes and I need to treat them separately.



Make an equation:



Here is how I would estimate storage for each of these categories.



Street names storage:[# cities] X [# streets/city] X [storage for street name]



Homes storage:[# cities] X [# homes/city] X [one photo storage + text storage]



Public buildings storage:[# cities] X [# public buildings/city] X [10 X one photo storage + text storage]



Businesses storage:[# cities] X [# businesses/city] X [10 X one photo storage + text storage]



Traffic storage:[# streets] X [storage/minute] X [# minutes/year]



Non-urban areas:[surface of the earth in square miles] X [25%] X [storage/100 sq miles]



Total storage= [Street names storage] + [Homes storage] + [Public buildings storage] + [Businesses storage] + [Traffic storage] + [Non-urban areas]



To estimate the storage required for street names, homes, public buildings and businesses, I will differentiate between large and small cities, because big cities have more of these types of locations than small cities.

For traffic storage estimation, I will assume that traffic information is kept only for a year.







Okay, let me start with the big city calculations:



I will use New York city as a proxy for a big city. It has about 1000 streets, and assuming it takes 100 KB to store the street name and other metadata, like its distance, then it takes 100 MB for a big city to store street information. I am not including photos of the street, because I will account for the street photos in the homes, public buildings and businesses storage calculations.



For the big city homes calculation, New York city has about 9M people, and assuming there are 3 people per home, that gives 1M homes. Then assuming 4 MB for a photo of the street view and 100 KB for the home location information, and multiplying by 1M homes results in about 12 TB.

Assuming there are about 10,000 public buildings in a big city, multiplying that by (40 MB + 100 KB) which is storage for photos and text, results in 400 GB. I am assuming that there are about 4x as many photos for buildings than for homes.

Assuming there are about 20,000 businesses in a big city, multiplying that by (40 MB + 100 KB) for photo and text storage results in 800 GB.



Let’s move to small city calculations:



I will assume that the number of a streets in a small city is about 1/4 of the number of streets in a big city, so 1,000 / 4 = 250. Multiplying this number of streets by 100 KB to store the street metadata results in 25 MB.

I will assume that an average of 300,000 people live in a small city. Divide by 3 persons per home, gives 100,000 homes. And multiplying that by (4 MB + 100 KB) for photo and location storage, results in 410 GB.

I will assume the number of public buildings is 1/10 of the number of buildings in a big city, so 10,000 / 10 = 1,000 buildings. Multiplying that by (40 MB + 100 KB) of storage for photos and text, results in 40 GB.

I will assume the number of businesses is 1/4 of the number in a big city, so 20,000 / 4 = 5,000. Multiplying that by (40 MB + 100 KB) of storage for photos and text results in 200 GB.



With these results, I can now calculate the total storage for one big city as 

100 MB + 12 TB + 400 GB + 800 GB = 13 TB. 

And, the total storage for a small city is

 25 MB + 410 GB + 40 GB + 200 GB = 650 GB. 

Now we need to multiply these numbers by the number of big cities and small cities. I know there are about 1,000 big cities in the world and I am going to guess that there are about 4,000 small cities, so the total storage for city information in Google maps is: 

1,000 X 13 TB + 4,000 X 650 GB, which is about 15 PB.

Let’s calculate traffic data stored in Google maps. I will assume that traffic data is only kept for one day. Under this assumption, I will estimate storage by multiplying the number of streets in the world times storage needed to record traffic per minute times minutes in a day. 

To calculate the number of streets, I will first estimate the number of streets in big cities and then small cities. I know there are about 1000 big cities in the world and I will assume that a big city, like New York City, has 1000 streets, 

so 2,000 x 1,000 results in 2M streets for big cities. 

Assuming there are 4,000 small cities in the world, and that each small city has about 250 streets, then there are 4,000 X 250 = 1M streets for all small cities. 

Then multiplying the number of streets by the storage per minute and minutes in a day gives

 (1M + 1M ) X 10 MB / minute X 1,440 minutes / day, resulting in 28 PB. 

I am assuming here that it takes 10 MB per minute to record traffic photos per street.

Now let’s calculate non-urban areas. I will use the surface area of the earth to do this. The surface area of the earth is about 4 x π x radius², where the radius of the earth is about 4000 miles. Assuming that 25% of the earth surface is solid, and to store metadata takes 400 MB per 100 sq miles, the equation becomes

 4 x 4 x (4,000 miles)^2 X ¼ X 400 MB / 100 sq miles = 256 TB.

Finally, adding storage for cities, traffic, and non-urban areas results in 

15 PB + 28 PB + 256 TB = 43 PB. 

Google holds about 15 EB per year, so I think that 43 PB for Google Maps is not unreasonable.



Share this post with a friendSince you liked this post, why not share it to help spread the word?Share