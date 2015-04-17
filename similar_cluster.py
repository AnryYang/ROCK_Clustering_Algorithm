#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__='Anry Yang'

class SimilarCluster:
  def __init__(self,cluster_key,goodness=0.0):
    self.cluster_key=cluster_key
    self.goodness=goodness

  def get_goodness(self):
    return self.goodness

  def get_cluster_key(self):
    return self.cluster_key

  @staticmethod
  def sort_by_goodness(values):
    def compare(f1,f2):
      result=0
      if f1.get_goodness()<f2.get_goodness():
        result=1
      elif f1.get_goodness()>f2.get_goodness():
        result=-1
      else:
        result=0
      return result
    values.sort(cmp = compare)
# class SimilarCluster
  
#   attr_reader :cluster_key, :goodness
  
#   def initialize(cluster_key, goodness = 0.0)
#     @cluster_key = cluster_key
#     @goodness = goodness 
#   end
  
#   def goodness
#     @goodness
#   end
  
#   def self.sort_by_goodness(values)
#     values.sort do |one, another|
#       # Sort descending
#       another.goodness <=> one.goodess
#     end
#   end

  
# end
