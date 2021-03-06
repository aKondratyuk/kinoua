"""empty message

Revision ID: 455ffc9d0cae
Revises: 
Create Date: 2020-02-06 22:36:15.779881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '455ffc9d0cae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('director',
    sa.Column('director_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('director_id')
    )
    op.create_table('movie',
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('url', sa.String(length=1255), nullable=False),
    sa.Column('imdbrating', sa.Float(precision=10), nullable=False),
    sa.Column('ratingcount', sa.Float(precision=10), nullable=False),
    sa.Column('director_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['director_id'], ['director.director_id'], ),
    sa.PrimaryKeyConstraint('title'),
    sa.UniqueConstraint('url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie')
    op.drop_table('director')
    # ### end Alembic commands ###
