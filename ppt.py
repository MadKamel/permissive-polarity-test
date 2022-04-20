#
#-------------------------------------------------------------------------------------------------------------------------------------
#         PPT (Permissive Polarity Test)
#                 by Eric Rustrum
#
#             This program/module takes user input as a yes or no answer and translates it into a boolean value or polarity
#                 value, such as +1 or -3, with '+' being yes and '-' being no. If the user gives an amibiguous answer, then
#                 the module will automatically return a default value of False. To change the default return, the 'default'
#                 argument in the main method, 'requestPermissionFromUser' needs to be either True or False, depending on the
#                 desired default return value.
#
#--------------------------------------------------------------------------------------------------------------------------------------
#
# NOTE: because of the nature of the expected inputs, the most useful application for this would be in voice commands for yes/no
#            questions.
#
#
# Note from future me: Hi! This is future me. I just went into the code and added a bunch of comments. Bye!
#

# Keywords to look out for:
positive_keywords = ['may', 'nice', 'please', 'want', 'ok', 'sure', 'can', 'good', 'yes', 'positive', 'true', 'yeah', 'affirmative', 'fine']
negative_keywords = ['dont', 'cant', 'bad', 'no', 'negative', 'false', 'stop', 'not']
neutral_keywords = ['maybe', 'neutral', 'um', 'guess']
strong_negative_keywords = ['never']
strong_positive_keywords = ['must']
not_neut_keys = ['sure'] # as in 'not sure'
must_neg_keys = ['not'] # as in 'must not'
must_pos_keys = ['do'] # as in 'must do'
go_pos_keys = ['ahead'] # as in 'go ahead'
do_pos_keys = ['it'] # as in 'do it'
do_neg_keys = ['not'] # as in 'do not'
i_pos_keys = ['guess', 'suppose', 'approve'] # as in 'I suppose' or 'I approve'
why_pos_keys = ['not'] # as in 'why not'

# Nifty lil' function that shifts a number towards zero. It's a misnomer.
def shiftToAbs(value, pos=1, neg=1):
  if value == 0: # Nothing to shift
    pass

  elif value < 0: # It's negative, shift it up.
    value += pos

  elif value > 0: # It's positive, shift it down.
    value -= neg
  return value # Return value.


def getUserInput(prompt=''):
  return input(prompt+'\n < ').split(' ')


# Main function
def requestPermissionFromUser(prompt=None, weight=0, default=False, debug=False, diagnose=False):
  _local_polarity = 0 # I just added this comment here because I could
  _ask = getUserInput(prompt) # This line wanted to be a team player too

  for i in range(len(_ask)): # Go through each word in list looking for keywords.
    if _ask[i] in positive_keywords:
      _local_polarity += 1 * (i + 1)

    elif _ask[i] in negative_keywords:
      _local_polarity -= 1 * (i + 1)
    
    try:
      if _ask[i] == 'must' and _ask[i + 1] in must_neg_keys:
        _local_polarity -= 2 * (i + 1)
      
      elif _ask[i] == 'why' and _ask[i + 1] in why_pos_keys:
        _local_polarity += 2 * (i + 1)
        
      elif _ask[i] == 'not' and _ask[i + 1] in not_neut_keys:
        _local_polarity = shiftToAbs(_local_polarity)
      
      elif _ask[i] == 'i' and _ask[i + 1] in i_pos_keys:
        _local_polarity += 1 * (i + 1)
      elif _ask[i] == 'go' and _ask[i + 1] in go_pos_keys:
        _local_polarity += 1 * (i + 1)
      
      elif _ask[i] == 'must' and _ask[i + 1] in must_pos_keys:
        _local_polarity += 2 * (i + 1)

      elif _ask[i] == 'do' and _ask[i + 1] in do_pos_keys:
        _local_polarity += 2 * (i + 1)

      elif _ask[i] == 'do' and _ask[i + 1] in do_neg_keys:
        _local_polarity -= 1 * (i + 1)
        
    except:
      pass

    if _ask[i] in strong_negative_keywords:
      _local_polarity -= 2 * (i + 1)

    elif _ask[i] in strong_positive_keywords:
      _local_polarity += 2 * (i + 1)

    elif _ask[i] in neutral_keywords:
      _local_polarity = shiftToAbs(_local_polarity)

  if debug: print('choice polarity: ', _local_polarity)
  _simple_decision = shiftToAbs(_local_polarity, pos=weight, neg=weight) # Shifts the resulting polarity based on severity/weight
  if debug: print('final decision: ', _simple_decision)
  if debug: print('\n')

  if not diagnose: # Diagnose = Debug mode, so this is normal behaviour.
    if _simple_decision == 0:
      return default # Return the default judgement (indecisive)
  
    elif _simple_decision < 0:
      return False # Return False (negative polarity)
  
    elif _simple_decision > 0:
      return True # Return True (positive polarity)
  else: # This, on the other hand, is debug behaviour.
    return [_local_polarity, _simple_decision, _ask] # Just dump all the values


# Goodbye
