# -*- coding: utf-8 -*-
"""Untitled59.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fj85xN30bfCwL5pk7m8weyqc0pxVAk9s
"""

def kasallik_tashxisi(alomat):
  if alomat=="bosh og'riq, istima":
    return "Sizda grip bor"
  elif alomat=="qorin og'riq":
    return "Sizda spazma bor"
  else:
    return "Noaniq kasallik, Shifokorga murojaat qiling"
alomat=input("Alomatni kiriting   ")
natija=kasallik_tashxisi(alomat)
print(natija)