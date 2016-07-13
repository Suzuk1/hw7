#!/usr/bin/env python3

import sys
import math



def komanum(self,g):
  goukei=0

  for element in g._board:
    if element!=0
    goukei=goukei+1
  return goukei


def caluculate(self,g):
  gouk=komanum(self,g)
  ariaA=[[2,3],[2,4],[2,5],[2,6],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[4,2],[4,3],[4,5],[4,6],[4,7],[5,2],[5,3],[5,4],[5,5],[5,6],[5,7],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7],[7,3],[7,4],[7,5],[7,6]]
  ariaB=[[2,2],[2,7],[7,2],[7,7]]
  ariaC=[[1,2],[1,3],][1,4],[1,5],[1,6],[1,7],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7],[2,8],[3,8],[4,8],[5,8],[6,8],[7,8]]
  ariaD=[[1,1],[1,8],[8,1],[8,8]]
  player = g.Next()
  
  
  if gouk<20:
    for element in g._board:
      if element==player:
	if element in ariaA:
	  total=total+5
        if element in ariaB:
	  total=total-10
        if element in ariaC:
	  total=total+10
        if element in ariaD:
	  total=total+30

    return total

  elif gouk<45:
    for element in g._board:
      if element==player:
	if element in ariaB:
	  total=total-10
        if element in ariaC:
	  total=total+10
        if element in ariaD:
	  total=total+30
      if element!=player and element!=0:
	if element in ariaA:
	  total=total+5
	  
    return total

  if gouk<64:
    for element in g._board:
      if element==player:
	if element in ariaA:
	  total=total+5
        if element in ariaB:
	  total=total-10
        if element in ariaC:
	  total=total+20
        if element in ariaD:
	  total=total+40

    return total

def soutei(self,g):
  
   k=0
    for tuginote in g.valid_moves():
      nextboard=g.NextBoardPosition(self, tuginote)
      tekivalid_moves = g.ValidMoves(nextboard)
      i=0
    
      for tekituginote in tekivalid_moves:
        nextboard2=g.NextBoardPosition(self, tekituginote)
        tekiSum[i]=caluculate(self,g,nextboard2)
        i=i+1
      max_idx=tekiSum.index(max(tekiSum))
      nextboard2a=g.NextBoardPosition(self,tekivalid_moves[max_idx])
      playersum[k]=caluculate(self,g,nextboard2a)
      k=k+1
    Max_idx=playersum.index(max(playersum))
    goodposition=valid_moves[Max_idx]
    
  return goodposition


if __name__ == '__main__':  
    move=soutei()
    return move