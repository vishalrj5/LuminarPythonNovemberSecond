#covid_data={
#    kerala:{"state":"kerala","confirmed_cases":500000,"cured":49000,"death":10000},

#}

f=open("covid_19_india.csv","r")
covid_data={}
for lines in f:
    print(lines)
    data=lines.rstrip("\n").lower().split("\t")
    state=data[3].rstrip("***")
    if state=="Telengana":
        state="Telengana"
    cured=data[6]
    death=data[7]
    confirmed=data[8]
    covid_data[state]={
        "state":state,
        "confirmed":confirmed,
        "cured":cured,
        "death":death
    }
for k,v in covid_data.items():
    print(k,v)
    #no,date,time,state,CI,CF,cure,death,confirm=words.rstrip("\n").split("\t")


def print_covid_data(**kwargs):
    #fetching value state
    state=kwargs["state"]
    if state in covid_data:
        print(state,",",covid_data[state]["confirmed"])
    else:
        print("invalid state")


print_covid_data(state="kerala")