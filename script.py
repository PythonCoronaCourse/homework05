class BigCat:
    sound = ""

    def __init__(self):
        self.bored = True

    def roar(self):
        print(self.sound)
        self.bored = False


class Tiger(BigCat):  # notice that Tiger is inheriting "roar" method from BigCat
    sound = "ROAR"  # we're only setting a sound it will make


class Lion(BigCat):  # notice that Lion is inheriting "roar" method from BigCat
    sound = "GRRAU"  # we're only setting a sound it will make


# notice that functions below are NOT a part of any of the classes above
def perform_cats_routine(cats):
    """" big cats like to roar if they're bored. this function looks
    at all the provided cats and if they're bored makes them roar """
    for cat in cats:
        if cat.bored:
            cat.roar()


def bore_a_cat(cat):
    """ this function takes a cat and makes them bored """
    cat.bored = True


# we're creating a list of big cats
joe_exotics_zoo = [Tiger(), Lion(), Lion(), Tiger(), Tiger()]

perform_cats_routine(joe_exotics_zoo)  # each cat should roar
perform_cats_routine(joe_exotics_zoo)  # no cat should roar, because they're not bored anymore

bore_a_cat(joe_exotics_zoo[0])
bore_a_cat(joe_exotics_zoo[2])

perform_cats_routine(joe_exotics_zoo)  # only one tiger and one lion should roar

 # 