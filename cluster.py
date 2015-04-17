#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__='Anry Yang'

class Cluster:
  def __init__(self,*args):
    self.elements = set()
    for cluster in args:
      self.add(cluster)

  def add(self,c):
    if isinstance(c,Cluster):
      for e in c.get_elements():
        self.elements.add(e)
    else:
      self.elements.add(c)

  def contains(self,e):
    if e in self.elements:
      return True
    else:
      return False

  def get_elements(self):
    return self.elements

  def inspect(self):
    for e in self.elements:
      print '\t\t'+e.inspect()

  def size(self):
    return len(self.elements)


# require 'set'
# class Cluster
  
#   def initialize(*args)
#     puts "Initializing cluster with args #{args.inspect}"
#     @elements = Set[]
#     args.each do |a|
#       add(a)
#     end
#     puts "Cluster created with elements: #{get_elements.collect { |e| e.inspect }.join(', ')}"
#   end
  
#   def add(e)
#     if e.is_a? Cluster
#       e.get_elements.each do |element|
#         puts "Adding element #{element}"
#         @elements.add element
#       end
#     else
#       puts "Adding element #{e}"
#       @elements.add e
#     end
#   end
  
#   def contains(e)
#     @elements.include? e
#   end
  
#   def get_elements
#     @elements
#   end
  
#   def size
#     @elements.size
#   end
  
# end