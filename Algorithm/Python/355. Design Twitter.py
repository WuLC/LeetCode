# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-10 14:17:08
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-10 14:18:53
# @Email: liangchaowu5@gmail.com


# referer: https://discuss.leetcode.com/topic/47838/python-solution
class Twitter(object):
    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)


    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))


    def getNewsFeed(self, userId):
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]


    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)


    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)