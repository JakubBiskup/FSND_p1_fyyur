"""empty message

Revision ID: 15cdc8379861
Revises: adba278300be
Create Date: 2020-01-03 11:44:11.028203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15cdc8379861'
down_revision = 'adba278300be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'state')
    op.drop_column('Artist', 'name')
    op.drop_column('Venue', 'state')
    op.drop_column('Venue', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('Venue', sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    op.add_column('Artist', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('Artist', sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
