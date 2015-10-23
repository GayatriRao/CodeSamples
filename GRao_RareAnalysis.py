
'''
Author: Gayatri Rao, Septemper 2015

Use Facebook's API and other open APIs of your choosing to compare Rare's Facebook posts 
(facebook.com/rare) to one of its competitors such as IJ Review (facebook.com/IjReview) 
or The Verge (facebook.com/verge). Choose 2 of the following to analyze:

- Post frequency and/or timing
'''

from facepy import GraphAPI
import json
import pylab as pl
from datetime import datetime

access = '<access token>' #add your access token here
graph = GraphAPI(access)

def getPosts(page):
    data = graph.get(page+'/posts?fields=message', page=True, retry=5)
    post = []
    for each in data:
        post.append(each)
    return post

def getCreatedTime(page):
    '''
    get time of creation of the original post so that we can 
    calculate posting frequency from it.
    '''
    data1= graph.get(page+'/posts?fields=created_time&limit=1', page=True, retry=5)
    times=[]
    i=0
    for data in data1:
        if data['data']:
            tmp = data['data'][0]['created_time']
            date = datetime.strptime(tmp, '%Y-%m-%dT%H:%M:%S+0000').date() #parse out the date from each time
            times.append(date.day)
            #print data['data'][0]['created_time']
    return times

def getPostFreq(times):
    '''
    get the daily posting frequency based on the list with times in it.
    '''
    freqs = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0, '24': 0, '25': 0, '26': 0, '27': 0, '28': 0, '29': 0, '30': 0, '31': 0}
    for each in times:
        if each < 1 | each > 31:
            print("Invalid date found")
        #if date is less than 1 or greater than 31 print error
        else:
            freqs[str(each)] += 1
    return freqs

if __name__ == '__main__':
    #Get the times when the posts were added
    verge_times = getCreatedTime('verge')
    rare_times = getCreatedTime('rare')
    #get frequencies for rare and the verge
    verge_freqs = getPostFreq(verge_times)
    rare_freqs = getPostFreq(rare_times)
    #plot the frequencies 
    pl.plot(verge_freqs.keys(), verge_freqs.values(), 'bv', label='verge')
    pl.plot(rare_freqs.keys(), rare_freqs.values(), 'rv', label='rare')
    pl.legend()
    pl.xlabel('Date')
    pl.ylabel('Daily Posting Frequency')
    pl.title('Daily posting frequency for Rare and Verge for dates 9/22-9/30:')
    pl.show()


