"""Loading of initial data

Revision ID: 7bc9a7f71eea
Revises: 95f98cfe293f
Create Date: 2023-08-13 00:48:23.303389

"""
from alembic import op
import sqlalchemy as sa

from mosreg import models
from mosreg.services.user import create_user
from utils.initial_data import database_initialization


# revision identifiers, used by Alembic.
revision = '7bc9a7f71eea'
down_revision = '95f98cfe293f'
branch_labels = None
depends_on = None

def upgrade() -> None:

    # Add users
    users = [
        {'name':'Кожурин Сергей Сергеевич', 'email':'0', 'password':'0'},
        {'name':'Шляпников Гурий Александрович', 'email':'1', 'password':'1'},
        {'name':'Астахова Анна Евгеньевна', 'email':'2', 'password':'2'},
        {'name':'Мотузов Фёдор Сергеевич', 'email':'3', 'password':'3'},
        {'name':'Афонин Алексей Геннадьевич', 'email':'4', 'password':'4'},
        {'name':'Емелькин Василий Анатольевич', 'email':'4', 'password':'5'},
        {'name':'Устименко Марина Николаевна', 'email':'5', 'password':'6'}
        
        # Add more users as needed
    ]

    for user in users:
        
        database_initialization(user)


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
