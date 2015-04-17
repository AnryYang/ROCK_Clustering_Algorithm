#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__='Anry Yang'

class DataPoint:
	def __init__(self,label,attr):
		self.label = label
		self.attr = attr
		
	def get_text_attr_values(self):
		return self.attr

	def inspect(self):
		content="{%s:%s}"%(self.label,self.attr)
		return content

# class DataPoint
#   attr_reader :label, :attributes
#   def initialize(label, attributes)
#     @label = label
#     @attributes = attributes
#   end
  
#   def get_text_attr_values
#     @attributes
#   end
# end
