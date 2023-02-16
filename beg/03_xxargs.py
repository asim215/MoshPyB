def save_user(**user):
    print(user)
    print(f"id: {user['id']}")
    print(f"name: {user['name']}")
    print(f"age: {user['age']}")


save_user(id=1, name="Josh", age=34)
