import requests, json

def get_name():
    myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhRTkQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBybnV0IHJwcm8gcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkyMzIyMzQ0LCJpYXQiOjE2NjA3ODYzNDR9.-kAqRq3x5D5J0nCgzOm-2ATMbz9e7EZYXUiitEt6h4k"}
    myurl = "https://api.fitbit.com/1/user/-/profile.json"
    resp = requests.get(myurl, headers=myheader).json()
    print(resp["user"]["fullName"])

def get_heartrate():
    myheader = {"Authorization":"Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhRTkQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBybnV0IHJwcm8gcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkyMzIyMzQ0LCJpYXQiOjE2NjA3ODYzNDR9.-kAqRq3x5D5J0nCgzOm-2ATMbz9e7EZYXUiitEt6h4k"}
    myurl = "https://api.fitbit.com/1/user/-/activities/heart/date/2022-08-24/1d/1min.json"
    resp = requests.get(myurl, headers=myheader).json()
    time = resp["activities-heart-intraday"]["dataset"][-1]["time"]
    value = resp["activities-heart-intraday"]["dataset"][-1]["value"]
    print("your most recent heart rate recorded at " + str(time) + " AM is " + str(value) + " beats per minute")
    
def get_steps():
    myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhRTkQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBybnV0IHJwcm8gcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkyMzIyMzQ0LCJpYXQiOjE2NjA3ODYzNDR9.-kAqRq3x5D5J0nCgzOm-2ATMbz9e7EZYXUiitEt6h4k"}
    myurl = "https://api.fitbit.com/1/user/-/activities/date/2022-08-24.json"
    resp = requests.get(myurl, headers=myheader).json()
    totalSteps = resp["summary"]["steps"]
    #print(resp)
    print("your total step count today is " + str(totalSteps) + " steps.")

def get_sleep():
    myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhRTkQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBybnV0IHJwcm8gcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkyMzIyMzQ0LCJpYXQiOjE2NjA3ODYzNDR9.-kAqRq3x5D5J0nCgzOm-2ATMbz9e7EZYXUiitEt6h4k"}
    myurl = "https://api.fitbit.com/1.2/user/-/sleep/date/2022-08-24.json"
    resp = requests.get(myurl, headers=myheader).json()
    sleep = resp["summary"]["totalMinutesAsleep"]
    print("you slept for " + str(sleep) + " minutes last night.")

def get_activeness():
    myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhRTkQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBybnV0IHJwcm8gcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkyMzIyMzQ0LCJpYXQiOjE2NjA3ODYzNDR9.-kAqRq3x5D5J0nCgzOm-2ATMbz9e7EZYXUiitEt6h4k"}
    myurl = "https://api.fitbit.com/1/user/-/activities/date/2022-08-24.json"
    resp = requests.get(myurl, headers=myheader).json()
    sedentaryMinutes = resp["summary"]["sedentaryMinutes"]
    veryActive = resp["summary"]["veryActiveMinutes"]
    print("today, you were sedentary for " + str(sedentaryMinutes) + " minutes and active for " + str(veryActive) + " minutes in the very high activity zone.")


get_name()

get_heartrate()

get_steps()

get_sleep()

get_activeness()