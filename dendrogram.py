#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__='Anry Yang'

from cluster_set import ClusterSet
import copy

class Dendrogram:
  def __init__(self,level_label_name):
    self.level_label_name = level_label_name
    self.next_level=0
    self.entry_map=[]
    self.level_labels=[]

  def add_level(self,label,clusters):
    cluster_set = ClusterSet()
    for cluster in clusters:
      cluster_set.add(copy.copy(cluster))
    level = self.next_level
    self.entry_map.append(cluster_set)
    self.level_labels.append(label)

    self.next_level+=1
    return level

  def inspect_all(self):
    for level in range(len(self.level_labels)):
      self.inspect(level)

  def inspect(self,level):
    cluster_num=1
    if self.entry_map[level].size()>0:
      print "=================================================================="
      print "Clutser for level %s; %s=%s; Number of clusters:%s"%(level,self.level_label_name,self.level_labels[level],self.entry_map[level].size())
      for cluster in self.entry_map[level].get_all_clusters():
        if cluster.size()>0:
          print '\tCluster No.%s:contains %s elements'%(cluster_num,cluster.size())
          cluster_num+=1
          # cluster.inspect() 
  def inspect_top(self):
    self.inspect(self.next_level-1)

# require 'cluster_set'
# class Dendrogram
  
#   attr_reader :next_level
  
#   def initialize(level_label_name)
#     @level_label_name = level_label_name
#     @next_level = 0
#     @entry_map = []
#     @level_labels = []
#   end
  
#   def add_level(label, clusters)
    
#     cluster_set = ClusterSet.new
#     clusters.each do |cluster|
#       cluster_set.add(cluster.clone)
#     end
    
#     level = next_level
    
#     @entry_map[level] = cluster_set
#     @level_labels[level] = label
    
#     @next_level += 1
    
#   end
  
#   def inspect
#     str = ''
#     @level_labels.size.times do |i|
#       str << "Cluster #{i}: Goodness #{@level_labels[i]}\n"
#       str << @entry_map[i].inspect
#       str << "\n"
#     end
#     str
#   end
  
# end
