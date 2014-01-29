class BettingMoney:
	"""TopCoder Single Round Match 191 Round 1 - Division II, Level One
	   Steven Schmatz"""
	def moneyMade(self, amounts, centsPerDollar, finalResult):
		win_list = amounts[:finalResult] + amounts[finalResult + 1:]
		money_won = sum(win_list)*100
		money_lost = amounts[finalResult]*centsPerDollar[finalResult]
		return money_won - money_lost
		
"""
Test Cases
----------

amounts_test = [100,100,100,100]
centsPerDollar_test = [5,5,5,5]
finalResult_test = 0

amounts_test = [10,20,30]
centsPerDollar_test = [20,30,40]
finalResult_test = 1

test = BettingMoney()
print test.moneyMade(amounts_test, centsPerDollar_test, finalResult_test)"""