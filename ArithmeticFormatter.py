def arithmetic_arranger(problems, answerDisplay = False):
  problem = ['', '', '', '']

  # Error 1: that is meaningful to the user.
  if len(problems) > 5:
    return 'Error: Too many problems.'

  for i in range(0, len(problems)):
    dashes = '-'
    answer = str()

    # Error 2: that is meaningful to the user.
    if problems[i].split()[1] != '+' and problems[i].split()[1] != '-': # Return if either + or - doesn't exist.
      return '''Error: Operator must be '+' or '-'.'''

    # Error 3: that is meaningful to the user.
    if not problems[i].split()[0].isdigit() or not problems[i].split()[2].isdigit():
      return '''Error: Numbers must only contain digits.'''

    # Error 4: that is meaningful to the user.
    if len(problems[i].split()[0]) > 4 or len(problems[i].split()[2]) > 4:
      return '''Error: Numbers cannot be more than four digits.'''
      
    if int(problems[i].split()[0]) >= int(problems[i].split()[2]):
      dashes *= ( len(problems[i].split()[0]) + 2 )
    else:
      dashes *= ( len(problems[i].split()[2]) + 2 )

    if answerDisplay == True:
        if problems[i].split()[1] == '+':
          answer = str( int(problems[i].split()[0]) + int(problems[i].split()[2]) )
          problem[3] += (' ' * (len(dashes) - len(answer)) ) + answer
        else:
          answer += str( int(problems[i].split()[0]) - int(problems[i].split()[2]) )
          problem[3] += (' ' * (len(dashes) - len(answer)) ) + answer
          
    if i != len(problems)-1:
      problem[0] += ( 
        (' ' * (len(dashes) - len(problems[i].split()[0])) )
        + problems[i].split()[0] + '    ')

      problem[1] += ( 
        problems[i].split()[1] 
        + ( ' ' * (len(dashes) - len(problems[i].split()[2]) - 1))
        + problems[i].split()[2] + '    '
      )

      problem[2] += dashes + '    '

      problem[3] += '    '
        
    if i == len(problems)-1:
      problem[0] += ( 
        (' ' * (len(dashes) - len(problems[i].split()[0])) )
        + problems[i].split()[0] + '\n')

      problem[1] += ( 
        problems[i].split()[1] 
        + ( ' ' * (len(dashes) - len(problems[i].split()[2]) - 1))
        + problems[i].split()[2] + '\n'
      )

      problem[2] += dashes + '\n'

  arranged_problems = problem[0] + problem[1] + problem[2] + problem[3]
  
  return arranged_problems
