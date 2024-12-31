## Level 1 Exercise
Empty_list = list() # Declaring an empty list
List = [1, 'Car', 3, 4, 5] # Declaring a list with 5 elements
print(List) # Printing the list
Lenght = print(len(List)) # Printing the length of the list
First_item = print(List[0]) # Printing the first item in the list
Middle_item = print(List[2])
Last_item = print(List[-1]) # Printing the last item in the list
Mixed_data_types = ["Enock Namunane", 23, '23ft', "Single", "P.O.Box 166 Gulu city-Uganda"] 
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] 
print(it_companies) 
Number_of_companies = print(len(it_companies))
First_company = print(it_companies[0])
Middle_company = print(it_companies[3])
Last_company = print(it_companies[-1])
it_companies.insert(2, 'Tesla') # modifying list of companies using insert method
Modified_list = it_companies[0] = 'Facebook Inc'
print(it_companies)
it_companies.insert(3, 'EverPesa Technologies')
print(it_companies)
it_companies = [company.upper() if company== 'Tesla' else company for company in it_companies] # Changing Tesla to uppercase using list comprehension method
print(it_companies)
# Checking if a certain company exists in the it_companies list
Company = 'Tesla'
if Company in it_companies:
    print("Yes", Company, "is in the list")
else:
    print("No", Company, "is not in the list")

joined_companies = '#'.join(it_companies)
print(joined_companies)
sorted_list = sorted(it_companies)
reversed_list = sorted(it_companies, reverse = True)
First_3_companies = it_companies[:3]
Last_3_companies = it_companies[-3:]
Middle_company = it_companies[int(len(it_companies)/2)]
it_companies.pop(0)
it_companies.pop(4)
it_companies.pop(-1)
it_companies.clear()
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
full_stack.insert(4, 'Python')
full_stack.insert(5, 'SQL')




## Level 2 Exercise
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
max_age = max(ages)
min_age = min(ages)
ages.append(max_age)
ages.append(min_age)
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]
average_age = sum(ages) / n
range_age = max_age - min_age
min_average_diff = abs(min_age - average_age)
max_average_diff = abs(max_age - average_age)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
index = len(countries)//2
middle_country = countries[index]
print(middle_country)
first_half = countries[:index]
second_half = countries[index:]
countries_to_unpack = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# Unpacking the first three countries and the rest as scandic countries
first, second, third, *scandic_countries = countries_to_unpack
[print(country) for country in [first, second, third] + scandic_countries]