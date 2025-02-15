# How would you evaluate the success of a Payment Gateway Product?

*Source: https://www.mypminterview.com/p/success-metrics-of-payment-gateway-product*

---

Evaluate the success of a Payment Gateway Product? - PM Interview

Top Product Manager Interview Question - Asked at PayTM, Stripe, Razorpay, Paypal, PayU and more . . .

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share







Why are Product Metrics Questions asked?



Product Metric Interview Questions are frequently asked by interviewers during Product Management interviews to gauge your aptitude on whether you are able to properly, identify the key metrics that would help analyze a feature’s performance and its impact on the business, the users, and the product.



Common Mistakes to avoid:

Not describing the product, the feature, its goals and directly jumping into defining the metrics.Not giving a structured answer and defining generic metrics. (e.g. I would check if the users are using the feature or not).

Not describing the product, the feature, its goals and directly jumping into defining the metrics.

Not giving a structured answer and defining generic metrics. (e.g. I would check if the users are using the feature or not).



How to Answer a Product Metrics Question?



The key to correctly answering a Product Metric Question is following a structured framework.

Here is a step-by-step framework, you can follow while answering Product Metrics questions in Product Management Interviews :

Describe the Product. (P)Describe the Feature. (F)Define the feature Goals you want to achieve (G)Describe the User Journey of the feature (J)Define the Metrics for each step of the User Journey (M)Evaluate and Prioritize the Metrics. (E)Summarize your answer (S)

Describe the Product. (P)

Describe the Feature. (F)

Define the feature Goals you want to achieve (G)

Describe the User Journey of the feature (J)

Define the Metrics for each step of the User Journey (M)

Evaluate and Prioritize the Metrics. (E)

Summarize your answer (S)



Clarifying Questions



Q) Is the service provider a bank itself or a third-party platform?

A) It’s a third-party platform that has integration with banks and merchants.



Describe the Product:



A payment gateway is a service or product that makes it simple for customers to pay a certain retailer or platform.

Customers are given the option to select their preferred payment method through the payment gateway, which also makes life easier for platforms and merchants by offering payment as a service (which otherwise they would have to build on their own).

The payment processor receives the payment information (such as credit card or debit card details) that the payment gateway has collected. Communication between the payment processor, credit card issuers, and merchant-acquiring banks is also made easier by the payment gateway.

The payment processor authorises card data, looks out for fraud, and transfers money from the client to the merchant bank.

Finally, it informs the payment gateway if the request has been authorised or rejected. 





Goal: 



Generally the goal of a payment gateway business is to maximize revenue which can be achieved by: Maximizing the volume of transactions or Maximizing payment volume.





User Journey:



The customer typically follows these steps to make a payment via Payment Gateway on the merchant site,

Starts the payment process on the retailer's website.Selects a chosen payment method (bank account, credit card, debit card etc.)Gets a list of the payment gateways that are readily available.Selects a payment gateway (if there are multiple options available)Payment started.Performs the next steps in accordance with the payment method.Receives payment confirmation. (approved or rejected.)

Starts the payment process on the retailer's website.

Selects a chosen payment method (bank account, credit card, debit card etc.)

Gets a list of the payment gateways that are readily available.

Selects a payment gateway (if there are multiple options available)

Payment started.

Performs the next steps in accordance with the payment method.

Receives payment confirmation. (approved or rejected.)



Users for the payment gateway can be divided into 2 segments:

Consumers or end users.Merchants/Products/Platforms.

Consumers or end users.

Merchants/Products/Platforms.



Assumptions:



Out of scope:

Tools, products, and the onboarding process for merchants.Detailed technical metrics.Metrics related to integration with payment partners.

Tools, products, and the onboarding process for merchants.

Detailed technical metrics.

Metrics related to integration with payment partners.





List of Metrics:



Acquisition: # of users accessing the payment gateway (While this is dependent on the merchant, but this number should keep on growing). (P2)Activation: # of users completing their first payment. (P1)Retention:# of users storing payment/CC info for future use. (P3)# of users selecting the payment gateway on products having multiple payment gateways. (P1)(While this is also dependent on the merchant)Revenue: ARPU (Average Revenue Per User) (P0)Total Revenue generated. (P0)

Acquisition: # of users accessing the payment gateway (While this is dependent on the merchant, but this number should keep on growing). (P2)

Activation: # of users completing their first payment. (P1)

Retention:

# of users storing payment/CC info for future use. (P3)# of users selecting the payment gateway on products having multiple payment gateways. (P1)(While this is also dependent on the merchant)

# of users storing payment/CC info for future use. (P3)

# of users selecting the payment gateway on products having multiple payment gateways. (P1)(While this is also dependent on the merchant)

Revenue: 

ARPU (Average Revenue Per User) (P0)Total Revenue generated. (P0)

ARPU (Average Revenue Per User) (P0)

Total Revenue generated. (P0)



