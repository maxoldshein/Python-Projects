import praw

def main():
    reddit = praw.Reddit(client_id = 'JsqdPAndPA4D2w', client_secret = 'JaJWZadZ5nG6k9ZOl10PY-Z_iKU', user_agent = '"mo_application', username = "pythonscripttester", password = "python")

    subreddit = raw_input("Enter a subreddit: ")
    submissionLimit = input("Enter the numer of posts you want to see (limitted to 100): ")

    try:
        sr = reddit.subreddit(subreddit).top(limit=submissionLimit)
    except Exception as e:
        print "You didn't enter a valid subreddit!"
        return
    
    print "The top " + str(submissionLimit) + " submissions for /r/" + subreddit

    counter = 1
    
    for submission in sr:
       print str(counter) + ". Title: " + submission.title
       print "\tScore: " + str(submission.score)
       print "\tComments: " + str(submission.num_comments)
       counter = counter + 1
       
main()
