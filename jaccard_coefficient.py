#!/usr/bin/python
#-*- coding:utf-8 -*-

import math

__author__='Anry Yang'

class JaccardCoefficient:
	def similarity(self,x,y):
		if len(x)==0 or len(y)==0:
			return 0.0
		else:
			set_x = set(x)
			set_y = set(y)
			union_xy = set_x | set_y
			intersection_xy = set_x & set_y
			return float(len(intersection_xy))/float(len(union_xy))

# class JaccardCoefficient
  
#   def similarity(x, y)
#     return 0.0 if x.size == 0 or y.size == 0
#     set_x = x.to_set
#     set_y = y.to_set
#     union_xy = set_x | set_y
#     intersection_xy = set_x & set_y
#     intersection_xy.size.to_f / union_xy.size.to_f 
#   end
  
# end