Acquisition: # of Merchants/Products using the payment gateway.(Directly tied to revenue. Marketing effort involved and need to support multiple backend integrations) (P0)Activation:The total number of transactions completed. (P0)# of transactions completed per merchant. (P0)Retention: # of merchants renewing the contract/repeat merchants. (P0)# of Transacting Merchants - WoW, MoM.Referral: # of leads received via referral from existing merchants. (P1)Revenue: # Total Revenue Share Earned per Merchant. (I am assuming payment gateways take a revenue share of total transactions happening through their platform) (P0)LifeTime Value (LTV) per Merchant. (P1)Customer Acquisition Cost / LTV. (P1)

Acquisition: # of Merchants/Products using the payment gateway.(Directly tied to revenue. Marketing effort involved and need to support multiple backend integrations) (P0)

Activation:

The total number of transactions completed. (P0)# of transactions completed per merchant. (P0)

The total number of transactions completed. (P0)

# of transactions completed per merchant. (P0)

Retention: 

# of merchants renewing the contract/repeat merchants. (P0)# of Transacting Merchants - WoW, MoM.

# of merchants renewing the contract/repeat merchants. (P0)

# of Transacting Merchants - WoW, MoM.

Referral: # of leads received via referral from existing merchants. (P1)

Revenue: 

# Total Revenue Share Earned per Merchant. (I am assuming payment gateways take a revenue share of total transactions happening through their platform) (P0)LifeTime Value (LTV) per Merchant. (P1)Customer Acquisition Cost / LTV. (P1)

# Total Revenue Share Earned per Merchant. (I am assuming payment gateways take a revenue share of total transactions happening through their platform) (P0)

LifeTime Value (LTV) per Merchant. (P1)

Customer Acquisition Cost / LTV. (P1)



# of Transactions hitting the payment gateway after a submit or checkout. (P2)# of Transactions reaching the financial institutions. (P2)Average time (in milliseconds) for the transaction to reach the gateway. (P2)(An important metric for customer experience)Average time (in milliseconds) for reaching the financial institution. (P2)(Directly tied to timeout of transaction metric)# of responses from the financial institution (positive vs denied). (P2)# of Timeout transactions. (P1)# of Cancelled Transactions. (Cancelled by user). (P1)# of Failed Transactions. (P0)% of fraud-tagged transactions. (Actual Vs False Negative). (P1)# of Headless Transactions. (Rollback transactions at the backend but frontend transaction went through) (P1)# of Transaction responses being sent back to POS. (P2)Transaction Amounts. (Higher amounts and histograms signal higher trust and reliability.) (P2)Commission/Fee paid to financial institutions - per Transaction and Cumulative. (P3)# of protocols (Secure) and Security formats supported (like MFA - Multi-Factor Authentication). # of customers signing up for MFA support. (P3)

# of Transactions hitting the payment gateway after a submit or checkout. (P2)

# of Transactions reaching the financial institutions. (P2)

Average time (in milliseconds) for the transaction to reach the gateway. (P2)(An important metric for customer experience)

Average time (in milliseconds) for reaching the financial institution. (P2)(Directly tied to timeout of transaction metric)

# of responses from the financial institution (positive vs denied). (P2)

# of Timeout transactions. (P1)

# of Cancelled Transactions. (Cancelled by user). (P1)

# of Failed Transactions. (P0)

% of fraud-tagged transactions. (Actual Vs False Negative). (P1)

# of Headless Transactions. (Rollback transactions at the backend but frontend transaction went through) (P1)

# of Transaction responses being sent back to POS. (P2)

Transaction Amounts. (Higher amounts and histograms signal higher trust and reliability.) (P2)

Commission/Fee paid to financial institutions - per Transaction and Cumulative. (P3)

# of protocols (Secure) and Security formats supported (like MFA - Multi-Factor Authentication). # of customers signing up for MFA support. (P3)





From the list of metrics mentioned above, if I have to monitor just a few, I would track the,

# of unsuccessful transactions (per merchant) & Total Revenue generated (per merchant)- Monitoring this would ensure that the business/product is growing.# of unsuccessful transactions - This is directly tied to customer experience and retention. It can be due to,Canceled by customer.Transaction failure at bank due to technical failure.Transaction denied due to risk.

# of unsuccessful transactions (per merchant) & Total Revenue generated (per merchant)- Monitoring this would ensure that the business/product is growing.

# of unsuccessful transactions - This is directly tied to customer experience and retention. It can be due to,

Canceled by customer.Transaction failure at bank due to technical failure.Transaction denied due to risk.

Canceled by customer.

Transaction failure at bank due to technical failure.

Transaction denied due to risk.



Summary:



Therefore, in order to assess the performance of a payment gateway product, I will first divide all metrics to determine which are pertinent to the various stages of the user journey.Implementation and tracking of the metrics will be based on the defined priority.

If these indicators rise, it will be a sign of success; if they fall, more research is needed to retain existing customers and acquire new ones.

Share this post with a friendSince you liked this post, why not share it to help spread the word?Share