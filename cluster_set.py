#!/usr/bin/python
#-*- coding:utf-8 -*-

from cluster import Cluster

__author__='Anry Yang'


class ClusterSet:
  def __init__(self):
    self.all_clusters = set()

  def add(self,c):
    if isinstance(c,Cluster):
      self.all_clusters.add(c)

  def remove(self,c):
    self.all_clusters.remove(c)

  def size(self):
    return len(self.all_clusters)

  def get_all_clusters(self):
    return self.all_clusters



# require 'set'
# class ClusterSet

#   def initialize
#     @all_clusters = Set[]
#   end
  
#   def add(cluster)
#     @all_clusters.add cluster
#   end
  
#   def remove(cluster)
#     @all_clusters.remove cluster
#   end
  
#   def inspect
#     @all_clusters.collect do |cluster|
#         cluster.inspect
#     end.join("\n")
#   end
  
# end
