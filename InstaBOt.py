import requests                                                            #library for sending request over internet
import urllib                                                              #for downloading an image
from textblob import TextBlob                                              #for positive and negative comments setiments analysis
from textblob.sentiments import NaiveBayesAnalyzer

# at=Access token and bu=base url


at=''
bu='https://api.instagram.com/v1/'


#function for otaining self insta profile info of the user


def self_info():
    request_url=bu+"users/self/?access_token="+at
    print "Get request url: "+request_url
    user_info=requests.get(request_url).json()
    if user_info['meta']['code']==200:
        if len(user_info['data'])>0:
            print "User Id:"+user_info['data']['id']
            print "User Name:"+user_info['data']['username']
            print "Full Name:"+user_info['data']['full_name']
            print "Bio:\n"+user_info['data']['bio']
            print "Following:"+str(user_info['data']['counts']['follows'])
            print "Followed by:"+str(user_info['data']['counts']['followed_by'])
            print "Total Posts:"+str(user_info['data']['counts']['media'])
        else:
            print"User doesn't Exist."
    else:
        print 'Status code other than 200 received.'



#function for obtaining the profile id for any user by username


def get_user_id(user_name):
    request_url = bu +"users/search?q="+user_name+"&access_token="+ at
    print "Get request url:"+request_url
    user_info = requests.get(request_url).json()
    if user_info['meta']['code']==200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()



#function for getting the profile info of any other user by entering username


def get_user_info(user_name):
    user_id=get_user_id(user_name)
    if user_id==None:
        print "User do not exist."
    else:
        request_url = bu +"users/"+user_id+"/?access_token="+ at
        print "Get request url:" + request_url
        user_info = requests.get(request_url).json()
        if user_info['meta']['code'] == 200:
            if len(user_info['data']) > 0:
                print "User Id:" + user_info['data']['id']
                print "User Name:" + user_info['data']['username']
                print "Full Name:" + user_info['data']['full_name']
                print "Bio:\n" + user_info['data']['bio']
                print "Following:" + str(user_info['data']['counts']['follows'])
                print "Followed by:" + str(user_info['data']['counts']['followed_by'])
                print "Total Posts:" + str(user_info['data']['counts']['media'])
            else:
                print"User doesn't Exist."
        else:
            print 'Status code other than 200 received.'


#function for downloading the recent post of own profile


def get_own_post():
    request_url = bu +"users/self/media/recent/?access_token="+ at
    print "Get request url:" + request_url
    own_media = requests.get(request_url).json()
    if own_media['meta']['code']==200:
        if len(own_media['data'])>0:
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            caption=own_media['data'][0]['caption']['text']
            likes=str(own_media['data'][0]['likes']['count'])
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
            if caption == 'null':
                print "No Caption Added."
                print "likes:" + likes
            else:
               print "Image Caption:"+caption
               print "likes:"+likes
        else:
            print 'Post does not exist!'
    else:
        print "Status code other than 200 received."

    return own_media['data'][0]['id']





max_like=[]
min_like=[]
max_comment=[]
min_comment=[]
Caption=[]


#function for downloading the recent post of any other user profile

