from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.kennel_database
owners = db.owners
dogs = db.dogs


#Insert a new owner into the database
def add_owner(first_name, surname, email_address):
    print("Adding new owner: " + first_name + " " + surname + ", who can be contacted at " + email_address + ".")
    new_owner = owners.insert_one({'first_name': first_name, 'surname': surname, 'email_address': email_address})
    return new_owner.inserted_id


#Delete an owner from the database
def delete_owner(owner_id):
    owner_first_name = owners.find_one({'_id': owner_id})['first_name']
    owner_surname = owners.find_one({'_id': owner_id})['surname']
    print("Deleting owner: " + owner_first_name + " " + owner_surname)
    owners.delete_one({'_id': owner_id})


#Find an owner by the first and last name
def find_owner_by_name(first_name, surname):
    print("Finding owner: " + first_name + " " + surname)
    owner = owners.find_one({'first_name': first_name, 'surname': surname})
    print(first_name + " " + surname + " found.")
    return owner


#Update a user's email address
def update_owner_email(owner_id, new_email):
    owner_first_name = owners.find_one({'_id': owner_id})['first_name']
    owner_surname = owners.find_one({'_id': owner_id})['surname']
    owners.update_one({'_id': owner_id}, {"$set": {'email_address': new_email}})
    print(owner_first_name + " " + owner_surname + " now set to " + new_email + ".")


#Insert a new dog into the database
def add_dog(name, age, breed, owner_id):
    owner_first_name = owners.find_one({'_id': owner_id})['first_name']
    owner_surname = owners.find_one({'_id': owner_id})['surname']
    print("Adding new dog: " + name + ", who is a " + breed + " aged " + str(age) + " belonging to " + owner_first_name +
          " " + owner_surname + ".")
    new_dog = dogs.insert_one({'name': name, 'age': age, 'breed': breed, 'owner_id': owner_id})
    return new_dog.inserted_id


#Delete a dog from the database
def delete_dog(dog_id):
    dog_name = dogs.find_one({'_id': dog_id})['name']
    print("Deleting dog: " + dog_name)
    dogs.delete_one({'_id': dog_id})


#Find a dog by their name and breed
def find_dog(name, breed):
    print("Finding dog: " + name + ", the " + breed)
    dog = dogs.find_one({'name': name, 'breed': breed})
    print(name + " found with ObjectId " + str(dog['_id']) + ".")
    return dog


#Find a dog given its owner's ObjectId and the dog's name
def find_dog_for_owner(owner_id, name):
    owner = owners.find_one({'_id': owner_id})
    owner_first_name = owner['first_name']
    owner_surname = owner['surname']
    print("Finding the dog belonging to " + owner_first_name + " " + owner_surname + ".")
    dog = dogs.find_one({'owner_id': owner_id, 'name': name})
    print(name + " belongs to " + owner_first_name + " " + owner_surname + ".")
    return dog


#Find all of an owner's dogs given an owner's ObjectId
def find_dogs_for_owner(owner_id):
    owner = owners.find_one({'_id': owner_id})
    owner_first_name = owner['first_name']
    owner_surname = owner['surname']
    print("Finding the dogs belonging to " + owner_first_name + " " + owner_surname + ".")
    owner_dogs = dogs.find({'owner_id': owner_id})
    print("Found " + str(owner_dogs.count()) + " dogs belonging to " + owner_first_name + " " + owner_surname + ".")
    return owner_dogs


#Update a dog's age
def update_dog_age(dog_id, age):
    dog_name = dogs.find_one({'_id': dog_id})['name']
    print("Updating " + dog_name + "'s age to " + str(age))
    dogs.update_one({'_id': dog_id}, {"$set": {'age': age}})


def main():
    owner_id1 = add_owner("Adam", "Smith", "adam@smith.com")
    dog_id1 = add_dog("Spot", 4, "Collie", owner_id1)
    dog_id2 = add_dog("Skip", 7, "Labrador", owner_id1)
    find_owner_by_name("Adam", "Smith")
    find_dog("Spot", "Collie")
    find_dog_for_owner(owner_id1, "Skip")
    find_dogs_for_owner(owner_id1)
    update_owner_email(owner_id1, "adam@smith2.com")
    update_dog_age(dog_id1, 5)
    delete_owner(owner_id1)
    delete_dog(dog_id1)
    delete_dog(dog_id2)
    client.kennel_database.command("dropDatabase")

if __name__ == '__main__':
    main()