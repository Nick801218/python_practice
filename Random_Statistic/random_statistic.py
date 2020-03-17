# Random module (Do not name your file the same name as the module)
import random
data_ch=random.choice([1,6,3,7,2])
print(data_ch)

data_sam=random.sample([1,6,3,7,2],3)
print(data_sam)

data_shl=[1,70,3,7]
random.shuffle(data_shl)
print(data_shl)

data_uni=random.random()# =random.unform(0.0,1.0)
print(data_uni)

data_nor=random.normalvariate(0,10)
print(data_nor)

# Statistic module
import statistics as stat
print(stat.mean([1,7,36,80]))
print(stat.median([1,7,36,80]))
print(stat.stdev([1,7,36,80]))

