age_user = int(input())
if age_user <= 16:
    print("Lion King")
elif age_user >= 17 and age_user <= 25:
    print("Trainspotting")
elif age_user >= 26 and age_user <= 40:
    print("Matrix")
elif age_user >= 41 and age_user <= 60:
    print("Pulp Fiction")
else:
    print("Breakfast at Tiffany's")
