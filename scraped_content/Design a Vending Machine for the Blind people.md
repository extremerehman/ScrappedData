# Design a Vending Machine for the Blind people

*Source: https://www.mypminterview.com/p/design-a-vending-machine-for-the-blind-people*

---

Design a Vending Machine for the Blind people

Product Design Case Study: Design a Vending Machine for the Visually Impaired

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share



Goal

Our goal is to design a vending machine that is accessible, simple, and offers a frictionless experience for blind people. We want to ensure that our vending machine addresses the key pain points of blind people while supporting a variety of language types.

Vision

We believe that in the future we can personalize the vending machine experience for each user. With speech recognition models, we can start to answer complex queries for users about the quantity of the remaining items and offer discounts to upsell the customer. Our goal is to make sure users actually enjoy using the vending machine and, as a result,  start transacting more. This vision will ensure we create a vending machine that is delightful to interact with and help us solidify a  strong brand amongst the blind community.

User Personas:



Below we paint a picture of our target users through a set of user personas:



Dan is 35 years old. He has been blind since birth, but is employed and has a positive attitude. He lives with a friend of his and currently works as an engineer at a big public corporation. Safety is important to Dan.

Pain Points:  Dan is frustrated about how he can drop his card while inserting it into a vending machine. Dan is worried someone might steal his card when he takes it out. Dan dislikes having to debug issues with the vending machine (e.g. no remaining items), and doesn’t know what’s inside if the vending machine doesn’t include braille.

Goals:  Dan wants to be able to use the vending machine without fear of safety. Dan wants to minimize the number of times he inputs various details on the machine. Dan wants the vending machine to communicate with him more clearly about the availability of different items.

Melinda is 60 years old and she lost her eyesight due to macular degeneration.  She retired from work and lives at a retirement home. Melinda also immigrated from China and cannot communicate in English. She is not very technically competent and struggles to use complex products.

Pain Points:  Melinda is frustrated by how most vending machines in America do not support the Chinese. Melinda in general is frustrated by vending machines -  she hasn’t used them until moving into her new retirement home, so they’re less common for her to interact with. Melinda also is frustrated by how she might press the wrong buttons and get the wrong vending machine item.

Goals: Melinda wants her vending machine to be able to support Chinese and additional languages. Melinda wants the process of getting items from a vending machine to be a lot more simple as she feels it’s too complex. Melinda wants to ensure that the vending machine is able to offer a clear confirmation message to her about what she’s received.

Use Cases:

Below is a list of some common use cases to get a better understanding of the key functionality we need to provide:

Inserting money: A user can insert money either via a credit card payment or cash payment.Browsing items:  A user can browse the items in the vending machine by perusing a window where all the items are featured, or a series of panels with images of the item.Selecting item: Via a series of buttons, a user can click the letter and number combination that corresponds to the item they desire.Collecting item: The machine drops the selected item and leaves it in a bottom cartridge for the user to pick up.

Inserting money: A user can insert money either via a credit card payment or cash payment.

Browsing items:  A user can browse the items in the vending machine by perusing a window where all the items are featured, or a series of panels with images of the item.

Selecting item: Via a series of buttons, a user can click the letter and number combination that corresponds to the item they desire.

Collecting item: The machine drops the selected item and leaves it in a bottom cartridge for the user to pick up.

Takeaways:

User Focus:  In general, the early adopters of our system are more likely to be similar to Dan. Most blind users who have a certain degree of technical competence are less likely to seek external help or assistance while using vending machines.Pain Points: The general pain points worth focusing on are around reducing the number of user inputs, supporting people of all language types, and providing easy access to browsing items (a core part of the vending machine experience).Use Cases: In terms of use cases,  we should focus on browsing and selecting. Inserting money and collecting items are already common use cases that blind individuals navigate with a variety of machines (e.g. an ATM, ticket machine).

User Focus:  In general, the early adopters of our system are more likely to be similar to Dan. Most blind users who have a certain degree of technical competence are less likely to seek external help or assistance while using vending machines.

Pain Points: The general pain points worth focusing on are around reducing the number of user inputs, supporting people of all language types, and providing easy access to browsing items (a core part of the vending machine experience).

Use Cases: In terms of use cases,  we should focus on browsing and selecting. Inserting money and collecting items are already common use cases that blind individuals navigate with a variety of machines (e.g. an ATM, ticket machine).

