import os, math
import sys
import pandas as pd
import backtrader as bt

# a class extending backtrader.Strategy
class GoldenCross(bt.Strategy):
    # a tuple defining these four variables, 
    # so as to pass the param to the method
    params = (('fast', 50),
              ('slow', 200),
              ('order_pct', 0.95),
              ('ticker', 'SPY'))

    def __init__(self):
        #initalise Fast MA
        self.fastma = bt.indicators.SimpleMovingAverage(
            self.data.close, 
            period=self.params.fast, 
            plotname='50 day MA'
        )
        #initalise Slow MA
        self.slowma = bt.indicators.SimpleMovingAverage(
            self.data.close, 
            period=self.params.slow, 
            plotname='200 day MA'
        )
        #initialise Crossover
        self.crossover = bt.indicators.CrossOver(
            self.fastma, 
            self.slowma
        )

    def next(self):
    # position.size means the share we actually own
    # And we are gonna buy the share as long as it doesn't go beyond my investment amount threshold
    # which is 95% order_pct
        
        
        if self.position.size == 0:
            # according to https://www.backtrader.com/docu/indautoref/#crossover,
            # 1.0 if the 1st data crosses the 2nd data upwards, = Golden Cross
            if self.crossover > 0:
                amount_to_invest = (self.p.order_pct * self.broker.cash)
                # size of share we buy
                    # (e.g. if we hv 100000 in total, the closing p is 100, then we will buy 1000 shares) 
                self.size = math.floor(amount_to_invest / self.data.close)
                print("Buy {} shares of {} at {}".format(self.size, self.p.ticker, self.data.close[0]))
                #we are gonna buy
                self.buy(size=self.size)
                
        if self.position.size > 0:
                # -1.0 if the 1st data crosses the 2nd data downwards = Death Cross
            if (self.crossover < 0):
                print("Sell {} shares of {} at {}".format(self.size, self.p.ticker, self.data.close[0]))
                self.close()