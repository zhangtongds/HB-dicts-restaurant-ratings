import sys

def restaurant_rating(filename):
    restaurant_ratings = {}
    """Restaurant rating lister."""

    with open(filename) as f:
        for line in f:
            #words = line.split(":")
            key = line[:-3]
            value = line[-2]
            restaurant_ratings[key] = value
            # print "{} is rated at {}.".format(key, value)

        # print restaurant_ratings
        return restaurant_ratings

# def sorted_restaurant_rating(restaurant_ratings):
#     """ Take the dictionary and return it sorted """

#     # restaurant_ratings = restaurant_rating(filename)
#     restaurant_names = sorted(restaurant_ratings)
#     for restaurant in restaurant_names:
#         print "{} is rated at {}.".format(restaurant, restaurant_ratings[restaurant])

# restaurant_ratings = restaurant_rating(sys.argv[1])
# sorted_restaurant_rating(restaurant_ratings)



def sorted_restaurant_rating(filename):
    """ Take the dictionary and return it sorted """
    rest_lst = restaurant_ratings.items()
    sorted_rest_lst = sorted(rest_lst)
    for restaurant, rating in sorted_rest_lst:
        print "{} is rated at {}.".format(restaurant, rating)

restaurant_ratings = restaurant_rating(sys.argv[1])
sorted_restaurant_rating(restaurant_ratings)