Refined Vision:

Instead of a vending machine, we refine our vision to create self-serviced mini-stores. With our new vision, people can access their on-the-go essentials and treats with a fun, accessible device. We predict the upfront investment in a better device will payout over the long run with increased sales and higher margins on the costs of goods sold.

Based on all of these factors, our hypothesis is that our new-age vending machine should be voice-assisted. This experience will not only benefit the blind user but also create a smoother high-tech experience for the non-blind user. Adding voice capabilities allows for opportunities to make the device more friendly and delightful, which will in turn also help boost sales.

Next, we’ll discuss what our device actually looks like.

Design and User Experience:



Objectives: While designing our vending machine, the key areas we are going to focus on are:

Reducing user friction and keypad-based inputProviding support for multiple languagesDelivering a simple user experienceEnsuring our system is functional for non-blind users as well, as the vending machine will be used by both parties.

Reducing user friction and keypad-based input

Providing support for multiple languages

Delivering a simple user experience

Ensuring our system is functional for non-blind users as well, as the vending machine will be used by both parties.



Assumptions: Below is a list of some assumptions about what users need to be aware of before interacting with our system.

The name of the friendly and more accessible vending machine is Vince.To initialize the system, they must speak with the system and say “Start order” or “Hello Vince” in their respective language.If the user’s language is not identified then we send an error sound and inform the user in English of the supported languages we provide. If the errors continue, the vending machine will default its behavior to that of a non-blind accessible vending machine. Here we assume that users are aware that a lack of confirmation message signals that they need to interact with the machine as they would a normal vending machine.

The name of the friendly and more accessible vending machine is Vince.

To initialize the system, they must speak with the system and say “Start order” or “Hello Vince” in their respective language.

If the user’s language is not identified then we send an error sound and inform the user in English of the supported languages we provide. If the errors continue, the vending machine will default its behavior to that of a non-blind accessible vending machine. Here we assume that users are aware that a lack of confirmation message signals that they need to interact with the machine as they would a normal vending machine.

User Journeys

Here is the user flow in our new vending machine experience. The user can conduct all the voice interactions through the vending machine’s speakers.

Step 1: Initialization 

Default state: The default of the state of the machine is to include some flashing lights and soft ambient music. This helps to attract users to the device.Voice  Activated initialization: The user first comes to the vending machine and says “Begin order” or “Hello Lisa” in their respective language. The vending machine then analyzes their voice and deciphers what language they are speaking in. If the language cannot be identified, an error sequence as mentioned above is initiated.Card Insert initialization: If the user is not aware that they can use the voice-activated option, they can insert their card. When the system attempts to retrieve details from their origin bank, it could also potentially identify the country and language of origin for the user.

Default state: The default of the state of the machine is to include some flashing lights and soft ambient music. This helps to attract users to the device.

Voice  Activated initialization: The user first comes to the vending machine and says “Begin order” or “Hello Lisa” in their respective language. The vending machine then analyzes their voice and deciphers what language they are speaking in. If the language cannot be identified, an error sequence as mentioned above is initiated.

Card Insert initialization: If the user is not aware that they can use the voice-activated option, they can insert their card. When the system attempts to retrieve details from their origin bank, it could also potentially identify the country and language of origin for the user.

Step 2: Specifying Transaction options

Our  Voice assistant, Vince, then begins communicating with the user in the language of their choice. It first asks them which of the following  options they would be interested in:

List Beverages — this will list the beverage options and the price of each of them.List Snacks — this will list the snack options and the price of each of them.Balance — this will read out the amount of money currently inserted into the machineCancel  — this will end the conversation if the user no longer wants an item.  This option is automatically selected after a minute of inactivity.

List Beverages — this will list the beverage options and the price of each of them.

List Snacks — this will list the snack options and the price of each of them.

Balance — this will read out the amount of money currently inserted into the machine

Cancel  — this will end the conversation if the user no longer wants an item.  This option is automatically selected after a minute of inactivity.

To select an option, the user simply has to state what they heard. The system will then fuzzy match the text to an option. It will then say, “I  heard you wanted ____, is that right?” This step is important to avoid unwanted items or items that sound phonetically similar.

