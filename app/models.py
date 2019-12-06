from datetime import date
import calendar


class Result:

    SQLITE_DATE_FORMAT = '%Y-%m-%d'
    INVESTMENT_FRIENDLY_MONTHS = [11, 12, 1, 2, 3, 4]

    month = date.today().month
    month_name = calendar.month_name[month]

    def __init__(self, interest_rate_date, inflation_rate_data, exchange_rate_data):
        self.interest_rate = interest_rate_date.iloc[-1][0]
        index = -2
        while interest_rate_date.iloc[index][0] == self.interest_rate:
            print("Skipping: " + str(interest_rate_date.iloc[index][0]))
            index = index - 1
        self.past_interest_rate = interest_rate_date.iloc[index][0]
        print(str(self.past_interest_rate))

        self.past_inflation_rate_date = inflation_rate_data.index[-14].start_time.strftime('%Y-%m')
        self.past_inflation_rate = inflation_rate_data.iloc[-14][0]
        self.inflation_rate_date = inflation_rate_data.index[-2].start_time.strftime('%Y-%m')
        self.inflation_rate = inflation_rate_data.iloc[-2][0]

        self.past_exchange_rate_date = exchange_rate_data.index[-13].start_time.strftime('%Y-%m')
        self.past_exchange_rate = exchange_rate_data.iloc[-13][0]
        self.exchange_rate_date = inflation_rate_data.index[-1].start_time.strftime('%Y-%m')
        self.exchange_rate = exchange_rate_data.iloc[-1][0]

    def __repr__(self):
        return '<Result {} {} {} {} {} {} >'.format(self.past_interest_rate,  self.interest_rate,
                                                    self.past_inflation_rate, self.inflation_rate,
                                                    self.past_exchange_rate, self.exchange_rate)

    def get_season_result(self):
        return 1 if self.month in self.INVESTMENT_FRIENDLY_MONTHS else 0

    def get_interest_rate_result(self):
        return 1 if self.interest_rate < self.past_interest_rate else 0

    def get_inflation_rate_result(self):
        return 1 if self.inflation_rate <= self.past_inflation_rate else 0

    def get_exchange_rate_result(self):
        return 1 if self.exchange_rate < self.past_exchange_rate else 0

    def get_result(self):
        return self.get_season_result() + self.get_interest_rate_result() \
               + self.get_inflation_rate_result() + self.get_exchange_rate_result()
