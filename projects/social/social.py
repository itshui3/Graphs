from random import shuffle
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        if num_users < avg_friendships:
            return -1
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user('Auto-Generated User')
        # Create friendships
        howMany = num_users * avg_friendships // 2
        friendshipSet = set()

        for person in self.users:
            for friend in self.users:
                if friend != person and (friend, person) not in friendshipSet:
                    friendshipSet.add((person, friend))

        possibleFriendships = []
        for friendTup in friendshipSet:
            possibleFriendships.append(friendTup)
        shuffle(possibleFriendships)

        connectThese = possibleFriendships[:howMany]

        for cT in connectThese:
            self.add_friendship(cT[0], cT[1])
        
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visitedResult = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # Get Neighbors
        neighbors = self.friendships[user_id]

        q = Queue()
        visitSet = set()
        visitSet.add(user_id)

        q.enqueue((user_id, 0))
        visitedResult[user_id] = [user_id]

        while q.size() > 0:
            pointFriend, separation = q.dequeue()

            neighbors = self.friendships[pointFriend]

            if len(neighbors) > 0:
                for n in neighbors:
                    if n not in visitSet:
                        q.enqueue((n, separation + 1))
                        visitSet.add(n)
                        visitedResult[n] = visitedResult[pointFriend] + [n]
        return visitedResult


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    lengthTotal = 0
    for i, c in connections.items():
        lengthTotal += len(c)

    print(lengthTotal // 1000)

    # to create 100 users with avg of 10 friends each, how many times would you need to call add_friendship? 
    # Answer:***: 500 times, because each call adds 2 friendships

    # 1k users with 5 avg friend, what % of other users will be in a particular user's extended social network? what is avg degree of separation between a user and those in their extended network? 

