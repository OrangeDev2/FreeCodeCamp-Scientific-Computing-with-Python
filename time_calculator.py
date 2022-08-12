def add_time(start, duration, dayOfTheWeek = "tueSday"):
  #add_time("11:06 PM", "20:02") -> 1:08 PM

  n = 1 # number of days later

  dayOfTheWeek = dayOfTheWeek.lower()
  day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

  dayLater = ''
  
  startEnding = start.split(':')[1].split()[1]
  ending = ['AM', 'PM']

  startHour = int(start.split(':')[0])
  startMinute = int(start.split(':')[1].split()[0])

  durationHour = int(duration.split(':')[0])
  durationMinute = int(duration.split(':')[1])

  resultHour = startHour + durationHour
  resultMinute = startMinute + durationMinute

  while resultMinute > 59:
    resultMinute -= 60
    resultHour += 1

  hourChange = 0
  
  while resultHour > 12:
    resultHour -= 12
    hourChange += 12

    if hourChange == 24:
      n += 1
      hourChange = 0
    if startEnding == 'AM':
      startEnding = 'PM'
    if startEnding == 'PM':
      startEnding = 'AM'

  if n == 1:
    dayLater = '(next day)'
  if n > 1:
    dayLater = f'({n} days later)'

  index = day.index(dayOfTheWeek)
  #print(index)
  
  for i in range(0, n):
    print(i)

  resultTime = str(resultHour) + ':' + str(resultMinute) + ' ' + startEnding + ' ' + dayLater
  
  if resultMinute < 10:
    resultTime = str(resultHour) + ':0' + str(resultMinute) + ' ' + startEnding + ' ' + dayLater

  #print(resultTime)

  return new_time
