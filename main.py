#!/usr/bin/python
#_*_ coding:utf-8 _*_

from rock_algorithm import RockAlgorithm
from data_point import DataPoint

__author__='Anry Yang'



a = [1,0,1,0,1]
b = [1,0,1,0,0]
c = [0,0,0,1,0]
d = [1,1,1,1,1]
e = [0,1,1,0,0]

dps = []
dps.append(DataPoint('a',a))
dps.append(DataPoint('b',b))
dps.append(DataPoint('c',c))
dps.append(DataPoint('d',d))
dps.append(DataPoint('e',e))

rock = RockAlgorithm(dps,3,0.2)
dnd = rock.cluster()

dnd.inspect_all()
# dnd.inspect_top()


# require 'set'
# require 'rock_algorithm'
# require 'data_point'

    
# a = ['1','2','3'].to_set
# b = ['11','9','10'].to_set
# c = ['11','9','10'].to_set
# d = ['11','10','6'].to_set
# e = ['5','6','7'].to_set

# dps = [DataPoint.new('a', a), DataPoint.new('b', b), DataPoint.new('c', c), DataPoint.new('d', d), DataPoint.new('e',e)]

# rock = RockAlgorithm.new(dps, 3, 0.2)

# dnd = rock.cluster

# puts '='*50
# puts dnd.inspect
