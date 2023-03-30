from datetime import *


# todays_date= date.today()
# print(todays_date)



# date_str = todays_date.isoformat()
# print(date_str)



# DOB = "2021-04-13"
# # dt_object = datetime.strptime(DOB, "%y-%m-%d")
# # print(dt_object)
# # DOB = (datetime.fromisoformat(DOB))
# date_1 = datetime.strptime(DOB, "%Y-%m-%d")
# print(date_1)
# # date_2 = datetime.strptime(todays_date, "%Y-%m-%d")
# print(todays_date)
# date_2 = datetime.strftime(todays_date, "%Y-%m-%d")
# date_2 = datetime.strptime(date_2, "%Y-%m-%d")
# date_1 = datetime.strptime(DOB, "%Y-%m-%d")
# date_difference = date_2 - date_1
# print(date_difference)

# if date_difference > 700:
#     print("yes")

# DOB_1 = "2021-04-13"

# date_2 = todays_date.strftime("%Y/%m/%d")
# print(date_2)

# date_of_birth = int((DOB_1[0]) + (DOB_1[1]) + (DOB_1[2]) + (DOB_1[3]) + (DOB_1[5]) + (DOB_1[6]) + (DOB_1[8] + (DOB_1[9])))
# print(date_of_birth)
# todays_date = int((date_2[0]) + (date_2[1]) + (date_2[2]) + (date_2[3]) + (date_2[5]) + (date_2[6]) + (date_2[8] + (date_2[9])))
# print(todays_date)

# print(todays_date - date_of_birth)



date_of_birth = "2020-10-20"
date_today = date.today()
todays_date = date_today.strftime("%Y/%m/%d")
dateofbirth_int = int((date_of_birth[0]) + (date_of_birth[1]) + (date_of_birth[2]) + (date_of_birth[3]) + (date_of_birth[5]) + (date_of_birth[6]) + (date_of_birth[8]) + (date_of_birth[9]))
todaysdate_int = int((todays_date[0]) + (todays_date[1]) + (todays_date[2]) + (todays_date[3]) + (todays_date[5]) + (todays_date[6]) + (todays_date[8]) + (todays_date[9]))
date_difference = todaysdate_int - dateofbirth_int
print(todays_date)
print(dateofbirth_int)
print(todaysdate_int)
print(date_difference)

# date_1 = datetime.date(DOB)
# date_2 = datetime.date(todays_date)
# date_difference = date_1 - date_2
# print(date_difference)

# timedelta = todays_date - DOB 
# print(timedelta)



# DOB_str = DOB.isoformat()
# print(DOB_str)

# def calculate_age_years_months(date_of_birth):
#     date_today = date.today()
    
#     if date_today.month < date_of_birth.month:
#         age_in_months = (date_today.month - date_of_birth.month) + 12
#     elif date_today.month > date_of_birth.month:
#         age_in_months = (date_today.month - date_of_birth.month)

#     if (date_today.month > date_of_birth.month) and (todays_date.year - date_of_birth.year > 0):
#         age_in_years = (todays_date.year - date_of_birth.year)
#     elif (date_today.month < date_of_birth.month) and (todays_date.year - date_of_birth.year == 1):
#         age_in_years = 0
#     else:
#         age_in_years = 0

#     if age_in_years == 1:
#         result = f"{age_in_years} year old"
#     elif age_in_years > 1:
#         result = f"{age_in_years} years old"
#     else:
#         result = f"{age_in_months} months old"
#     return result

 

# print(calculate_age_years_months(DOB))



