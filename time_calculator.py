def add_time(start, duration, dayow = None):
    lst = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    part, meri = start.split()
    start_hour, start_minute = part.split(':')
    dur_hour, dur_minute = duration.split(':')
    sum_hour = int(start_hour) + int(dur_hour)
    sum_minute = int(start_minute) + int(dur_minute)
    if sum_minute >= 60:
        sum_hour = sum_hour + (sum_minute // 60)
        sum_minute = sum_minute % 60

    minutes = str(sum_minute).zfill(2)
    new_hour = sum_hour % 12
    if new_hour == 0:
        new_hour = 12

    if (sum_hour // 12) % 2 != 0:
        new_meri = 'AM' if meri == 'PM' else 'PM'
    elif sum_hour < 12:
        new_meri = meri
    else:
        new_meri = meri
    new_time = str(new_hour) + ':' + str(minutes).zfill(2) + ' ' + new_meri
    #check dayow and find index
    if dayow:
        day = dayow.lower()
        index = lst.index(day)
        if sum_hour < 24:
            new_day = lst[index].title()
            new_time = str(new_hour) + ':' + str(minutes).zfill(2) + ' ' + new_meri + ', ' + new_day
        if sum_hour >= 24:
            index = index + round(sum_hour / 24)
            
    if meri == 'PM' and 24 > sum_hour > 12:
        new_time = new_time + ' (next day)'

    if sum_hour >= 24:
        nday = round(sum_hour / 24)
        if nday > 1:
            day_later = ' (' + str(nday) + ' days later)'
        else:
            day_later = ' (next day)'
        new_time = str(new_hour) + ':' + str(minutes).zfill(2) + ' ' + new_meri + day_later
        if dayow:
            if index >= 7:
                index = index % 7
                new_day = lst[index].title()
            else:
                new_day = lst[index].title()
            new_time = str(new_hour) + ':' + str(minutes).zfill(2) + ' ' + new_meri + ', ' + new_day + day_later

    return new_time


#days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)

print(add_time("11:59 PM", "24:05"))
# "12:04 AM (2 days later)"

print(add_time("2:59 AM", "24:00", "saturDay"))
# "2:59 AM, Sunday (next day)"

print(add_time("8:16 PM", "466:02", "tuesday"))
#return  "6:18 AM, Monday (20 days later)"

print(add_time("2:59 AM", "24:00"))
#return "2:59 AM (next day)"

print(add_time("11:59 PM", "24:05"))
#return  "12:04 AM (2 days later)"

print(add_time("8:16 PM", "466:02"))
#return "6:18 AM (20 days later)"
