'''this class is simple risk calculator based on the sentiment analysis.
'''
class risk_analyzer:
    #constuctor positive, negative and neutral emotions
    def __init__(self,positive,negative,neutral):
        self.positive=positive
        self.negative=negative
        self.neutral=neutral
        #risk to be calculated
        self.risk=None
       
    def risk_taken(self):
        #split the neutral emotion in half 
        #and adds the half in positive and the other half in negative 
        self.positive+=self.neutral/2
        self.negative+=self.neutral/2
        if self.positive>85.0:
            self.risk="very low risk. Very good reputation"
            
        elif self.positive>70.0:
            self.risk="low risk. Good reputation"
     
        elif self.positive >60.0:
            self.risk="medium risk"
            
        elif self.positive>40.0:
            self.risk="high risk. Bad reputation"  
            
        else:
            self.risk="very high risk. Very bad reputation"
