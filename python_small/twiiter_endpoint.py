import pandas
import tweepy
import random

consumer_token = "lD5SvfXnghwgz9jqmMqwM1lAt"
consumer_secret = "bGFCu6Ng0I7Sc4pGJO1C6TCuwLdAFxFAULdhIrIaZw2xhPGY1X"
access_token = "1144482016995319808-BAjmzkJPJPXVnYk79shvP2ummZLuiQ"
access_secret = "1ujVelMRHBaKT6ean7wMegCLT73CPj3o7fRb3Ykfih3Vr"

auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)


hash_tags_for_c = ["#1MillionSlaves","#greencardbacklog","#discrimination"]

hash_tag_for_s = ["#studyabroad","#HigherEducation","#GMAT","#GRE",'#F1Visa',"#MS","#MBA"]

hash_tag_for_college = ["#iitmadras",'#iitdelhi',"#iitkanpur","#iitpatna","#iitindore","#iitgoa","#iitjamu",\
                        "#iitkgp","#iitjodhpur","#iitropar","#iitbhilai","#AIMS"]

sentences = ["Indian's SHOULD AVOID #USA for #highereducation using #f1Visa . They are in 90+ YEAR BACKLOG",\
            "There is no #AmericanDream for #Indian students looking for #highereducation. 1.1 Million still waiting for #greencard", \
            "More than 1.1 Million #Indian #legal #immigrants including kids and women in 90+ YEARS Greencard BACKLOG. ",\
            "There is no #equality in for #Indian #students in #USA due to 90 + YEARS BACKLOG", \
            "Students from India SHOULD BE AWARE that there is a 90 + YEARS Backlog for #Indians in #USA",\
            "DREAM of #equality remains unfulfilled as long as DISCRIMINATION continues with 'COUNTRY OF BIRTH' in #USA",\
            "100s of folks have literally died waiting in backlog! 100k+ kids will be deported turning 21! ",\
            "The green card backlog for employment-based immigrants in 2020 has surpassed 1.2 million applicants @CatoInstitute" ]


new_tweet = random.choice(sentences) + " "+ random.choice(hash_tags_for_c) + " " +  \
random.choice(hash_tag_for_s) + " " + random.choice(hash_tag_for_college) 

print(len(new_tweet))

# if len(new_tweet) <= 140:
#     api.update_status(new_tweet)
# else:
#     None

print(new_tweet)








