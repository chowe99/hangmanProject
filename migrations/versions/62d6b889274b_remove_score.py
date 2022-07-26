"""remove score

Revision ID: 62d6b889274b
Revises: 07eed8e407c5
Create Date: 2022-05-23 12:40:38.186857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62d6b889274b'
down_revision = '07eed8e407c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('scores', 'number_of_guesses')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('scores', sa.Column('number_of_guesses', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###