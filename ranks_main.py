from ranks import User

if __name__ == "__main__":
    user = User()
    print(user.rank)  # => -8
    print(user.progress)  # => 0
    user.inc_progress(-7)
    print(user.progress)  # => 10
    user.inc_progress(-5)  # will add 90 progress
    print(user.progress)  # => 0 # progress is now zero
    print(user.rank)  # => -7 # rank was upgraded to -7