import sys

restaurant_ratings = {}

def restaurant_rating(filename):
    """Restaurant rating lister."""
    #restaurant_ratings = {}

    with open(filename) as f:
        for line in f:
            #words = line.split(":")
            key = line[:-3]
            value = line[-2]
            restaurant_ratings[key] = value
            # print "{} is rated at {}.".format(key, value)
        # print restaurant_ratings
        return restaurant_ratings

def sorted_restaurant_rating(restaurant_ratings):
    """ Take the dictionary and return it sorted """
    rest_lst = restaurant_ratings.items()
    sorted_rest_lst = sorted(rest_lst)
    for restaurant, rating in sorted_rest_lst:
        print "{} is rated at {}.".format(restaurant, rating)

def add_ratings():
    restaurant_name = raw_input("Please input a restaurant name: ")
    rating = raw_input("Please input rating for {}: ".format(restaurant_name))
    restaurant_ratings[restaurant_name] = rating
    return restaurant_ratings

add_ratings()
restaurant_ratings = restaurant_rating(sys.argv[1])
sorted_restaurant_rating(restaurant_ratings)
