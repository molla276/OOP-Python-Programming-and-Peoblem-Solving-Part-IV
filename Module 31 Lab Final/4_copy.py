total_rainfall = 0
def rainfall ( ) :
    week_days = [ 'Day_1' , 'Day_2' , 'Day_3' , 'Day_4' , 'Day_5' , 'Day_6' , 'Day_7' ]

    display_list = []
    for day in range(7) : 
        rain_fall = input ('Plze Enter your value for ' + week_days[day] + ': ')
        display_list.append (rain_fall)

    minimum = display_list[0]
    maximum = display_list[0]

    for rain in display_list :

        if rain < minimum : minimum = rain
        if rain > maximum : maximum = rain

    print ('Minimun rainfall for this week:' , minimum)
    print ('Maximum rainfall for this week:' , maximum)

def print_results(rainfall):
    total_weeks = len(rainfall)
    print("Weeks of rainfall", rainfall)
    
rainfall ()

weekly_rainfall = print_results()
print_results(weekly_rainfall)