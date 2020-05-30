import numpy as np 


class PayOff:
    def __init__(self, TheOptionsType_, Strike_):
        '''
        Inputs:
        =========
        TheOptionsType_: string (European call, European put, Binary call, Binary put)
        Strike_: float strike price
        '''
        
        self.__TheOptionsType = TheOptionsType_
        self.__Strike = Strike_
        
    def __call__(self,spot):
        # Overloading the ( ) operator
        '''
        inputs:
        =========
        spot: numpy array of spot prices
        
        
        returns:
        =========
        payoff value for each option 
        '''
        
        if self.__TheOptionsType == 'European call':
            return np.maximum(spot - self.__Strike,0)
        elif self.__TheOptionsType == 'European put':
            return np.maximum(self.__Strike - spot,0)
        elif self.__TheOptionsType == 'Binary call':
            return np.piecewise(spot, [spot < self.__Strike, spot >= self.__Strike], [0, 1])
        elif self.__TheOptionsType == 'Binary put':
            return np.piecewise(spot, [spot <= self.__Strike, spot > self.__Strike], [1, 0])
        else:
            raise Exception('Unknown option type found.')