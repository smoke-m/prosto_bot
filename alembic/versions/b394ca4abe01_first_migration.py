"""First migration

Revision ID: b394ca4abe01
Revises: 
Create Date: 2024-10-23 12:26:40.544790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b394ca4abe01'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('requestsinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_nic', sa.Text(), nullable=True),
    sa.Column('user_request', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usersinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_nic', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_nic')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usersinfo')
    op.drop_table('requestsinfo')
    # ### end Alembic commands ###
