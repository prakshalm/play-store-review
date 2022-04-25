import re

#LEADER APP
userMessage="""Google Play, City Mall Live

★☆☆☆☆ English
फ्रॉड फाउंडेशन की जगह
_by_ <https://www.google.com/search?q=%22ShivBharat-__-Yadav00220%22|ShivBharat Yadav> _for v1.30.9 () -_  · <https://watch.appfollow.io/apps/my-first-workspace/reviews/56176?review_id=917686285&amp;utm_medium=slack&amp;utm_source=reviews&amp;utm_campaign=reply&amp;autologin=236483:95e0da652c4a6fdbd206204d31e3bf36474201424133dfa0b75749973c93f0e6:1650551048&amp;t=r|Reply> · <https://appfollow.io/gp/10556/review/917686285?s=global4&amp;utm_medium=slack&amp;utm_source=reviews&amp;utm_campaign=permalink|Permalink> · <https://appfollow.io/gp/10556/review/917686285?s=global4&amp;action=translate&amp;utm_medium=slack&amp;utm_source=reviews&amp;utm_campaign=translate|Translate> · <https://watch.appfollow.io/apps/my-first-workspace/reviews/56176?review_id=917686285&amp;utm_medium=slack&amp;utm_source=reviews&amp;utm_campaign=add_tag&amp;autologin=236483:95e0da652c4a6fdbd206204d31e3bf36474201424133dfa0b75749973c93f0e6:1650551048&amp;t=r|Add tag>"""

userMessage=userMessage.split(" ")
for data in userMessage:
    returned_value=re.search(r"<https://www\.google\.com/search\?q=%22",data,re.IGNORECASE)
    if returned_value:
        userName=returned_value.string
        print(userName)
        
        #removing unnecessary symbols from the userName
        userName=userName.replace("<https://www.google.com/search?q=%22","")
        userName=userName.replace("+"," ")
        userName=userName.replace("%22","")
        userName=userName.replace("|"," ")
        userName=userName.replace("_","")
        userName=userName.replace("-","")
        userName = ''.join([i for i in userName if not i.isdigit()])    #removing digits from the userName
        userName=userName.split(" ")
        print(userName)
        userName=str(userName[0]+" "+userName[1])
        print(userName)