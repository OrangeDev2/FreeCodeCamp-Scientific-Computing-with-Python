def add_time(start, duration, dayOfTheWeek = str()):
# Returns: 12:03 AM, Thursday (2 days later)
  day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

  startHour = int(start.split(":")[0])
  startMinute = int(start.split(":")[1].split()[0])
  startEnding = start.split(":")[1].split()[1]

  durationHour = int(duration.split(":")[0])
  durationMinute = int(duration.split(":")[1])

  addedHour = startHour + durationHour
  addedMinute = startMinute + durationMinute

  newHour = int()
  newMinute = int()

  n = int() #number of days

  dayChange = 0

  n_ending = 0 # count of ending format changes.  AM -> PM -> ...

  while addedHour > 12 or addedMinute >= 60:
    if addedHour > 12:
      addedHour -= 12
      dayChange += 12
      n_ending += 1
      
    if addedMinute >= 60: 
      addedMinute -= 60
      addedHour += 1

      if addedHour >= 12: # Example: 11:00 AM -> 12:00 PM, thats 1 count of ending format change
        n_ending += 1
      

  if dayChange >= 12 and startEnding == 'PM':
    n += 1
    #n_ending += 1
    while dayChange >= 24:
      n += 1
      dayChange -= 24
  elif dayChange >= 12 and startEnding == 'AM':
    while dayChange >= 24:
      n += 1
      dayChange -= 24

  newHour = str(addedHour)
  newMinute = str(addedMinute)
  
  if addedMinute < 10:
    newMinute = '0' + str(addedMinute)

  newTime = newHour + ':' + newMinute

  ##############################
  #print(newTime)
  #print('n', n)
  #print('n_ending', n_ending)

  #newEnding = str()
  newEnding = 'AM'
  
  if n_ending % 2 == 0:
    newEnding = startEnding
  if n_ending % 2 != 0 and startEnding == 'AM':
    newEnding = 'PM'

  #print('newEnding', newEnding)
  
  dayLater = str()

  result = newTime + ' ' + newEnding
  
  if n == 1:
    dayLater = '(next day)'
    result = newTime + ' ' + newEnding + ' ' + dayLater
  if n > 1:
    dayLater = f'({n} days later)'
    result = newTime + ' ' + newEnding + ' ' + dayLater
  
  if dayOfTheWeek.lower() in day:
    dayOfTheWeek = dayOfTheWeek.lower()
    newDay = dayOfTheWeek[0].upper() + dayOfTheWeek[1:]

    #print('test', newDay, dayOfTheWeek, n)

    if n >= 1:
      #print('n >= 1 is True')
      dayIndex = day.index(dayOfTheWeek.lower())
  
      #print('dayIndex', dayIndex)
  
      newIndex = dayIndex

      n_condition = n
      i = newIndex
      
      while n_condition >= 0:
        if i > 6:
          i -= 7
        #print(i)
        #print(day[i])
        newDay = day[i]
        
        i += 1
        n_condition -= 1
        #for i in range(newIndex , n+2):
        #  if i > 6:
        #    i -= 7
        #  print(i)
        #newDay = day[i]
  
      newDay = newDay[0].upper() + newDay[1:]
      
    #print(newDay)

    result = newTime + ' ' + newEnding + ', ' + newDay + ' ' + dayLater
    
    if n == 0:
      result = newTime + ' ' + newEnding + ', ' + newDay

  #result = result.rstrip()
  
  #print(result)
  
  return result
