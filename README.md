# Stocky

Like many stuck at home during the pandemic, I've turned towards the stock market as a distraction, a form of entertainment and because it's an important topic to be knowledgable about. I wanted to start a coding project that incorporates my newfound interest and see where it goes.

Step 1: Find an API that will give stock information. There are many out there such as alpha vantage, morningstar, iexfinance to name a few. I settled on the Yahoo finance API provided through RapidAPI because the free tier is just right for me.

Step 2: Consume the API to provide information on whatever you like, documentation at https://rAPIdAPI.com/blog/how-to-use-the-yahoo-finance-API/
Edit: I ended up using a python libaray, pandas datareader, to access stock information but still via the yahoo finance API.

Step 3: I wanted to make a chart, straightforward goal. I used pandas datareader to retrieve historical data and save it to a csv file. I read the csv file and plot the closing price. I used everyone's favorite meme stock, Tesla in this example.

Step 4: Tesla is a prime example of a momentum stock. One way to get an indicator of momentum is to plot the short term and the long term moving averages of the stock price. If the short term line is above the long term line then momentum is picking up and the price will most likely rise in the near term. If the short term line is below then momentum is slowing down and the price will most likely fall in the near term.

Step 5: Volume is a another indicator of momentum.
