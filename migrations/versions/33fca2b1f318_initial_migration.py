"""Initial migration.

Revision ID: 33fca2b1f318
Revises: 
Create Date: 2020-09-24 17:26:53.560484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33fca2b1f318'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('actors', sa.Column('description', sa.String(), nullable=True))
    op.add_column('movies', sa.Column('genres', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movies', 'genres')
    op.drop_column('actors', 'description')
    # ### end Alembic commands ###