def get_users_post(user_name):
    user_id=get_user_id(user_name)
    if user_id==None:
        print"User Doesn't exist. "
    else:
        caption = None
        request_url=bu+"users/"+user_id+"/media/recent/?access_token="+at
        print "Get request url:" + request_url
        user_media = requests.get(request_url).json()
        if user_media['meta']['code'] == 200:
            if len(user_media['data']) > 0:
                print "1.See post with max. likes.\n2.See post with least likes.\n3.See post With maximum comments.\n4.See post with minimum comments.\n5.See post by caption.\n6.See the most recent post."
                post_choice=int(raw_input("Enter your choice."))
                if post_choice==1:
                    for x in user_media['data']:
                        max_like.append(x['likes']['count'])
                    list_max=max(max_like)
                    index=max_like.index(list_max)
                    image_name = user_media['data'][index]['id'] + '.jpeg'
                    image_url = user_media['data'][index]['images']['standard_resolution']['url']
                    if user_media['data'][index]['caption']:
                        caption = user_media['data'][index]['caption']['text']
                    likes = str(user_media['data'][index]['likes']['count'])
                    urllib.urlretrieve(image_url, image_name)
                    print 'Your image has been downloaded!'
                    if caption == None:
                        print "No Caption Added."
                        print "likes:" + likes
                    else:
                        print "Image Caption:" + caption
                        print "likes:" + likes
                elif post_choice==2:
                    for x in user_media['data']:
                        min_like.append(x['likes']['count'])
                    list_min=min(min_like)
                    index=min_like.index(list_min)
                    image_name = user_media['data'][index]['id'] + '.jpeg'
                    image_url = user_media['data'][index]['images']['standard_resolution']['url']
                    if user_media['data'][index]['caption']:
                        caption = user_media['data'][index]['caption']['text']
                    likes = str(user_media['data'][index]['likes']['count'])
                    urllib.urlretrieve(image_url, image_name)
                    print 'Your image has been downloaded!'
                    if caption == None:
                        print "No Caption Added."
                        print "likes:" + likes
                    else:
                        print "Image Caption:" + caption
                        print "likes:" + likes
                elif post_choice==3:
                    for x in user_media['data']:
                        max_comment.append(x['comments']['count'])
                    comment_max=max(max_comment)
                    index=max_comment.index(comment_max)
                    image_name = user_media['data'][index]['id'] + '.jpeg'
                    image_url = user_media['data'][index]['images']['standard_resolution']['url']
                    if user_media['data'][index]['caption']:
                        caption = user_media['data'][index]['caption']['text']
                    likes = str(user_media['data'][index]['likes']['count'])
                    urllib.urlretrieve(image_url, image_name)
                    print 'Your image has been downloaded!'
                    if caption == None:
                        print "No Caption Added."
                        print "likes:" + likes
                    else:
                        print "Image Caption:" + caption
                        print "likes:" + likes
                elif post_choice==4:
                    for x in user_media['data']:
                        min_comment.append(x['comments']['count'])
                    comment_min=min(min_comment)
                    index=min_comment.index(comment_min)
                    image_name = user_media['data'][index]['id'] + '.jpeg'
                    image_url = user_media['data'][index]['images']['standard_resolution']['url']
                    if user_media['data'][index]['caption']:
                        caption = user_media['data'][index]['caption']['text']
                    likes = str(user_media['data'][index]['likes']['count'])
                    urllib.urlretrieve(image_url, image_name)
                    print 'Your image has been downloaded!'
                    if caption == None:
                        print "No Caption Added."
                        print "likes:" + likes
                    else:
                        print "Image Caption:" + caption
                        print "likes:" + likes


                elif post_choice==5:
                    for x in user_media['data']:
                        if x['caption']:
                            Caption.append(x['caption']['text'])
                        else:
                            Caption.append('No caption')
                    a=raw_input("Enter a caption related word.")
                    for y in Caption:
                        if a in y:
                            c=Caption.index(y)
                            image_name = user_media['data'][c]['id'] + '.jpeg'
                            image_url = user_media['data'][c]['images']['standard_resolution']['url']
                            likes = str(user_media['data'][c]['likes']['count'])
                            urllib.urlretrieve(image_url, image_name)
                            print 'Your image has been downloaded!'
                            print "Likes:"+likes
                            print "Your word was found in Caption: "+y
                        else:
                            print "Caption not found in any post."
                            break


                elif post_choice==6:
                    image_name = user_media['data'][0]['id'] + '.jpeg'
                    image_url = user_media['data'][0]['images']['standard_resolution']['url']
                    if user_media['data'][0]['caption']:
                        caption = user_media['data'][0]['caption']['text']
                    likes = str(user_media['data'][0]['likes']['count'])
                    urllib.urlretrieve(image_url, image_name)
                    print 'Your image has been downloaded!'
                    if caption == None:
                        print "No Caption Added."
                        print "likes:" + likes
                    else:
                        print "Image Caption:" + caption
                        print "likes:" + likes
            else:
                "No Post Exit."
        else:
            print "Status code other than 200 received."

#function for obtaing the id  of the recent media post

def post_id(user_name):
    user_id=get_user_id(user_name)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = bu + "users/" + user_id + "/media/recent/?access_token=" + at
    print "Get request url:" + request_url
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()



#function for like a post by entering username


def like_post(user_name):
    media_id=post_id(user_name)
    request_url=bu+"media/"+media_id+"/likes"
    print "Post request url:"+request_url
    payload={"access_token":at}
    print "Post request url:"+request_url
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'


def recent_media_liked(user_name):
    request_url=bu+"users/self/media/liked?access_token="+at
    print "Get request url:"+request_url
    like_info= requests.get(request_url).json()
    if like_info['meta']['code']==200:
        if len(like_info['data']) > 0:
            media_name = like_info['data'][0]['id'] + '.jpeg'
            media_url = like_info['data'][0]['images']['standard_resolution']['url']
            caption = like_info['data'][0]['caption']['text']
            likes = str(like_info['data'][0]['likes']['count'])
            Comments=str(like_info['data'][0]['comments']['count'])
            urllib.urlretrieve(media_url, media_name)
            print 'Your image has been downloaded!'
            if caption == 'null':
                print "No Caption Added."
                print "likes:" + likes
                print "Comments:"+Comments
            else:
                print "Image Caption:" + caption
                print "likes:" + likes
                print "Comments:" + Comments
        else:
            print 'Post does not exist!'
    else:
        print "Status code other than 200 received."






#function for commenting on a post

def post_comment(user_name):
    media_id=post_id(user_name)
    comment_text = raw_input("Your comment: ")
    payload={"access_token": at ,"text" : comment_text}
    request_url = bu+"media/"+media_id+"/comments"
    print "Post request url:" + request_url
    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"


#function for accessing list of comments and then deleting them if necessary

