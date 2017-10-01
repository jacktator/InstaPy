from instapy import InstaPy

#if you don't provide arguments, the script will look for INSTA_USER and INSTA_PW in the environment

session = InstaPy(nogui=True)
session.login()

#Reduces the amount of time under sleep to a given percentage
#It might be useful to test the tool or to increase the time for slower connections (percentage > 100)
session.set_sleep_reduce(95)

#likes specified amount of posts for each hashtag in the array (the '#' is optional)
#in this case: 100 dog-posts and 100 cat-posts
session.like_by_tags(['#ethereal_moods', '#fairy', '#annoyingfairy', '#stylediaries', '#reading', '#visualoflife', '#openmyworld', '#inspiration', '#workhard', '#workharder', '#pinkmood', '#pinkmoodstyle', '#autumnmood', '#darkart', '#darkatmosphere', '#mondaymood ', '#happytimes ', '#visualoflife ', '#openmyworld ', '#bleachmyfilm ', '#picoftheday ', '#makestories ', '#breakdown ', '#shootaward ', '#stylediarie'], amount=100)

#likes specified amount of posts for each location in the array
#in this case: 100 posts geotagged at the chrysler building and 100 posts geotagged at the salton sea
session.like_by_locations(['c114925/sydney-australia/', 'c2721681/haymarket-australia/', 'c114893/surry-hills-australia/', 'c107428/bondi-australia/', 'c112089/mascot-australia/', 'c2687080/broadbeach-waters-australia/', 'c2719626/chippendale-australia/', 'c2673728/milsons-point-australia/', 'c115053/taren-point-australia/', 'c114925/sydney-australia/'], amount=100)

#gets tags from image passed as instagram-url and likes specified amount of images for each tag
# session.like_from_image(url='www.instagram.com/p/BSrfITEFUAM/', amount=5)

#likes 100 posts for each tag of your latest image
# session.like_from_image(amount=100)

#likes 50 photos of other animals

# session.like_by_tags(['#animals'], amount=50, media='Photo')
# session.like_from_image(url='www.instagram.com/image', amount=50, media='Photo')

#likes 15 videos of cats

# session.like_by_tags(['#cat'], amount=15, media='Video')
# session.like_from_image(url='www.instagram.com/image', amount=15, media='Video')

#Likes 10 random photo of geach given user

# session.like_by_users(usernames=['friend1', 'friend2', 'friend3'], amount=10, random=True, media='Photo')

#Interact with the people that a given user is following
#set_do_comment, set_do_follow and set_do_like are applicable
session.set_user_interact(amount=5, random=True, percentage=50, media='Photo')
session.set_do_follow(enabled=True, percentage=70)
session.set_do_like(enabled=True, percentage=70)
session.set_comments(["Nice Shot!", "Super!"])
session.set_do_comment(enabled=True, percentage=80)
session.interact_user_followers(['riiita_77',
'fx.tse',
'chenman135',
'bymins_',
'pattieung',
'_iamheraa',
'_iungyumi',
'jh,e',
'i_ioooo',
'm.ja77',
'samson_moi',
'istanbul',
'westcoast_exposures',
'travel_2_germany',
'guerojo',
'andrew_glatt',
'st_ella',
'karishashasha',
'hannurinne',
'alma_natuurfotografie'], amount=10, random=True)

session.end()
