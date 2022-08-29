import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."

                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."

                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        #Check for duplicates
        username = data["username"]
        user = UserModel.find_by_username(username)
        if user:
            return {"message": "A user with that username already exist"}, 400

        #user = UserModel(data['username'], data['password'])
        user = UserModel(**data) #unpacking
        user.save_to_db()

        return {"message": "user created successfully."}, 201



