class Receta:
    def __init__(self, id, url, image, name, description, author, rattings, ingredients, steps, nutrients, times, serves, difficult, vote_count, subcategory, dish_type, maincategory):
        self.id = id
        self.url = url
        self.image = image
        self.name = name
        self.description = description
        self.author = author
        self.rattings = rattings
        self.ingredients = ingredients
        self.steps = steps
        self.nutrients = nutrients
        self.times = times
        self.serves = serves
        self.difficult = difficult
        self.vote_count = vote_count
        self.subcategory = subcategory
        self.dish_type = dish_type
        self.maincategory = maincategory

    def mostrar_receta(self):
        print(f"Nombre de la receta: {self.name}")
        print(f"Descripción: {self.description}")
        print(f"Autor: {self.author}")
        print(f"Ingredientes: {self.ingredients}")
        print(f"Pasos: {self.steps}")

