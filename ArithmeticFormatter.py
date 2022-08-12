def arithmetic_arranger(problems, displayAnswers = True):

  answer = ''
  
  for firstLine in problems:
    firstOperand = firstLine.split()[0]
    secondOperand = firstLine.split()[2]
    largeOperand = int()

    if firstOperand >= secondOperand:
      largeOperand = firstOperand
    else:
      largeOperand = secondOperand

    space = ' ' * ( (len(str(largeOperand)) + 2) - len(firstOperand))
    
    answer += space + str(firstOperand) + '    '

  answer += '\n'
  
  for secondLine in problems:
    firstOperand = secondLine.split()[0]
    operator = secondLine.split()[1]
    secondOperand = secondLine.split()[2]
    largeOperand = int()

    if firstOperand >= secondOperand:
      largeOperand = firstOperand
    else:
      largeOperand = secondOperand

    space = ' ' * ( (len(str(largeOperand)) + 2) - len(secondOperand) - len(operator))
    
    answer += operator + space + str(secondOperand) + '    '

  answer += '\n'

  for dashesLine in problems:
    firstOperand = dashesLine.split()[0]
    secondOperand = dashesLine.split()[2]
    largeOperand = int()

    if firstOperand >= secondOperand:
      largeOperand = firstOperand
    else:
      largeOperand = secondOperand

    dashes = '-' * (len(str(largeOperand)) + 2)
    
    answer += dashes + '    '

  if displayAnswers is True:
    answer += '\n'
    
    for fourthLine in problems:
      firstOperand = fourthLine.split()[0]
      operator = fourthLine.split()[1]
      secondOperand = fourthLine.split()[2]
      finalAnswer = int()
      largeOperand = int()
  
      if firstOperand >= secondOperand:
        largeOperand = firstOperand
      else:
        largeOperand = secondOperand

      if '+' == operator:
        finalAnswer = int(firstOperand) + int(secondOperand)
      if '-' == operator:
        finalAnswer = int(firstOperand) - int(secondOperand)
  
      space = ' ' * ( (len(str(largeOperand)) + 2) - len(str(finalAnswer)))
    
      answer += space + str(finalAnswer) + '    '
    
  #print(answer)

  arranged_problems = answer
  
  return arranged_problems
