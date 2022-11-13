from TravelAgent import TravelAgent

def main():
    travel_agent = TravelAgent('Go Jaan')
    trip_info1 = travel_agent.set_trip_multi_city_one_way('DAC', 'PRA', '02/10/2022')
    print('aircraft', trip_info1[0])
    print('aircraft', trip_info1[1])

if __name__ == '__main__':
    main()