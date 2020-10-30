population_symbols = {'AAPL':15, 'TSLA':10, 'T':7, 'AMZN':44, 'INTC':16, 'NOK':1, 'MSFT':90, 'GILD':400, 'BAC':3, 'NVDA':78, 'WMT':14}

while(True):

	Stock_Name = input('Please enter a stock ticker symbol (type exit to close): ')

	if Stock_Name == 'exit':
		break


	if Stock_Name in population_symbols.keys():
		print('The current price of ' + Stock_Name + ' is ' + str('{:,}'.format(population_symbols[Stock_Name])))

	else: 
		print("Please check for any typos. Data not available for ",Stock_Name)