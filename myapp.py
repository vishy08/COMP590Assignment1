import requests, json

def get_name():
    myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhRUTkiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJyZXMgcmxvYyByd2VpIHJociBydGVtIiwiZXhwIjoxNjYxMzUwODMzLCJpYXQiOjE2NjA3NDYwMzN9.-6KKpR38nXavOTwsBrJBKuMQD3thwGeFDguLTMiOPM0"}
    myurl = "https://api.fitbit.com/1/user/-/profile.json"
    resp = requests.get(myurl, headers=myheader).json()
    print(resp["user"]["fullName"])

def get_heartrate():
    myheader = {"Authorization":"Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSNkIiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBybnV0IHJwcm8gcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkyMjk1NDQ0LCJpYXQiOjE2NjA3NTk0NDR9.bILcGIrPRXPWRrWBZDKRLsZdtTKKqPUpZ4NZZ-U3k5g"}
    myurl = "https://api.fitbit.com/1/user/-/activities/heart/date/2022-08-24/1d/1min.json"
    resp = requests.get(myurl, headers=myheader).json()
    time = resp["activities-heart-intraday"]["dataset"][-1]["time"]
    value = resp["activities-heart-intraday"]["dataset"][-1]["value"]
    print("your most recent heart rate recorded at " + str(time) + " AM is " + str(value) + " beats per minute")
    
def get_steps():
    myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhRUTkiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJyZXMgcmxvYyByd2VpIHJociBydGVtIiwiZXhwIjoxNjYxMzUwODMzLCJpYXQiOjE2NjA3NDYwMzN9.-6KKpR38nXavOTwsBrJBKuMQD3thwGeFDguLTMiOPM0"}
    myurl = "https://api.fitbit.com/1/user/-/activities/list.json?afterDate=2019-01-01&sort=asc&offset=0&limit=2"
    resp = requests.get(myurl, headers=myheader).json()
    totalSteps = resp["activities"][-1]["steps"]
    print("your total step count today is " + str(totalSteps) + " steps.")

def get_sleep():
    myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhRUTkiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJyZXMgcmxvYyByd2VpIHJociBydGVtIiwiZXhwIjoxNjYxMzUwODMzLCJpYXQiOjE2NjA3NDYwMzN9.-6KKpR38nXavOTwsBrJBKuMQD3thwGeFDguLTMiOPM0"}
    myurl = "https://api.fitbit.com/1.2/user/-/sleep/date/2022-08-17.json"
    resp = requests.get(myurl, headers=myheader).json()
    sleep = resp["summary"]["totalMinutesAsleep"]
    print("you slept for " + str(sleep) + " minutes last night.")

def get_activeness():
    myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhRUTkiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJyZXMgcmxvYyByd2VpIHJociBydGVtIiwiZXhwIjoxNjYxMzUwODMzLCJpYXQiOjE2NjA3NDYwMzN9.-6KKpR38nXavOTwsBrJBKuMQD3thwGeFDguLTMiOPM0"}
    myurl = "https://api.fitbit.com/1/user/-/activities/date/2019-01-01.json"
    resp = requests.get(myurl, headers=myheader).json()
    sedentaryMinutes = resp["summary"]["sedentaryMinutes"]
    veryActive = resp["summary"]["veryActiveMinutes"]
    print("today, you were sedentary for " + str(sedentaryMinutes) + " minutes and active for " + str(veryActive) + " minutes in the very high activity zone.")


get_name()

get_heartrate()

get_steps()

get_sleep()

get_activeness()