positive_keywords = ['may', 'nice', 'please', 'yeet', 'want', 'ok', 'sure', 'can', 'good', 'yes', 'positive', 'true', 'yeah', 'affirmative', 'fine']
negative_keywords = ['dont', 'cant', 'bad', 'no', 'negative', 'false', 'stop', 'not']
neutral_keywords = ['maybe', 'neutral', 'um', 'guess']
strong_negative_keywords = ['never']
strong_positive_keywords = ['must']
not_neut_keys = ['sure']
must_neg_keys = ['never', 'not', 'stop']
must_pos_keys = ['do']
go_pos_keys = ['ahead']
do_pos_keys = ['it']
do_neg_keys = ['not']
i_pos_keys = ['guess', 'suppose', 'approve']

def shiftToAbs(value, pos=1, neg=1):
  if value == 0:
    pass

  elif value < 0:
    value += pos

  elif value > 0:
    value -= neg
  return value


def getUserInput(prompt=''):
  return input(prompt+'\n < ').split(' ')


def requestPermissionFromUser(prompt=None, weight=0, default=False, debug=False, diagnose=False):
  _local_polarity = 0
  _ask = getUserInput(prompt)

  for i in range(len(_ask)):
    if _ask[i] in positive_keywords:
      _local_polarity += 1 * (i + 1)

    elif _ask[i] in negative_keywords:
      _local_polarity -= 1 * (i + 1)
    
    try:
      if _ask[i] == 'must' and _ask[i + 1] in must_neg_keys:
        _local_polarity -= 2 * (i + 1)

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
  _simple_decision = shiftToAbs(_local_polarity, pos=weight, neg=weight)
  if debug: print('final decision: ', _simple_decision)
  if debug: print('\n')

  if not diagnose:
    if _simple_decision == 0:
      return default
  
    elif _simple_decision < 0:
      return False
  
    elif _simple_decision > 0:
      return True
  else:
    return [_local_polarity, _simple_decision, _ask]