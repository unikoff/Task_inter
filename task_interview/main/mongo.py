import pymongo
client = pymongo.MongoClient('mongodb+srv://unik:passwordnikita@cluster0.sgpxixb.mongodb.net/?retryWrites=true&w=majority')
db = client.Mongo_test
coll = db.recipe


def recipe_add(recipe: dict):
    query = {"recipe": recipe['recipe_id']}
    recipedb = [item for item in coll.find(query)]
    if recipedb:
        weight = int(recipe['weight'])
        weight += int(recipedb[0].get(recipe['product_id'])) if recipedb[0].get(recipe['product_id']) else 0
        fil = {"recipe": recipe['recipe_id']}
        data = {"$set": {recipe['product_id']: weight}}
        coll.update_one(fil, data)
        print(1)
    else:
        coll.insert_one({"recipe": recipe['recipe_id'], recipe['product_id']: int(recipe['weight'])})
        print(2)


def cook_recipe(recipe: dict):
    fil = {"recipe": recipe['recipe_id']}
    recipedb = [item for item in coll.find(fil)]
    count = 1
    count += recipedb[0].get('count') if recipedb[0].get('count') else 0
    data = {"$set": {'count': count}}
    coll.update_one(fil, data)


def show_table(recipe: dict):
    list_final = []
    for item in coll.find():
        if item:
            product = int(item.get(recipe['product_id'])) if item.get(recipe['product_id']) else 100
            if (item.get(recipe['product_id']) is None) or product < 10:
                list_final.append(item)
    return list_final