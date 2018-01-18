#craigslistScraper.py
#Created by Maxwell Oldshein

from bs4 import BeautifulSoup
import requests
import string
import re
import pprint as pp
import timeit

start = timeit.default_timer()
urlBase = 'http://boston.craigslist.com/search/ggg'

total = 0
paymentDictionary = {}
titles = []

print "Getting data..."

for i in range(0, 500, 100):
    print "Starting at result %d." % i
    rsp = requests.get(urlBase, params = {'is_paid' : 'yes', 's' : i})
    print "URL: %s" % rsp.url
    html = BeautifulSoup(rsp.text, 'html.parser')
    
    gigs = html.findAll('p', attrs = {'class' : 'result-info'})
    #print len(gigs)

    for gig in gigs:
        #print counter

        gigTitle = gig.find('a', attrs = {'class' : 'result-title hdrlnk'}).text
        #print gigTitle

        if (gigTitle not in titles):
            titles.append(gigTitle)
            
            gigDate = gig.find('time', attrs = {'class' : 'result-date'})['datetime'].encode('utf-8')
            gigDate = gigDate.split(" ")
            gigDate = gigDate[0]
            #print gigDate

            gigLink = gig.find('a', attrs = {'class' : 'result-title hdrlnk'})['href']
            #print gigLink
            gigURL =  gigLink
            gigRsp = requests.get(gigURL)
            #print gigRsp.url
            
            gigHtml = BeautifulSoup(gigRsp.text, 'html.parser')
            #print gigHtml.prettify()[:10000]

            compensation = gigHtml.find('b').text
            compensation = compensation.encode('utf-8')
            compensationParts = re.split(' |/|-', compensation.replace('$', '').replace('-', ' ').replace('+', '').replace(',', '').replace(".", " "))
            #print compensationParts
            
            for c in compensationParts:
                if (c.isdigit() == True ):
                    temp = int(c)

                    #Considering most of the compensations for the jobs are in hourly rates, I tried to create a system to turn all of the
                    #pay rates to hourly earnings.
                    #If the compensation is over $50 get the hourly rate (in order to avoid extremely large daily totals)
                    if (temp > 50):
                        temp = temp / 8
                    #If the compensation is over $500, assume that it is monthly, and then get the hourly rate of that as well.
                    elif (temp > 500):
                        temp = (temp / 30) / 8

                    #print "payment: %d" % temp

                    if (gigDate in paymentDictionary):
                        paymentDictionary[gigDate] += temp
                    elif (gigDate not in paymentDictionary):
                        paymentDictionary[gigDate] = temp
                    break


print "\nThe totals by day are:"
pp.pprint(paymentDictionary, width = 1)

for key in paymentDictionary.keys():
    total += paymentDictionary[key]

dailyAverage = total / (len(paymentDictionary))

stop = timeit.default_timer()

print "\nThe average earnings is about $%d per day." % round(dailyAverage)
print "Runtime: %d seconds." % (stop - start)
