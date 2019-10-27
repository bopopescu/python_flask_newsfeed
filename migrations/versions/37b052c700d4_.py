"""empty message

Revision ID: 37b052c700d4
Revises: 767f54325786
Create Date: 2019-10-24 12:52:15.793543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37b052c700d4'
down_revision = '767f54325786'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'notes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('notes', sa.VARCHAR(length=1000), nullable=True))
    # ### end Alembic commands ###