from flask import Flask, jsonify, request
from models.meals import Meal
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/meal-registration'

db.init_app(app)

@app.route('/meal/<int:id_meal>', methods=["GET"])
def getOne(id_meal):
    meal = Meal.query.get(id_meal)
    return jsonify(meal.to_dict())

@app.route('/meals', methods=["GET"])
def getAll():
    meals = Meal.query.all()
    return jsonify([meal.to_dict() for meal in meals])

@app.route('/meal', methods=["POST"])
def create():
    data = request.json
    if data:
        name = data.get("name")
        description = data.get("description")
        date = data.get("date")
        with_in = data.get("with_in")

        if name and date:
            meal = Meal(name=name, description=description, date=date, with_in=with_in)
            db.session.add(meal)
            db.session.commit()
            return jsonify({"message": "Registro criado com sucesso"})

    return jsonify({"message": f"Falha ao registrar a refeição!"}), 500

@app.route('/meal/<int:id_meal>', methods=["PUT"])
def edit(id_meal):
    meal = Meal.query.get(id_meal)
    data = request.json

    if meal and data:
        name        = data.get("name")
        description = data.get("description")
        date        = data.get("date")
        with_in     = data.get("with_in")

        if name:
            meal.name = name

        if date:
            meal.date = date

        if with_in:
            meal.with_in = with_in

        if description:
            meal.description = description

        db.session.commit()
        return jsonify({"message": "Registro atualizado com sucesso"})

    return jsonify({"message": f"Falha ao atualizar a refeição!"}), 500

@app.route('/meal/<int:id_meal>', methods=["DELETE"])
def remove(id_meal):
    meal = Meal.query.get(id_meal)

    if meal:
        db.session.delete(meal)
        db.session.commit()

        return({"message":"Registro deletado com sucesso!"})

    return jsonify({"message": "Erro ao deletar o registro"}), 404

if __name__ == '__main__':
    app.run(debug=True)