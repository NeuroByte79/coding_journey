def config_store():
    print("\n⚙️ CONFIG STORE SYSTEM\n")

    config = {}

    # Input + validation
    config["app_name"] = input("Enter app name: ")

    while True:
        try:
            config["version"] = float(input("Enter version (e.g., 1.0): "))
            break
        except:
            print("❌ Invalid version, try again")

    debug_input = input("Enable debug mode (yes/no): ").lower()
    config["debug"] = True if debug_input == "yes" else False

    while True:
        try:
            config["max_users"] = int(input("Enter max users: "))
            if config["max_users"] > 0:
                break
            else:
                print("❌ Must be positive")
        except:
            print("❌ Invalid number")

    # Display config
    print("\n📦 CONFIG SUMMARY")
    print("="*40)
    for key, value in config.items():
        print(f"{key:<12}: {value}")
    print("="*40)


config_store()