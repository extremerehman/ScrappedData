# Estimate the total number of Uber Rides

*Source: https://www.mypminterview.com/p/estimate-the-total-number-of-uber-rides*

---

Estimate the total number of Uber Rides - My PM Interview

Product Management Interview Question: Guess estimate the total number of Uber Rides

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share



Product Estimation questions are frequently asked by interviewers in product management interviews, to check your ability to estimate metrics (such as revenue, cost, the number of users, etc.) of a product.

Guess-estimation becomes an important skill for a product manager when it comes to estimating the revenue of a product, the size of a new market, the cost of running a product, the revenue or growth potential of a new business opportunity and convincing stakeholders of a new product idea and its prioritization in the roadmap.



While answering, its important to

Communicate the estimation approach in a structured way while explaining.Make sure the interviewer is on the same page with your calculations and approach.Explain your assumptions and the rationale behind them.Use an estimation tree, it allows you to explain your operations' logic first, then focuses solely on calculations.

Communicate the estimation approach in a structured way while explaining.

Make sure the interviewer is on the same page with your calculations and approach.

Explain your assumptions and the rationale behind them.

Use an estimation tree, it allows you to explain your operations' logic first, then focuses solely on calculations.

Answer Structure:

Here is a step-by-step framework, you may follow while answering product estimation interview questions during your interview:

Ask clarifying questions to remove ambiguity and narrow the scope of the question.Make an equation. based on the assumptions, edge cases, and data sources.Break down the equation into components along with explaining your assumptions.Calculate each component to solve the equation and find the result.Do a sanity check of your equation, assumptions, and calculations.

Ask clarifying questions to remove ambiguity and narrow the scope of the question.

Make an equation. based on the assumptions, edge cases, and data sources.

Break down the equation into components along with explaining your assumptions.

Calculate each component to solve the equation and find the result.

Do a sanity check of your equation, assumptions, and calculations.



1. Ask Clarifying Questions

Q) We are talking about Uber car-based rides only (NOT scooters, public transit, or helicopters)?A) Yes.Q) Do we want to calculate the number of rides per Day / Week / Month / Year? A) Calculate per Day.Q) Is this for any particular Geography? A) Consider for US only.Q) Assumption: “Ride” mean only successful ride?A) Yes. Q) Should we include both regular and premium Uber rides? A) Yes. 

Q) We are talking about Uber car-based rides only (NOT scooters, public transit, or helicopters)?A) Yes.

Q) Do we want to calculate the number of rides per Day / Week / Month / Year? A) Calculate per Day.

Q) Is this for any particular Geography? A) Consider for US only.

Q) Assumption: “Ride” mean only successful ride?A) Yes. 

Q) Should we include both regular and premium Uber rides? A) Yes. 

2. About the Product:

Uber is a ridesharing platform that connects riders to drivers. The goal of the platform is to provide easy, affordable and hasle free mode of transportation.

Uber provides multiple services like  Ride-Hailing, Food Delivery, Package Delivery, Couriers, Freight transportation, Electric Bicycles, Scooters, and Ferry transport. 

For the sake of this question, we would just be concentrating on Uber Car Rides.

3. Make an Equation:



Total Number of Uber Rides in US per day = 

( #of Uber Users   X    Average no of rides )   per user segment



4. Breakdown of Equation: 



Total US population = 300M

Target Uber audience age is in the range of 15 to 65. (with an average life expectance of 80 years)

Thus, the target user count = (50/80)x300M = 190M

Assuming 50% of these users actually use Uber → 95M Uber users.

Now, splitting the user segment by their usage type:

Power UsersNormal UsersDormant Users

Power Users

Normal Users

Dormant Users

Assuming 20% users are Power users, who use Uber at least once a week.

= 20% of 95M

= 19M users

Hence, the number of riders per day,

 = 19/7 = 2.7M Rides

Assuming 60% users are Normal users, who use Uber at least once a month.

= 60% of 95M

= 57M

Hence, the number of riders per day,

= 57/30 = 1.9M Rides

Assuming 20% users are Normal users, who use Uber at least once a Quarter.

= 20% of 95M

= 19M

Hence, the number of riders per day,

= 19/90 = 0.2M Rides

Hence, 

Total Number of Uber Rides in US per day,

= 2.7M + 1.9M + 0.2M 

=~4.8M Rides.



5. Do A Sanity Check:



Let’s do the same calculation with a different approach to validate the numbers,

Rides = (# of drivers) x (# of hours per driver) x (# of rides per hour)



# of US population: 300 million# of registered drivers: (80%) => 240 millionService driver: (5%) => 12 millionTruck: 5%Taxi/Cab: 25% → 3 millionPublic transport: 5%Others: 55%Taxi/Cab: 3 millionTraditional Taxi: 40%Uber: 30% → 1 millionLyft: 15%Other: 15%

# of US population: 300 million

# of registered drivers: (80%) => 240 million

Service driver: (5%) => 12 millionTruck: 5%Taxi/Cab: 25% → 3 millionPublic transport: 5%Others: 55%

Service driver: (5%) => 12 million

Truck: 5%Taxi/Cab: 25% → 3 millionPublic transport: 5%Others: 55%

Truck: 5%

Taxi/Cab: 25% → 3 million

Public transport: 5%

Others: 55%

Taxi/Cab: 3 million

Traditional Taxi: 40%Uber: 30% → 1 millionLyft: 15%Other: 15%

Traditional Taxi: 40%

Uber: 30% → 1 million

Lyft: 15%

Other: 15%

# of Uber drivers (1 million)# of full-time drivers (30%) => 0.3 million# of part-time drivers (50%) => 0.5 million# of occasional drivers (20%) => 0.2 million

# of Uber drivers (1 million)

# of full-time drivers (30%) => 0.3 million# of part-time drivers (50%) => 0.5 million# of occasional drivers (20%) => 0.2 million

# of full-time drivers (30%) => 0.3 million

# of part-time drivers (50%) => 0.5 million

# of occasional drivers (20%) => 0.2 million



Full-time8 hours per dayPart-time4 hours per dayOccasional1 hours per day

Full-time

8 hours per day

8 hours per day

Part-time

4 hours per day

4 hours per day

Occasional

1 hours per day

1 hours per day

Total hours per day = 8x0.3 + 4x0.5 + 1x0.2 = 4.6 million hours per day 



Waiting time: 15 minsPickup time: 10 minsRiding time: 30 minsDrop-off time: 5 mins

Waiting time: 15 mins

Pickup time: 10 mins

Riding time: 30 mins

Drop-off time: 5 mins

Total time per ride = 1 hour

Total Number of Rides = (# of drivers) x (# of hours per driver) x (# of rides per hour)

= 4.6 million rides per day





Share this post with a friendSince you liked this post, why not share it to help spread the word?Share