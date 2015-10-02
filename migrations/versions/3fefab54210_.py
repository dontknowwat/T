"""empty message

Revision ID: 3fefab54210
Revises: 2b82d0e5595
Create Date: 2015-10-02 16:57:14.433919

"""

# revision identifiers, used by Alembic.
revision = '3fefab54210'
down_revision = '2b82d0e5595'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('roles_name_key', 'roles', type_='unique')
    op.drop_column('roles', 'id')
    op.add_column('users', sa.Column('role', sa.String(), nullable=True))
    op.create_foreign_key(None, 'users', 'roles', ['role'], ['name'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'role')
    op.add_column('roles', sa.Column('id', sa.INTEGER(), nullable=False))
    op.create_unique_constraint('roles_name_key', 'roles', ['name'])
    ### end Alembic commands ###