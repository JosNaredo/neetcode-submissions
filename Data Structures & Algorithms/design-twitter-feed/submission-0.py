class Twitter:

    def __init__(self):
        self.postedtweets = []
        self.followings = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postedtweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if self.postedtweets == []:
            return []
        extra_id = self.followings.get(userId) or []
        valid_id = [userId] + extra_id
        feed = [tweet[1] for tweet in self.postedtweets[::-1] if tweet[0] in valid_id]
        if len(feed) > 10:
            return feed[0:10]
        else:
            return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if self.followings.get(followerId) != None:
            if followeeId in self.followings[followerId]:
                pass
            else:
                self.followings[followerId].append(followeeId)
        else:
            self.followings[followerId] = [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.followings.get(followerId) != None:
            if followeeId in self.followings[followerId]:
                self.followings[followerId].remove(followeeId)
            else:
                pass
        else:
            self.followings[followerId] = [followeeId]
