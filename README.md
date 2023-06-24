# **Investigating Sentiment Patterns in Amazon Reviews: A look into the Entertainment Industry**

This repository contains the code and resources for the Investigating Sentiment Patterns in Amazon Reviews project, which focuses on analyzing users' sentiments towards different forms of entertainment based on Amazon reviews. The dataset used for this project is the Amazon Top 50 Movies, Books, and Games Reviews.

### **Contributors**

Authors: Ivan Chavez, Lane Whitmore, Uyen Pham

### **Project Objectives**

1. Collect Amazon review data for the top 50 movies, books, and games by implementing web scraping techniques such as the Selenium Framework. See ***web-scraper*** folder.
2. Analyze the collected review data to understand users' sentiments.
3. Apply Natural Language Processing (NLP) techniques such as stop word removal and tokenization for data processing.
4. Train and evaluate sentiment classification models based on the review star ratings.
5. Perform topic modeling on the review data to identify the main topics using Latent Dirichlet Allocation (LDA) and Non-Negative Matrix Factorization (NMF) techniques.
6. Implement the sentiment classification model and topic modeling into an application API for real-time sentiment analysis.
   The code for steps 2 to 6 can be found in the ***notebooks*** folder, while all the necessary functions are stored in the ***function*** folder. The trained models are pickled and stored in the ***models*** folder.
   
### **Dataset Description**

The dataset consists of individual CSV files for each product, containing the following information: review username, product title, review title, review body, rating (1-5 whole numbers only), and the date and place the product was reviewed from.

The review count for each product ranges from 14 to 8,000 reviews.

## **API Instructions**

See ***static*** for the styles and formatting of a web page and ***template*** for html set up. Samples in ***testing_data*** can be used to test the app.

### **Follow these instructions to set up and run the API:**

1. Clone the repository to your local machine.

2. Open a command line interface and navigate to the directory of the cloned repository.

3. Ensure that all dependencies are installed. If not use `pip install -r requirements.txt`

4. Run the following command to start the local server: `uvicorn main:app --reload`
5. Once the server is running, open your web browser and enter the following URL: http://127.0.0.1:8000
6. You will be directed to the API application interface. To analyze reviews, follow these steps:
   
     Enter the reviews in the input field provided. The reviews should be in the following format:
          <pre>
          Review 1
          ---
          Review 2
          ---
          Review n
          </pre>
     Click the "Submit" button to initiate the analysis.
   
     The API will process the reviews and provide the following results:
     - Sentiment analysis: Each review will be classified as "good" or "bad" based on sentiment.
     
     - Review themes: The API will provide insights into the underlying themes discovered through topic modeling.
     
