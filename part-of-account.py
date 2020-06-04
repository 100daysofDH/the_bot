# here, in the actual document, authentication credentials are placed

#-------------------------------------------------------------------------------

main_hashtag = '#100daysofDH'

#tweeting_at_me = '@100DaysofDH' # TODO ignorecase

trailing_hashtags = '#100DaysofDH #100DaysofCode #dh #digitalhumanities'

# Hashtags which need to be present / are retweet-worthy on their own
# or in combination with the main_hashtag
#-------------------------------------------------------------------------------

#TODO don't retweet all of the just primary hashtags, there are such bots already
# but retweet if a combination of primary and secondary is there
primary_hashtags = ['#dh', '#digitalhumanities', '#WomenOfDH', '#DHlife']
# Hashtags which should only be retweeted if a primary one is present too
secondary_hashtags = ['#100DaysofDissertation', '#dissertating', \
                      '#100DaysofCode', '#womenwhocode', '#acwri', \
                      '#CodeNewbie', '#DHfromScratch', '#DataSittersClub', \
                      '#womenintech']

#-------------------------------------------------------------------------------

mention_replies = ['Keep up the good work!', 'Keep up the great work', \
                   'Keep going!', 'The #100DaysofDH bot is proud of you! :)', \
                   '#DH rulez!', '#digitalhumanities matter and #HumanitiesMatter'\
                   ]
#-------------------------------------------------------------------------------

users_to_follow = ['ProgHist', 'dhawards', 'DayofDH']
#-------------------------------------------------------------------------------

mon = ['It\'s #CodeNewbie question hour! What are your challenges for #100DaysofDH? What questions do you have for us? #dh and cheers to #MondayMotivation #DHchallengePrompt', \
      'Share your #MondayMotivation for the #100DaysofDH challenge. What #dh work will you tackle today? #MondayMorning #DHchallengePrompt', \
      'Are you motivated to start into a new week of #100DaysofDH? #MondayMood #MondayMotivation #DHchallengePrompt']
tues = ['What do you think are new trends in the #dh? #TuesdayTalk #100DaysofDH #DHchallengePrompt', \
        'What #dh discovery did you make lately which surprised you? #TuesdayTruth #100DaysofDH #DHchallengePrompt', \
        'What is your current favourite tool/software in #dh? #TechTuesday at #100DaysofDH #DHchallengePrompt', \
        'Which tools do you use which are relatively uncommon in the #dh that the #100DaysofDH community should know about? #TechTuesday #DHchallengePrompt', \
        'Showcase your stunning data transformations on #TransformationTuesday! #100DaysofDH #DHchallengePrompt', \
        'What would you like to tell your former self who was just starting out in the #dh? #100DaysofDH #TuesdayTreat #TuesdayTip #DHchallengePrompt']
wed = ['What will you do for your #WednesdayWorkout (#100DaysofDH challenge related, of course)? #DHchallengePrompt', \
       'What have you learned during your #100DaysofDH challenge? #WednesdayWisdom #DHchallengePrompt', \
       'It is #WomxnsWednesday! Praise some #WomeninDH who recently helped you with #dh work and link them here!  #WomenAlsoKnowDH #DHchallengePrompt' ]
thurs = ['Share your successes and experiences with #100DaysofDH for #ThrowbackThursday! #DHchallengePrompt', \
         'What experience in the #dh are you thankful for? #ThankfulThursday #DHchallengePrompt']
fri = ['What\'s planned as today\'s #100DaysofDH #FridayFun? #DHchallengePrompt', \
       'Will you work on #100DaysofDH during the weekend or do you prefer to take time off? #WeekendVibes #DHchallengePrompt', \
       'Are you ready for a break or getting ready to get going? #ThankGodItsFriday! #DHchallengePrompt', \
       'Nominate a #WomenofDH on this #FemlaeFriday! We could all use some more great #dh womxn to follow! #DHchallengePrompt', \
       'It\'s #FemaleFriday and #WomenAlsoKnowDH. Whom should we follow? #womenwhocode #WomenofDH  #WomenAlsoKnowDH #DHchallengePrompt']
sat = ['Are you still sleepy or already productive on this #SaturdayMorning? #DHchallengePrompt', \
       'Please nominate a scholar or project which highlights #DHDiversity for this #SaturdaySpotlight! #dh #DHchallengePrompt']
sun = ['What about using this Sunday to do some reading for #100DaysofDH? #WeekendVibes #SundayRead #DHchallengePrompt', \
       'Share something with us for #ScienceSunday! #100DaysofDH-related would be good too ;) #DHchallengePrompt', \
       'Please nominate scholars and projects for #SpotlightSunday who showcase diversity in the #dh/#DHDiversity! #DHchallengePrompt']

week = [mon, tues, wed, thurs, fri, sat, sun]
