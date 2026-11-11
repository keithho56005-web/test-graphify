from auth import register_user, login


def main():
    register_user("kiet@example.com", "123456")
    print(login("kiet@example.com", "123456"))


if __name__ == "__main__":
    main()
