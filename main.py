#   Permissive Polarity Test
#     by Eric Rustrum
#
#  This program will scan your input and determine whether
#   you meant yes or no. It does this by searching for keywords
#   that will increase or decrease the polarity of your meaning.
#   In other words, it compares words associated with 'yes'
#   against words associated with 'no'. The further the word
#   in the sentence, the more it impacts the result. Some words
#   will trigger a neutral polarity shift, essentially moving
#   towards zero. I have not conducted any proper tests on this
#   as of yet, but so far it works very well. I would appreciate
#   feedback on this. This file, 'main.py', is not the module that
#   powers the project. The code is in the file 'ppt.py'.
#

from ppt import *

while True:
  if requestPermissionFromUser('may i speak now', debug = True):
    print('i will speak then')
  else:
    print('ok i will be quiet')