If the system doesn’t clearly hear an option, it will list the options again and ask the user to state more clearly. After three failed attempts, the system will initiate the error sequence and eventually default to a  normal vending machine.

Step 3: Processing Purchase 

User states a beverage or snack option. The machine will respond “Ok,  processing your order.” and then “Your order is complete, please pick up  your item from the cartridge below (only if there is change) and your  change from the change box.” Music will play when the order is processing for delight as well as signaling to the user that the system is currently “loading” the beverage.After the purchase, the  machine will ask “Do you want to order anything else?” While initially,  this is a simple task, there’s an opportunity to improve this question in the future by saying suggesting good snack or beverage combinations,  like “Tostitos is a snack that goes really well with the water you just ordered. Would you like to buy a Tostitos for 20% off?”In general, we can also experiment with using sound cues to help the user identify where the items are located on the vending machine.

User states a beverage or snack option. The machine will respond “Ok,  processing your order.” and then “Your order is complete, please pick up  your item from the cartridge below (only if there is change) and your  change from the change box.” Music will play when the order is processing for delight as well as signaling to the user that the system is currently “loading” the beverage.

After the purchase, the  machine will ask “Do you want to order anything else?” While initially,  this is a simple task, there’s an opportunity to improve this question in the future by saying suggesting good snack or beverage combinations,  like “Tostitos is a snack that goes really well with the water you just ordered. Would you like to buy a Tostitos for 20% off?”

In general, we can also experiment with using sound cues to help the user identify where the items are located on the vending machine.

Mock-Ups



While normally we would include mockups for this design, since we’re designing a system for the blind, I propose that we focus on designing this product without an emphasis on visual details and instead stress test our system. Here’s a sample dialogue:

Vince: ambient musicUser: “Hello Vince” Vince: “Hi there! I hear that you’re speaking English.  It’s my pleasure to meet you! Would you like me to list the options in  the vending machine?” User: “Yes” Vince: “Great! Just say what you want from the following list: list beverages, list snacks, check your money balance, or cancel.” User: “List beverages” Vince: “I have coca-cola, sprite, and 7-up available in cans. They all cost $1. Just say the name of the beverage you’d like!” User: “Sprite” Vince: “I heard you wanted a ‘Sprite,’ is that right?” User: “Yes” Vince: “Great, you currently only have $0.25 in the machine. Please add $0.75 and say “done” when you’ve done so! The coin  slot is on the left of the machine.” User: adds money, says “done”. Vince: “Ok, processing your order” music “Your order is complete, please pick up your item from the cartridge below.  Let me know if you’d like to order a snack with that!”

Product Roadmap

To help prioritize features, we can use the below matrix that defines our product priority, the technical complexity, and the impact on the user.

Note:  With regards to priority, 1 refers to all features in our min-viable launch while 2s refer to features in our v2, and so on.



Competitive Advantage:

We plan to create product differentiation through these key areas:

Completely hands-free experience:  Our system offers a completely hands-free experience in a way that our competitors don’t. We rely on facial recognition for identification and voice for communication, which allows our users to conduct transactions without pressing any buttons on our ATM machine.Speech processing capabilities and personalization:  As our system gathers an increasing amount of speech data, we can start to flesh out our language model further. This will allow us to process complicated queries like “Do you have anything salty?”. In essence, we can start answering personalized queries for our users by building out a  more complex language model through the data we aggregate over time.  This will help build out our recommendation engine which we can use to upsell customers.Simplicity and a focus on the blind:  Our system is designed with a focus on blind individuals and simplicity. We can create an experience that is much simpler than our competitors, who suffer from feature bloat.

Completely hands-free experience:  Our system offers a completely hands-free experience in a way that our competitors don’t. We rely on facial recognition for identification and voice for communication, which allows our users to conduct transactions without pressing any buttons on our ATM machine.

Speech processing capabilities and personalization:  As our system gathers an increasing amount of speech data, we can start to flesh out our language model further. This will allow us to process complicated queries like “Do you have anything salty?”. In essence, we can start answering personalized queries for our users by building out a  more complex language model through the data we aggregate over time.  This will help build out our recommendation engine which we can use to upsell customers.

Simplicity and a focus on the blind:  Our system is designed with a focus on blind individuals and simplicity. We can create an experience that is much simpler than our competitors, who suffer from feature bloat.

Go-to-Market Strategy:

Launch Country: United States

