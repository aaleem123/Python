from bell_module import HairAccessories, GenderWise, HairWigs


def module_function():
    men_one = GenderWise("black", "123", "round", "Pk", "strong")
    print(men_one.color)
    print(men_one.power())
    print(men_one.goodlooking())


def new_function():
      # Using HairWigs class
    natural_wig = HairWigs("red", "125$", "bob", "England", "strong", "natural")
    print(natural_wig.material)
    print("#######################################")
    print("Next Participant")
    print("#######################################")
    print()


def main():
    ## Using HairWigs class
    natural_wig = HairWigs("red", "125$", "bob", "England", "strong", "natural")
    print(natural_wig.material)
    print("#######################################")
    print("Next Participant")
    print("#######################################")
    print( )

    # Using HairAccessories class
    pony_lex = HairAccessories("red", 12, "round", "Paris", "strong")
    print()
    print(pony_lex.color)
    print(pony_lex.where_from())
    print(pony_lex.power())
    print()
    print("#######################################")
    print("Next Participant")
    print("#######################################")
    print()

    # Using another instance of HairAccessories
    clip_alex = HairAccessories("black", 14, "block", "US", "weak")
    print(clip_alex.color)
    print(clip_alex.where_from())
    print(clip_alex.power())


if __name__ == "__main__":
    module_function()
    new_function()
    main()



