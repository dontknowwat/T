"""empty message

Revision ID: 2b82d0e5595
Revises: 484dda3ac68
Create Date: 2015-10-02 16:11:39.937807

"""

# revision identifiers, used by Alembic.
revision = '2b82d0e5595'
down_revision = '484dda3ac68'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('languages',
    sa.Column('language_code', sa.String(length=10), nullable=False),
    sa.Column('language_name', sa.String(length=100), nullable=False),
    sa.Column('dir', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('language_code'),
    sa.UniqueConstraint('language_name')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('creation_time', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('modification_time', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('translator_languages',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('language_code', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['language_code'], ['languages.language_code'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'language_code')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('translator_languages')
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('languages')
    ### end Alembic commands ###