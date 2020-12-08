f=open("Covid_19_India.csv","r")

covid_data={}
for lines in f:
    data=lines.rstrip("\n").lower().split(",")
    print(data)
    state=data[3].rstrip("***")
    if state=="telengana":
        state="telangana"
    cures=data[6]
    death=data[7]
    confirmed=data[8]
    covid_data[state]={

        "state":state,
        "confirmed":confirmed,
        "cuvered":cures,
        "death":death
    }
for k,v in covid_data.items():
    print(k,v)


def print_covid_data(**kwargs):
    state=kwargs["state"]
    if state in covid_data:
        print(state,",",covid_data[state]["confirmed"])
    else:
        print("invalid")


print_covid_data(state="kerala")