def comment_list_and_delete_comment(user_name):
    media_id = post_id(user_name)
    request_url = bu + "media/" + media_id + "/comments?access_token=" + at
    print "Get request url:" + request_url
    comment_info = requests.get(request_url).json()
    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']) > 0:
            counter=1
            for x in range(0, len(comment_info['data'])):
                comment_text = comment_info['data'][x]['text']
                print str(counter)+"."+comment_text
                counter=counter+1
            print "Do you want delete the comments ?"
            delete_choice=raw_input("Enter your choice (Y/N). ")
            if delete_choice.upper()=="Y":
                y=int(raw_input("Select Comment "))-1
                comment_id=comment_info['data'][y]['id']
                delete_url = bu + "media/" + media_id + "/comments/" + comment_id + "?access_token=" + at
                print 'DELETE request url : %s' % (delete_url)
                delete_info = requests.delete(delete_url).json()

                if delete_info['meta']['code'] == 200:
                    print "Comment successfully deleted!\n"
                else:
                    print 'Unable to delete comment!'
            elif delete_choice.upper()=="N":
                print "No comment deleted."
        else:
            print "There is no comment on the post"
    else:
        print "Status Code other than 200 received."


#function for automatically deleting the negative comments of the post



def delete_negative_comment(user_name):
    media_id=post_id(user_name)
    request_url=bu+"media/"+media_id+"/comments?access_token="+at
    print "Get request url:"+request_url
    comment_info=requests.get(request_url).json()
    if comment_info['meta']['code']==200:
        if len(comment_info['data'])>0:
            counter = 1
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                print str(counter) + "." + comment_text
                counter = counter + 1
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = bu+"media/"+media_id+"/comments/"+comment_id+"?access_token="+at
                    delete_url = bu + "media/" + media_id + "/comments/" + comment_id + "?access_token=" + at
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print "Comment successfully deleted!\n"
                    else:
                        print 'Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)
                counter=counter+1

        else:
            print "There is no comment on the post"
    else:
        print "Status Code other than 200 received."




def targeted_comments(user_name):
    user_id = get_user_id(user_name)
    if user_id == None:
        print"User Doesn't exist. "
    else:
        request_url = bu + "users/" + user_id + "/media/recent/?access_token=" + at
        print "Get request url:" + request_url
        user_media = requests.get(request_url).json()
        if user_media['meta']['code'] == 200:
            if len(user_media['data']) > 0:
                for x in user_media['data']:
                    if x['caption']:
                        Caption.append(x['caption']['text'])
                    else:
                        Caption.append('No caption')
                a = raw_input("Enter a caption related word.")
                for y in Caption:
                    if a in y:
                        c = Caption.index(y)
                        print "Your word was found in Caption: " + y
                        media_id =user_media['data'][c]['id']
                        comment_text = raw_input("Your comment: ")
                        payload = {"access_token": at, "text": comment_text}
                        request_url = bu + "media/" + media_id + "/comments"
                        print "Post request url:" + request_url
                        make_comment = requests.post(request_url, payload).json()

                        if make_comment['meta']['code'] == 200:
                            print "Successfully added a new comment!"
                        else:
                            print "Unable to add comment. Try again!"


                    else:
                        print "Caption not found in any post."
                        break
            else:
                print "There is no comment on the post"
        else:
           print "Status Code other than 200 received."


#Hello world message and asking user's name


name=raw_input("Hi,I'm InstaBot and what's your good name?\n")
print "Welcome to InstaBot"+" "+name

#function for starting the application and performing various actions


#menu prints and asks user for his/hers choice

def start_instabot():
    menu=True
    while menu==True:
        print "What's on your mind ?\n" + "1.Get own details.\n" + "2.Get a user's details.\n" + "3.See your recent post.\n" + "4.See a user's Post\n" + "5.Like a post\n" +"6.See recent Media Liked by a User.\n"+ "7.Comment on a Post\n" + "8.Delete a comment.\n" + "9.Delete negative comments.\n"+"10.Do targeted comments.\n"+"11.Exit Application."
        menu_choice = int(raw_input("Enter your choice."))
        if menu_choice == 1:
            print "Your Bio:\n"
            self_info()
        elif menu_choice == 2:
            user_name = raw_input("Enter Username.")
            print "User's Bio:\n"
            get_user_info(user_name)
        elif menu_choice == 3:
            print "Your recent post."
            get_own_post()
        elif menu_choice == 4:
            user_name = raw_input("Enter Username.")
            print "User's recent Post:\n"
            get_users_post(user_name)
        elif menu_choice == 5:
            user_name = raw_input("Enter username")
            like_post(user_name)
        elif menu_choice == 6:
            user_name = raw_input("Enter username")
            recent_media_liked(user_name)
        elif menu_choice == 7:
            user_name = raw_input("Enter username")
            post_comment(user_name)
        elif menu_choice == 8:
            user_name = raw_input("Enter username")
            comment_list_and_delete_comment(user_name)
        elif menu_choice == 9:
            user_name = raw_input("Enter username")
            delete_negative_comment(user_name)
        elif menu_choice==10:
            user_name=raw_input("Enter username.")
            targeted_comments(user_name)
        elif menu_choice==11:
            menu=False

#instabot get started by calling the start bot function


start_instabot()
