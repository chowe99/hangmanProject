"""Scores and words table

Revision ID: 48ffdb3b0c9d
Revises: 21d344a0b144
Create Date: 2022-05-12 15:14:50.367245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48ffdb3b0c9d'
down_revision = '21d344a0b144'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('words',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=60), nullable=True),
    sa.Column('definition', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_words_definition'), 'words', ['definition'], unique=True)
    op.create_index(op.f('ix_words_word'), 'words', ['word'], unique=True)
    op.create_table('scores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number_of_guesses', sa.Integer(), nullable=True),
    sa.Column('recorded', sa.Date(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('word_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['word_id'], ['words.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_scores_recorded'), 'scores', ['recorded'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_scores_recorded'), table_name='scores')
    op.drop_table('scores')
    op.drop_index(op.f('ix_words_word'), table_name='words')
    op.drop_index(op.f('ix_words_definition'), table_name='words')
    op.drop_table('words')
    # ### end Alembic commands ###
