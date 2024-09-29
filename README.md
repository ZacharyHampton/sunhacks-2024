# Product Finder

### Inspiration
In today’s digital age, consumers are faced with **overwhelming choices** when shopping online. Whether it’s buying a phone, skis, or books, people spend countless hours sifting through reviews and specs, often ending up frustrated. We wanted to simplify this process by creating a tool that delivers **personalized, AI-driven product recommendations**, empowering users to quickly and confidently make purchasing decisions. 

We also sought to explore **AI innovations**, **cloud scalability**, and **data-driven insights**, while incorporating ideas for **social good** and **accessibility** to benefit a wide range of users.

### What It Does
**findit.** is an intelligent shopping assistant designed to guide users through the decision-making process. By interacting with a **natural language chatbot**, users can specify their needs (e.g., “I need a phone with good battery life and a large display”). The chatbot leverages **large language models (LLMs)** and a **vectorized product database** to return **3-5 highly personalized product recommendations**. It is also designed to allow users to **tweak their preferences** for an even better match. 

findit. can expand to any product category, making it a **scalable and versatile solution** for online shoppers.

### How We Built It
1. **Frontend**: Developed with **Vue.js**, providing an intuitive UI that allows users to easily interact with the chatbot.
2. **Backend**: Built on **MongoDB Atlas**, which handles a large dataset of product details. The data is vectorized to enable efficient filtering based on user preferences. A **retrieval-augmented generation (RAG) system** combines database lookups with the power of LLMs to provide accurate recommendations.
3. **Cloud Infrastructure**: Hosted on **AWS**, ensuring scalability, security, and reliability for real-time chatbot responses and user queries.

### Challenges We Ran Into
We were faced with challenges every step of our development journey. But we knew what we signed up for and though sleep deprived, we came through. Our Major Challenges were:
- **Training the AI chatbot** to ask the right questions and convert user inputs (e.g., "good camera") into specific product filters (e.g., camera resolution above 12MP).
- Balancing the system's **scalability and performance** to ensure fast, accurate recommendations across a wide variety of product categories.
-**vectorizing** the database.
-**Scraping** the data which can be used to train the AI Chatbot

### Accomplishments That We're Proud Of
- Implementing an **AI-powered product recommendation system** that significantly simplifies the shopping experience.
- Successfully utilizing **MongoDB Atlas** for efficient data management and scalable product queries.
- **Integrating accessibility features**, making the system usable for people with disabilities.
- Creating a solution that is easily **scalable to new product categories**, showing immense potential for growth and future applications.

### What We Learned
- We gained valuable experience in integrating **AI models** with structured datasets using MongoDB Atlas, enabling us to create **personalized shopping experiences**.
- **AWS cloud infrastructure** allowed us to scale the project globally, and we learned how important infrastructure reliability is in ensuring a smooth user experience.
- Our research into **accessibility** opened our eyes to the importance of designing solutions for **all users**, especially those with disabilities.

### What's Next for findit.
The potential for our solution is limitless. If supported: -
- **Expand product categories**: We plan to include other categories like laptops, home appliances, and fashion.
- **Affiliate partnerships**: We will integrate affiliate links to monetize recommendations and offer real-time pricing updates from e-commerce platforms.
- **Multi-language support**: To make findit. accessible to global audiences, we’ll add support for multiple languages, ensuring that everyone can benefit from the tool.
- **Incorporate advanced accessibility features**: Further enhancing **voice interfaces** and ensuring users with disabilities can easily navigate the platform.
