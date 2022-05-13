"""last_seen field added to User

Revision ID: 1604db4e9b29
Revises: a56452e99997
Create Date: 2022-05-13 11:27:59.475347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1604db4e9b29'
down_revision = 'a56452e99997'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    # ### end Alembic commands ###