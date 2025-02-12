# What were the data pipeline challenges on your last AI project?

*Source: https://www.mypminterview.com/p/ai-app-to-detech-acne-severity*

---

#### Share this post

# What were the data pipeline challenges on your last AI project?

### Explain the data pipeline for the last AI project you worked on. What were the top challenges in getting data, and how did you resolve them?

#### Share this post

[Share](https://www.mypminterview.com/p/ai-app-to-detech-acne-severity?utm_source=substack&utm_medium=email&utm_content=share&action=share)

In my last project, which had an AI application, we developed a consumer application aimed at addressing the severity of acne through a simple selfie image. The primary goal of this application was to provide users with an immediate prognosis of their acne condition and recommend appropriate treatments or suggest visiting a specialist. This project not only leveraged advanced machine-learning techniques but also incorporated domain expertise from dermatologists to ensure accurate and actionable results for users.



## 1. Describe the Product:



The Acne Severity Prediction App is a consumer-focused mobile application designed to assess the severity of acne from a selfie image and provide personalized recommendations for treatment. It leverages advanced machine learning algorithms and image processing techniques to analyze facial images and determine the level of acne severity. The app aims to empower users by providing them with actionable insights and recommendations, potentially reducing the need for in-person dermatological consultations.

Key Features:

1. Acne Severity Analysis:Users can upload a selfie, and the app will analyze the image to determine the severity of acne. The analysis is based on a scale ranging from mild to severe, providing a detailed assessment of acne conditions.
2. Users can upload a selfie, and the app will analyze the image to determine the severity of acne. The analysis is based on a scale ranging from mild to severe, providing a detailed assessment of acne conditions.
3. Personalized Treatment Recommendations:Based on the severity of acne detected, the app offers personalized treatment suggestions. These may include over-the-counter products, skincare routines, or recommendations to consult a specialist.
4. Based on the severity of acne detected, the app offers personalized treatment suggestions. These may include over-the-counter products, skincare routines, or recommendations to consult a specialist.
5. Daily Prognosis:Users who upload daily images can receive a prognosis of their acne condition over time. This feature helps users track the effectiveness of treatments and monitor changes in their skin condition.
6. Users who upload daily images can receive a prognosis of their acne condition over time. This feature helps users track the effectiveness of treatments and monitor changes in their skin condition.
7. User Feedback Integration:Users can rate the relevance of the app’s suggestions and provide feedback. This feedback loop is crucial for iterative improvement of the recommendation algorithms.
8. Users can rate the relevance of the app’s suggestions and provide feedback. This feedback loop is crucial for iterative improvement of the recommendation algorithms.

Acne Severity Analysis:

* Users can upload a selfie, and the app will analyze the image to determine the severity of acne. The analysis is based on a scale ranging from mild to severe, providing a detailed assessment of acne conditions.

Users can upload a selfie, and the app will analyze the image to determine the severity of acne. The analysis is based on a scale ranging from mild to severe, providing a detailed assessment of acne conditions.

Personalized Treatment Recommendations:

* Based on the severity of acne detected, the app offers personalized treatment suggestions. These may include over-the-counter products, skincare routines, or recommendations to consult a specialist.

Based on the severity of acne detected, the app offers personalized treatment suggestions. These may include over-the-counter products, skincare routines, or recommendations to consult a specialist.

Daily Prognosis:

* Users who upload daily images can receive a prognosis of their acne condition over time. This feature helps users track the effectiveness of treatments and monitor changes in their skin condition.

Users who upload daily images can receive a prognosis of their acne condition over time. This feature helps users track the effectiveness of treatments and monitor changes in their skin condition.

User Feedback Integration:

* Users can rate the relevance of the app’s suggestions and provide feedback. This feedback loop is crucial for iterative improvement of the recommendation algorithms.

Users can rate the relevance of the app’s suggestions and provide feedback. This feedback loop is crucial for iterative improvement of the recommendation algorithms.



## 2. User Segments:



1. Young Adults and Teenagers:Primary users concerned with acne, looking for quick and reliable ways to assess their skin condition.Likely to seek guidance on whether to use over-the-counter treatments or visit a dermatologist.
2. Primary users concerned with acne, looking for quick and reliable ways to assess their skin condition.
3. Likely to seek guidance on whether to use over-the-counter treatments or visit a dermatologist.
4. Parents of Teenagers:Secondary users who might use the app to monitor and manage their teenagers' acne condition.Interested in ensuring their children receive appropriate care and treatment.
5. Secondary users who might use the app to monitor and manage their teenagers' acne condition.
6. Interested in ensuring their children receive appropriate care and treatment.
7. Dermatology Patients:Individuals already consulting dermatologists who want to track their acne progress between visits.Looking for continuous monitoring and personalized treatment recommendations.
8. Individuals already consulting dermatologists who want to track their acne progress between visits.
9. Looking for continuous monitoring and personalized treatment recommendations.
10. Dermatologists and Healthcare Providers:Professionals who can use the app to supplement their diagnosis and treatment plans.May use the app to monitor patient progress remotely and adjust treatment plans accordingly.
11. Professionals who can use the app to supplement their diagnosis and treatment plans.
12. May use the app to monitor patient progress remotely and adjust treatment plans accordingly.
13. Skincare Product Companies:Companies interested in understanding user needs and preferences for developing targeted acne treatment products.May use anonymized data insights for market research and product development.
14. Companies interested in understanding user needs and preferences for developing targeted acne treatment products.
15. May use anonymized data insights for market research and product development.

Young Adults and Teenagers:

* Primary users concerned with acne, looking for quick and reliable ways to assess their skin condition.
* Likely to seek guidance on whether to use over-the-counter treatments or visit a dermatologist.

Primary users concerned with acne, looking for quick and reliable ways to assess their skin condition.

Likely to seek guidance on whether to use over-the-counter treatments or visit a dermatologist.

Parents of Teenagers:

* Secondary users who might use the app to monitor and manage their teenagers' acne condition.
* Interested in ensuring their children receive appropriate care and treatment.

Secondary users who might use the app to monitor and manage their teenagers' acne condition.

Interested in ensuring their children receive appropriate care and treatment.

Dermatology Patients:

* Individuals already consulting dermatologists who want to track their acne progress between visits.
* Looking for continuous monitoring and personalized treatment recommendations.

Individuals already consulting dermatologists who want to track their acne progress between visits.

Looking for continuous monitoring and personalized treatment recommendations.

Dermatologists and Healthcare Providers:

* Professionals who can use the app to supplement their diagnosis and treatment plans.
* May use the app to monitor patient progress remotely and adjust treatment plans accordingly.

Professionals who can use the app to supplement their diagnosis and treatment plans.

May use the app to monitor patient progress remotely and adjust treatment plans accordingly.

Skincare Product Companies:

* Companies interested in understanding user needs and preferences for developing targeted acne treatment products.
* May use anonymized data insights for market research and product development.

Companies interested in understanding user needs and preferences for developing targeted acne treatment products.

May use anonymized data insights for market research and product development.



## 3. Data Pipeline Overview:



The data pipeline for our acne severity prediction app was designed to handle various stages from data collection to model deployment, ensuring a seamless flow of data through the system. Below are the key components of the data pipeline:



### a. Data Collection & Labelling



1. Clinical Images of Acne:High-resolution images were collected depicting various stages and severities of acne lesions on different skin types. These images serve as the primary input for training the model to recognize and assess acne severity.
2. High-resolution images were collected depicting various stages and severities of acne lesions on different skin types. These images serve as the primary input for training the model to recognize and assess acne severity.
3. Demographic and Metadata:Additional data such as age, gender, skin type, and any relevant medical history may have been collected to provide context and aid in personalized recommendations.
4. Additional data such as age, gender, skin type, and any relevant medical history may have been collected to provide context and aid in personalized recommendations.

Clinical Images of Acne:

* High-resolution images were collected depicting various stages and severities of acne lesions on different skin types. These images serve as the primary input for training the model to recognize and assess acne severity.

High-resolution images were collected depicting various stages and severities of acne lesions on different skin types. These images serve as the primary input for training the model to recognize and assess acne severity.

Demographic and Metadata:

* Additional data such as age, gender, skin type, and any relevant medical history may have been collected to provide context and aid in personalized recommendations.

Additional data such as age, gender, skin type, and any relevant medical history may have been collected to provide context and aid in personalized recommendations.

Regarding the sources or repositories used for data collection:

1. Clinical Databases:Data have been sourced from clinical databases containing anonymized images and patient information, obtained with consent for research and training purposes.
2. Data have been sourced from clinical databases containing anonymized images and patient information, obtained with consent for research and training purposes.
3. Dermatology Clinics and Practices:Collaboration with dermatology clinics or practices has provided access to diverse clinical images and patient data.
4. Collaboration with dermatology clinics or practices has provided access to diverse clinical images and patient data.
5. Research Institutions:Academic research institutions specializing in dermatology have contributed datasets to train the model.
6. Academic research institutions specializing in dermatology have contributed datasets to train the model.

Clinical Databases:

* Data have been sourced from clinical databases containing anonymized images and patient information, obtained with consent for research and training purposes.

Data have been sourced from clinical databases containing anonymized images and patient information, obtained with consent for research and training purposes.

Dermatology Clinics and Practices:

* Collaboration with dermatology clinics or practices has provided access to diverse clinical images and patient data.

Collaboration with dermatology clinics or practices has provided access to diverse clinical images and patient data.

Research Institutions:

* Academic research institutions specializing in dermatology have contributed datasets to train the model.

Academic research institutions specializing in dermatology have contributed datasets to train the model.

The data labelling process involved assigning severity labels to each image, indicating the extent and severity of acne present. Contributors involved in the labelling process  include:

1. Dermatologists:Experienced dermatologists with expertise in diagnosing and grading acne lesions have been involved in labelling the images. Their clinical judgment and expertise ensure accurate and consistent labelling.
2. Experienced dermatologists with expertise in diagnosing and grading acne lesions have been involved in labelling the images. Their clinical judgment and expertise ensure accurate and consistent labelling.
3. Medical Professionals:Other medical professionals, such as dermatology residents or healthcare providers with training in dermatology, have contributed to the labelling process under the supervision of experienced dermatologists.
4. Other medical professionals, such as dermatology residents or healthcare providers with training in dermatology, have contributed to the labelling process under the supervision of experienced dermatologists.
5. Data Annotation Teams:In some cases, dedicated data annotation teams or services specializing in medical image labelling have been employed to label the dataset efficiently.
6. In some cases, dedicated data annotation teams or services specializing in medical image labelling have been employed to label the dataset efficiently.
7. Quality Assurance Checks:Quality assurance checks have been conducted to ensure the accuracy and consistency of labelling across the dataset. This involves reviewing a subset of labelled images to identify and correct any discrepancies or errors.
8. Quality assurance checks have been conducted to ensure the accuracy and consistency of labelling across the dataset. This involves reviewing a subset of labelled images to identify and correct any discrepancies or errors.

Dermatologists:

* Experienced dermatologists with expertise in diagnosing and grading acne lesions have been involved in labelling the images. Their clinical judgment and expertise ensure accurate and consistent labelling.

Experienced dermatologists with expertise in diagnosing and grading acne lesions have been involved in labelling the images. Their clinical judgment and expertise ensure accurate and consistent labelling.

Medical Professionals:

* Other medical professionals, such as dermatology residents or healthcare providers with training in dermatology, have contributed to the labelling process under the supervision of experienced dermatologists.

Other medical professionals, such as dermatology residents or healthcare providers with training in dermatology, have contributed to the labelling process under the supervision of experienced dermatologists.

Data Annotation Teams:

* In some cases, dedicated data annotation teams or services specializing in medical image labelling have been employed to label the dataset efficiently.

In some cases, dedicated data annotation teams or services specializing in medical image labelling have been employed to label the dataset efficiently.

Quality Assurance Checks:

* Quality assurance checks have been conducted to ensure the accuracy and consistency of labelling across the dataset. This involves reviewing a subset of labelled images to identify and correct any discrepancies or errors.

Quality assurance checks have been conducted to ensure the accuracy and consistency of labelling across the dataset. This involves reviewing a subset of labelled images to identify and correct any discrepancies or errors.



### b. Data Processing and Cleaning



To ensure the data used for training the acne severity prediction model is of high quality and consistency, several preprocessing steps were taken to clean and prepare the data. Here are the preprocessing steps, along with potential issues encountered during data cleaning:

1. Image Preprocessing:Resizing and Cropping: Images have been resized to a standardized resolution and cropped to focus on the facial region containing acne lesions.Normalization: Normalizing image pixel values to a consistent scale can help reduce variation due to differences in lighting conditions and camera settings.
2. Resizing and Cropping: Images have been resized to a standardized resolution and cropped to focus on the facial region containing acne lesions.
3. Normalization: Normalizing image pixel values to a consistent scale can help reduce variation due to differences in lighting conditions and camera settings.
4. Data Augmentation:Techniques such as rotation, flipping, zooming, and adding noise to images have been applied to augment the dataset, increasing its diversity and robustness.
5. Techniques such as rotation, flipping, zooming, and adding noise to images have been applied to augment the dataset, increasing its diversity and robustness.
6. Handling Missing Values:Some images or associated metadata have missing values, possibly due to data collection errors or technical issues.Common approaches to handling missing values include imputation techniques such as mean, median, or mode imputation, or excluding incomplete samples from the dataset if they are too numerous.
7. Some images or associated metadata have missing values, possibly due to data collection errors or technical issues.
8. Common approaches to handling missing values include imputation techniques such as mean, median, or mode imputation, or excluding incomplete samples from the dataset if they are too numerous.
9. Dealing with Inconsistent Formats:Images or metadata have been stored in different formats or structures, leading to inconsistencies in data representation.Data cleaning involved standardizing formats across the dataset, converting data into a consistent format suitable for model training.
10. Images or metadata have been stored in different formats or structures, leading to inconsistencies in data representation.
11. Data cleaning involved standardizing formats across the dataset, converting data into a consistent format suitable for model training.
12. Quality Control:Quality control checks have been performed to identify and remove low-quality images or data points that do not meet predefined criteria for inclusion in the dataset.This could involve manual inspection by domain experts or automated algorithms designed to detect outliers or anomalies.
13. Quality control checks have been performed to identify and remove low-quality images or data points that do not meet predefined criteria for inclusion in the dataset.
14. This could involve manual inspection by domain experts or automated algorithms designed to detect outliers or anomalies.
15. Addressing Class Imbalance:The dataset exhibit class imbalance, with certain severity levels of acne being overrepresented or underrepresented.Techniques such as oversampling, undersampling, or using class-weighted loss functions have been employed to mitigate the effects of class imbalance during model training.
16. The dataset exhibit class imbalance, with certain severity levels of acne being overrepresented or underrepresented.
17. Techniques such as oversampling, undersampling, or using class-weighted loss functions have been employed to mitigate the effects of class imbalance during model training.
18. Data Splitting:The dataset has been split into training, validation, and testing sets to evaluate model performance and prevent overfitting.Stratified sampling techniques have been used to ensure that each severity level is represented proportionally in each data split.
19. The dataset has been split into training, validation, and testing sets to evaluate model performance and prevent overfitting.
20. Stratified sampling techniques have been used to ensure that each severity level is represented proportionally in each data split.
21. Feature Engineering:Additional features such as texture descriptors, color histograms, or facial landmarks have been extracted from the images to augment the dataset and improve model performance.
22. Additional features such as texture descriptors, color histograms, or facial landmarks have been extracted from the images to augment the dataset and improve model performance.

Image Preprocessing:

* Resizing and Cropping: Images have been resized to a standardized resolution and cropped to focus on the facial region containing acne lesions.
* Normalization: Normalizing image pixel values to a consistent scale can help reduce variation due to differences in lighting conditions and camera settings.

Resizing and Cropping: Images have been resized to a standardized resolution and cropped to focus on the facial region containing acne lesions.

Normalization: Normalizing image pixel values to a consistent scale can help reduce variation due to differences in lighting conditions and camera settings.

Data Augmentation:

* Techniques such as rotation, flipping, zooming, and adding noise to images have been applied to augment the dataset, increasing its diversity and robustness.

Techniques such as rotation, flipping, zooming, and adding noise to images have been applied to augment the dataset, increasing its diversity and robustness.

Handling Missing Values:

* Some images or associated metadata have missing values, possibly due to data collection errors or technical issues.
* Common approaches to handling missing values include imputation techniques such as mean, median, or mode imputation, or excluding incomplete samples from the dataset if they are too numerous.

Some images or associated metadata have missing values, possibly due to data collection errors or technical issues.

Common approaches to handling missing values include imputation techniques such as mean, median, or mode imputation, or excluding incomplete samples from the dataset if they are too numerous.

Dealing with Inconsistent Formats:

* Images or metadata have been stored in different formats or structures, leading to inconsistencies in data representation.
* Data cleaning involved standardizing formats across the dataset, converting data into a consistent format suitable for model training.

Images or metadata have been stored in different formats or structures, leading to inconsistencies in data representation.

Data cleaning involved standardizing formats across the dataset, converting data into a consistent format suitable for model training.

Quality Control:

* Quality control checks have been performed to identify and remove low-quality images or data points that do not meet predefined criteria for inclusion in the dataset.
* This could involve manual inspection by domain experts or automated algorithms designed to detect outliers or anomalies.

Quality control checks have been performed to identify and remove low-quality images or data points that do not meet predefined criteria for inclusion in the dataset.

This could involve manual inspection by domain experts or automated algorithms designed to detect outliers or anomalies.

Addressing Class Imbalance:

* The dataset exhibit class imbalance, with certain severity levels of acne being overrepresented or underrepresented.
* Techniques such as oversampling, undersampling, or using class-weighted loss functions have been employed to mitigate the effects of class imbalance during model training.

The dataset exhibit class imbalance, with certain severity levels of acne being overrepresented or underrepresented.

Techniques such as oversampling, undersampling, or using class-weighted loss functions have been employed to mitigate the effects of class imbalance during model training.

Data Splitting:

* The dataset has been split into training, validation, and testing sets to evaluate model performance and prevent overfitting.
* Stratified sampling techniques have been used to ensure that each severity level is represented proportionally in each data split.

The dataset has been split into training, validation, and testing sets to evaluate model performance and prevent overfitting.

Stratified sampling techniques have been used to ensure that each severity level is represented proportionally in each data split.

Feature Engineering:

* Additional features such as texture descriptors, color histograms, or facial landmarks have been extracted from the images to augment the dataset and improve model performance.

Additional features such as texture descriptors, color histograms, or facial landmarks have been extracted from the images to augment the dataset and improve model performance.

During the data cleaning process, common issues encountered may include:

* Identifying and handling outliers or anomalies in the dataset.
* Resolving inconsistencies or discrepancies in labeling or metadata.
* Ensuring data privacy and compliance with regulations when handling sensitive patient information.
* Balancing the trade-off between data quality and computational resources required for processing large datasets.

Identifying and handling outliers or anomalies in the dataset.

Resolving inconsistencies or discrepancies in labeling or metadata.

Ensuring data privacy and compliance with regulations when handling sensitive patient information.

Balancing the trade-off between data quality and computational resources required for processing large datasets.



### c. Data Storage and Management

## This post is for paid subscribers

