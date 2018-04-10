import sys
from random import choice
# restaurant_ratings = {}

def restaurant_rating(filename):
    """Restaurant rating lister."""
    restaurant_ratings = {}

    with open(filename) as f:
        for line in f:
            #words = line.split(":")
            key = line[:-3]
            value = line[-2]
            restaurant_ratings[key] = value
            # print "{} is rated at {}.".format(key, value)
        # prin t restaurant_ratings
    return restaurant_ratings


def sorted_restaurant_rating(restaurant_ratings):
    """ Take the dictionary and return it sorted """
    rest_lst = restaurant_ratings.items()
    sorted_rest_lst = sorted(rest_lst)
    for restaurant, rating in sorted_rest_lst:
        print "{} is rated at {}.".format(restaurant, rating)

def add_ratings(restaurant_ratings):
    nums = [1, 2, 3, 4, 5]
    restaurant_name = raw_input("Please input a restaurant name: ")
    rating = raw_input("Please input rating for {}: ".format(restaurant_name))
    while True:
        try:
            if int(rating) in nums:
                restaurant_ratings[restaurant_name] = rating
                break
            else:
                rating = raw_input("Please enter a rating between 1-5: ")
        except ValueError:
            rating = raw_input("Please enter a number: ")
            
def random_update_rating(restaurant_ratings):
    restaurant = choice(restaurant_ratings.items())
    print "{} is chosen, the rating is {}.".format(restaurant[0], restaurant[1])
    updated_rating = raw_input("Please enter a number 1 - 5 to update the rating: ")
    nums = [1, 2, 3, 4, 5]
    while True:
        try:
            if int(updated_rating) in nums:
                restaurant_ratings[restaurant[0]] = updated_rating
                break
            else:
                updated_rating = raw_input("Please enter a updated_rating between 1-5: ")
        except ValueError:
            updated_rating = raw_input("Please enter a number to update the rating: ")
    return restaurant_ratings

def user_update_rating(restaurant_ratings):
    restaurants = restaurant_ratings.items()
    print "Please choose the restaurants below: "
    for key, value in restaurants:
        print key
    user_choice = raw_input("Please choose a restaurant: ")
    
    while True:
        if user_choice in restaurant_ratings.keys():
            print "You chose {}, the rating is {}.".format(user_choice, restaurant_ratings[user_choice])
            updated_rating = raw_input("Please update the rating for {}: ".format(user_choice))
            nums = [1, 2, 3, 4, 5]
            while True:
                try:
                    if int(updated_rating) in nums:
                        restaurant_ratings[user_choice] = updated_rating
                        print "The updated rating for {} is {}. ".format(user_choice, updated_rating)
                        print "======================="
                        print "The sorted list of restaurants: "
                        break
                    else:
                        updated_rating = raw_input("Please enter a updated_rating between 1-5: ")
                except ValueError:
                    updated_rating = raw_input("Please enter a number to update the rating: ")
            break
        else:
            user_choice = raw_input("Please choose a restaurant WITHIN the list: ")


ratings = restaurant_rating(sys.argv[1])

# add_ratings(ratings)

# random_update_rating(ratings)


user_update_rating(ratings)

sorted_restaurant_rating(ratings)
