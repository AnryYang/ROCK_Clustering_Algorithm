#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__='Anry Yang'

#
# Goodness measure for merging two clusters.
#

class MergeGoodnessMeasure:
  def __init__(self,th):
    self.link_threshold = th
    self.p = 1.0 + 2.0*self.f(self.link_threshold)

  def g(self,n_links,nx,ny):
    a = (nx+ny)**self.p
    b = nx**self.p
    c = ny**self.p
    return float(n_links)/(a-b-c)

  def f(self,th):
    return (1.0-th)/(1.0+th)

# class MergeGoodnessMeasure 
#   # link_threshold: Threshold value that was used to identify neighbors among points.
#   # p: Intermediate value that is used in calculation of goodness measure and stays the same for different clusters.
#   attr_accessor :link_threshold, :p
  
#   def initialize(th)
#     @link_threshold = th
#     @p = 1.0 + 2.0 * f(th)
#   end
  
#   def g(n_links, nx, ny)
#     a = (nx + ny) ** p
#     b = nx ** p
#     c = ny ** p
#     n_links / (a - b - c)
#   end
  
#   # This is just one of the possible implementations.
#   # linkThreshold threshold value that was used to identify neighbors among points.    
#   def f(th)
#     # This implementation assumes that linkThreshold was a threshold for similarity measure (as opposed to dissimilarity/distance). 
#     (1.0 - th) / (1.0 + th);
#   end
# end