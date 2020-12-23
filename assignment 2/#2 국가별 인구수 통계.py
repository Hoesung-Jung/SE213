def get_population():
    f = open("C:\python deafault\pop.csv",'r')
    lines = f.readlines()
    f.close()
    del lines[0]
    country_population = {}
    for i in range(len(lines)):
        new_line  = lines[i].strip
        many_data = lines[i].split(',')
        country_population[many_data[1].strip()] = int(many_data[2])  #국가이름이 key이고 인구수가 value인 사전 완성
    #최고 인구수 찾기
    high_number = max(country_population.values())
    high_country = list(country_population.keys())[list(country_population.values()).index(high_number)]
    #median 구하기
    average = sum(list(country_population.values()))/len(list(country_population.values())) #value 수나 국가 수나 같다.
    print("{0}:{1}".format(high_country,high_number))
    real_median_country = list(country_population.keys())[int((len(country_population.keys())+1)/2)-1]
    real_median_number = list(country_population.values())[int((len(country_population.keys())+1)/2)-1]
    print("{0}:{1}".format(real_median_country, real_median_number))
    print("Average:{:.2f}".format(average))

get_population()