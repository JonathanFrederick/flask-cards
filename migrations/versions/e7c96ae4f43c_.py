"""empty message

Revision ID: e7c96ae4f43c
Revises: None
Create Date: 2016-07-24 16:38:29.046620

"""

# revision identifiers, used by Alembic.
revision = 'e7c96ae4f43c'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('pw_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    ### end Alembic commands ###
