


def maxProfit(price, n):

	#create profit list
	profit = [0]*n

	max_price = price[n-1]

	for i in range(n-2, 0, -1):

		if price[i] > max_price:
			max_price = price[i]

		# we can get profit[i] by taking maximum of previous maximum,i.e., profit[i+1]
		# profit by buying at price[i] and selling at max_price
                #profit[i] = max(profit[i+1], max_price - price[i])

	
	min_price = price[0]

	for i in range(1, n):

		if price[i] < min_price:
			min_price = price[i]

		# Maximum profit is maximum of:
		# a) previous maximum,
		# i.e., profit[i-1]
		# b) (Buy, Sell) at
		# (min_price, A[i]) and add
		# profit of other trans.
		# stored in profit[i]
		profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))

	result = profit[n-1]

	return result


# function
price = [3,3,5,0,0,3,1,4]
print("input:" ,price)
print ("Maximum profit is", maxProfit(price, len(price)))
