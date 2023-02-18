def add_time(start, duration, day=''):

    final_min = 0
    not_calculated = True
    new_time = ''
    days = ''
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

# splitting the data to independent values

    start_time, period = start.split(' ')
    start_hour, start_min = start_time.split(':')
    duration_hour, duration_min = duration.split(':')
    start_hour = int(start_hour)
    start_min = int(start_min)
    duration_hour = int(duration_hour)
    duration_min = int(duration_min)

# calculating total time gain

    while not_calculated:
        if start_min + duration_min > 59:
            duration_hour += 1
            duration_min = duration_min + start_min - 60
            start_min = 0
        final_min = start_min + duration_min
        not_calculated = False

# calculating final time

    temp_duration = duration_hour
    temp_start_hour = start_hour
    while temp_duration > 0:
        if temp_start_hour == 12:
            temp_start_hour = 1
            temp_duration -= 1
            continue
        elif temp_start_hour < 12:
            temp_start_hour += 1
            temp_duration -= 1
            continue
    converted_min = ((start_hour + duration_hour) * 60) + final_min

# testing for final period AM or PM

    if 1440 >= converted_min >= 720:
        if period == 'PM':
            final_period = 'AM'
        elif period == 'AM':
            final_period = 'PM'
    elif converted_min > 1440:
        if (converted_min // 720) % 2 == 0:
            final_period = period
        else:
            if period == 'PM':
                final_period = 'AM'
            elif period == 'AM':
                final_period = 'PM'
    elif converted_min < 720:
        final_period = period

    # calculating number of days

    if period == 'PM':
        if 720 <= converted_min <= 1440:
            days = 1
        elif converted_min > 1440:
            days = (converted_min//1440)+1
    elif period == 'AM':
        if 1440 <= converted_min <= 2160:
            days = 1
        elif converted_min > 2160:
            days = converted_min//1440

    tmp_days = days

# calculating the final day of the week

    if day != '':
        day = day.lower()
        day_nr = weekdays.index(day)
        if type(tmp_days) == str:
            tmp_days = 0
        if day_nr+tmp_days < 7:
            week_day = weekdays[day_nr + tmp_days].capitalize()
        else:
            while day_nr+tmp_days >= 7:
                tmp_days -= 7
            week_day = weekdays[day_nr + tmp_days].capitalize()

# final reports
# excluding starting day of the week

    if day == '':
        if type(days) == str:
            new_time = f"{temp_start_hour}:{final_min:02d} {final_period}"
        elif days == 1:
            new_time = f"{temp_start_hour}:{final_min:02d} {final_period} (next day)"
        elif days > 1:
            new_time = f"{temp_start_hour}:{final_min:02d} {final_period} ({days} days later)"

# including starting day of the week

    else:
        if type(days) == str:
            new_time = f"{temp_start_hour}:{final_min:02d} {final_period}, {week_day}"
        elif days == 1:
            new_time = f"{temp_start_hour}:{final_min:02d} {final_period}, {week_day} (next day)"
        elif days > 1:
            new_time = f"{temp_start_hour}:{final_min:02d} {final_period}, {week_day} ({days} days later)"

    return new_time

print(add_time("3:30 PM", "2:12", "Monday"))