"""empty message

Revision ID: 42513f92c30
Revises: 2efebda9e62
Create Date: 2015-10-02 19:34:13.493961

"""

# revision identifiers, used by Alembic.
revision = '42513f92c30'
down_revision = '2efebda9e62'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'roles', ['name'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'roles', type_='unique')
    op.drop_column('roles', 'id')
    ### end Alembic commands ###
