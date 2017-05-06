from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.kennel_database
owners = db.owners
dogs = db.dogs


#Insert a new owner into the database
def add_owner(first_name, surname, email_address):
    new_owner = owners.insert_one({'first_name': first_name, 'surname': surname, 'email_address': email_address,
                                   'dog_id': None})
    return new_owner.inserted_id


#Delete an owner from the database
def delete_owner(owner_id):
    owners.delete_one({'_id': owner_id})


#Find an owner by the first and last name
def find_owner_by_name(first_name, surname):
    owner = owners.find_one({'first_name': first_name, 'surname': surname})
    return owner


#Update a user's email address
def update_owner_email(owner_id, new_email):
    owners.update_one({'_id': owner_id}, {"$set": {'email_address': new_email}})


#Insert a new dog into the database
def add_dog(name, age, breed):
    new_dog = dogs.insert_one({'name': name, 'age': age, 'breed': breed})
    return new_dog.inserted_id


#Updates the owner document with their dog's ObjectId
def add_dog_owner(dog_id, owner_id):
    owners.update_one({'_id': owner_id}, {"$set": {'dog_id': dog_id}})


#Delete a dog from the database
def delete_dog(dog_id):
    dogs.delete_one({'_id': dog_id})


#Find a dog by their name and breed
def find_dog(name, breed):
    dog = dogs.find_one({'name': name, 'breed': breed})
    return dog


#Find a dog given its owner's ObjectId
def find_dog_by_owner(owner_id):
    owner = owners.find_one({'_id': owner_id})
    dog_id = owner['dog_id']
    dog = dogs.find_one({'_id': dog_id})
    return dog


#Update a dog's age
def update_dog_age(dog_id, age):
    dogs.update_one({'_id': dog_id}, {"$set": {'age': age}})
