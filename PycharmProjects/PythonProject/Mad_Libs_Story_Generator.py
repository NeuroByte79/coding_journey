def mad_libs():
    print("\n🎭 MAD LIBS STORY GENERATOR\n")

    name = input("Enter a name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    food = input("Enter a food: ")

    story = f"""
    One day, {name} went to {place}.
    Suddenly, a {adjective} {animal} appeared!
    It started to {verb} loudly.

    {name} was shocked, but then offered it some {food}.
    The {animal} became friendly and they became best friends!

    THE END 🚀
    """

    print("\n📖 Your Story:")
    print(story)

# Run
mad_libs()