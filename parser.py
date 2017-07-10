root_directory = 'factbook.github.io-master/'
profiles_directory = root_directory + '_profiles/'
html_ext = '.html'

gdp_ppp_header = '<h3>GDP (purchasing power parity):</h3>'
gdp_per_cap_header = '<h3>GDP - per capita (PPP):</h3>'
population_header = '<h3>Population:</h3>'

def getGDPandPopulationFromProfile(profile_name):
    profile_file_name = profiles_directory + profile_name + html_ext
    profile_file = open(profile_file_name)

    lines = profile_file.readlines()

    def getData(data_line):
        begin_pos = data_line.find('>') + 1
        end_pos = data_line.find(' (')
        temp = data_line[begin_pos:end_pos]

        if temp.find('<') == -1:
            return temp

        return temp[:-(len(temp) - temp.find('<'))]

    country_gdp_per_cap = "$NA"
    for i in range(0, len(lines)):
        if lines[i].find('title:        \"') != -1:
            pos = lines[i].find(' - ')
            country_name = lines[i][pos + 2:-2]

        elif lines[i].find(gdp_ppp_header) != -1:
            country_gdp = getData(lines[i+1])

        elif lines[i].find(population_header) != -1:
            country_population = getData(lines[i+1])

        elif lines[i].find(gdp_per_cap_header) != -1:
            country_gdp_per_cap = getData(lines[i+1])

    profile_file.close()

    return [country_name, country_gdp, country_population, country_gdp_per_cap]


def getGDPandPopulationData():
    index_file = open(root_directory + 'index.md')

    country_data = []

    for line in index_file:
        if line.find('## Other (2)') != -1:
            break

        if line.find('`') == 0:
            country_data.append(getGDPandPopulationFromProfile(line[1:3]))

    index_file.close()

    def convertGDPToFloat(str_num):
        begin_pos = str_num.find('$') + 1
        end_pos = str_num.find(' thousand')
        if end_pos != -1:
            str_num = str_num[begin_pos:end_pos]
            num = float(str_num)
            num = num * 1000

        end_pos = str_num.find(' million')
        if end_pos != -1:
            str_num = str_num[begin_pos:end_pos]
            num = float(str_num)
            num = num * 1000000

        end_pos = str_num.find(' billion')
        if end_pos != -1:
            str_num = str_num[begin_pos:end_pos]
            num = float(str_num)
            num = num * 1000000000

        end_pos = str_num.find(' trillion')
        if end_pos != -1:
            str_num = str_num[begin_pos:end_pos]
            num = float(str_num)
            num = num * 1000000000000

        return num


    orig_length = len(country_data)
    for i in range(0, len(country_data)):
        if i >= orig_length:
            break

        if (country_data[i][1].find('$NA') != -1):
            del country_data[i]
            orig_length = orig_length - 1

        temp_str = country_data[i][2]
        temp_nums_as_str = temp_str.split(',')
        temp_str = ""

        for str_num in temp_nums_as_str:
            temp_str = temp_str + str_num

        country_data[i][2] = float(temp_str)

        country_data[i][1] = convertGDPToFloat(country_data[i][1])

        temp_str = country_data[i][3][1:]
        temp_nums_as_str = temp_str.split(',')
        temp_str = ""

        for str_num in temp_nums_as_str:
            temp_str = temp_str + str_num

        country_data[i][3] = float(temp_str)

    return country_data
