from datetime import datetime

from app import models, db
from flask import current_app as app, jsonify, abort, request


@app.route('/users', methods=['GET'])
def get_users():
    """Возвращает список пользователей."""
    users = db.session.query(models.User).all()
    return jsonify([user.serialize() for user in users])


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Возвращает пользователя по ID."""
    user = db.session.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        abort(404)

    return jsonify(user.serialize())


@app.route('/orders', methods=['GET'])
def get_orders():
    """Возвращает список заказов."""
    orders = db.session.query(models.Order).all()
    return jsonify([order.serialize() for order in orders])


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Возвращает заказ по ID."""
    order = db.session.query(models.Order).filter(models.Order.id == order_id).first()

    if order is None:
        abort(404)

    return jsonify(order.serialize())


@app.route('/offers', methods=['GET'])
def get_offers():
    """Возвращает список предложений."""
    offers = db.session.query(models.Offer).all()
    return jsonify([offer.serialize() for offer in offers])


@app.route('/offers/<int:offer_id>', methods=['GET'])
def get_offer(offer_id):
    """Возвращает предложение по ID."""
    offer = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()

    if offer is None:
        abort(404)

    return jsonify(offer.serialize())


@app.route('/users', methods=['POST'])
def create_user():
    """Создание пользователя."""
    data = request.json

    db.session.add(models.User(**data))

    db.session.commit()

    return {}


@app.route('/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    """Редактирование пользователя."""
    data = request.json

    user = db.session.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        abort(404)

    db.session.query(models.User).filter(models.User.id == user_id).update(data)
    db.session.commit()
    return {}


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Удаление пользователя."""
    result = db.session.query(models.User).filter(models.User.id == user_id).delete()

    if result == 0:
        abort(404)

    db.session.commit()

    return {}


@app.route('/orders', methods=['POST'])
def create_order():
    """Создание заказа"""
    data = request.json

    data['start_date'] = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
    data['end_date'] = datetime.strptime(data['end_date'], '%Y-%m-%d').date()

    db.session.add(models.Order(**data))

    db.session.commit()

    return {}


@app.route('/orders/<int:order_id>', methods=['PUT'])
def edit_order(order_id):
    """ Обновление заказа с заданным ID"""
    data = request.json

    order = db.session.query(models.Order).filter(models.Order.id == order_id).first()

    if order is None:
        abort(404)

    data['start_date'] = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
    data['end_date'] = datetime.strptime(data['end_date'], '%Y-%m-%d').date()

    db.session.query(models.Order).filter(models.Order.id == order_id).update(data)

    db.session.commit()
    return {}


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Удаление заказа по ID."""
    result = db.session.query(models.Order).filter(models.Order.id == order_id).delete()

    if result == 0:
        abort(404)

    db.session.commit()

    return {}


@app.route('/offers', methods=['POST'])
def create_offer():
    """Создание предложения."""
    data = request.json

    db.session.add(models.Offer(**data))

    db.session.commit()

    return {}


@app.route('/offers/<int:offer_id>', methods=['PUT'])
def edit_offer(offer_id):
    """Редактирование предложения."""
    data = request.json

    offer = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()
    if offer is None:
        abort(404)

    db.session.query(models.Offer).filter(models.Offer.id == offer_id).update(data)
    db.session.commit()
    return {}


@app.route('/offers/<int:offer_id>', methods=['DELETE'])
def delete_offer(offer_id):
    """Удаление предложения по ID."""
    result = db.session.query(models.Offer).filter(models.Offer.id == offer_id).delete()

    if result == 0:
        abort(404)

    db.session.commit()

    return {}
