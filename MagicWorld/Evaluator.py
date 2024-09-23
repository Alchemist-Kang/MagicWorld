
import math
import time

#1-D lattice total energy function evaluator class
#
class MagicPower:
    selfCost=None
    selfDamage=None
    EnhanceDamage=None
        
    @classmethod  
    def ObjFuct(cls,state):
        totalDamage=0
        totalCost=0
        for i in range(len(state)):
            totalCost+= cls.selfCost[state[i]]

            if i == 0: totalDamage+=cls.selfDamage[state[i]]

            elif ((state[i]== 2) and (state[i-1]==2)):
                totalDamage= totalDamage + (cls.selfDamage[state[i]] + (cls.EnhanceDamage[state[i]][state[i-1]])[0]) *(cls.EnhanceDamage[state[i]][state[i-1]])[1]
            
            else:
                totalDamage= totalDamage + (cls.selfDamage[state[i]])*(cls.EnhanceDamage[state[i-1]][state[i]])
        objectives = [totalCost,totalDamage]

        
        return objectives