Rationale:  Initially, we want to narrow our focus to the United States only since partnering with multiple vendors across different countries might be difficult. Although the United States might have a smaller blind population than certain countries like India, there is already a heavy investment into accessibility initiatives which makes adoption easier.  We’ll select our specific launch city based on the prevalence of sight-disabled individuals and openness to accessibility.

Marketing Tactics:

Branding:  Our marketing message should convey that Vince is delightfully designed with the blind in mind but usable by anyone. We should emphasize the fact that we are providing a completely hands-free vending machine experience with a few specific use cases in mind. Additionally, it is worth highlighting the simplicity of interacting with Lisa. Unlike our competitors, we want to narrow our scope to a limited set of features to remove the complexity out of vending machines. We’ll include a  face/mascot with Vince to solidify the personal, human aspect of the machine.Customer: We’ll start by targeting venue locations with existing vending machines, and offer a distribution of sales profits to the venue that out-competes existing vending machine—venue relationships. We’ll eventually expand into restaurants and apartment buildings, to put our vending machines alongside others.Marketing Channels:  We want to start publishing a set of articles on accessibility when it comes to device manufacturing. Our goal is to emerge as thought leaders in this space, so banks are aware of our deep domain knowledge when it comes to building systems for the blind. We’ll simultaneously pursue partnerships as a second channel. We’ll partner with key early adopter customers to promote the product and co-promote the venue as an accessibility-forward location.Interaction Guidance:  We want users to be aware of how to initialize and conduct a  transaction with Lisa. We should provide all venues with instruction manuals and a set of marketing emails, so they can help spread awareness on how users can interact with Vince.

Branding:  Our marketing message should convey that Vince is delightfully designed with the blind in mind but usable by anyone. We should emphasize the fact that we are providing a completely hands-free vending machine experience with a few specific use cases in mind. Additionally, it is worth highlighting the simplicity of interacting with Lisa. Unlike our competitors, we want to narrow our scope to a limited set of features to remove the complexity out of vending machines. We’ll include a  face/mascot with Vince to solidify the personal, human aspect of the machine.

Customer: We’ll start by targeting venue locations with existing vending machines, and offer a distribution of sales profits to the venue that out-competes existing vending machine—venue relationships. We’ll eventually expand into restaurants and apartment buildings, to put our vending machines alongside others.

Marketing Channels:  We want to start publishing a set of articles on accessibility when it comes to device manufacturing. Our goal is to emerge as thought leaders in this space, so banks are aware of our deep domain knowledge when it comes to building systems for the blind. We’ll simultaneously pursue partnerships as a second channel. We’ll partner with key early adopter customers to promote the product and co-promote the venue as an accessibility-forward location.

Interaction Guidance:  We want users to be aware of how to initialize and conduct a  transaction with Lisa. We should provide all venues with instruction manuals and a set of marketing emails, so they can help spread awareness on how users can interact with Vince.

Measuring Success:

In order to decide which metrics are best used to measure the success of our product, we will first specify our product goal and then list out the user actions that best support these goals. From there, we can decide which metrics best capture these actions.

Goals: Our product goal is to ensure that blind people can seamlessly conduct a  transaction on our vending machine without any frustration and minimal keypad input.

Actions:

Conversing with our system.Inserting cash.Browsing options.Ordering an option.

Conversing with our system.

Inserting cash.

Browsing options.

Ordering an option.

Metrics:

% of queries successfully processed by voice system.Examination of the user funnel (where do users give up on our system? Where does our system error?) by looking at retention rates across the user adoption funnel.The number of transactions completed per user.% of transactions successfully completed.Average time to complete a transaction.% monthly Retention of customers.

% of queries successfully processed by voice system.

Examination of the user funnel (where do users give up on our system? Where does our system error?) by looking at retention rates across the user adoption funnel.

The number of transactions completed per user.

% of transactions successfully completed.

Average time to complete a transaction.

% monthly Retention of customers.

Evaluation:  It is worth pointing that there are some potential pitfalls with these metrics. For instance % of queries successfully processed by the system is largely contingent on how sensible the user input is. Similarly, the number of transactions completed per user is largely dependent on the users’ needs. Perhaps in the winter, users abandon their queries more because it is cold. These considerations show that we need additional qualitative data to get further feedback about user sentiment for our product.

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share