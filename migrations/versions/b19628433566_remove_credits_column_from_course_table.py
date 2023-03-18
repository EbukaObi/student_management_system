"""remove credits column from course table

Revision ID: b19628433566
Revises: cd9d5e495fea
Create Date: 2023-03-18 02:40:34.257049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b19628433566'
down_revision = 'cd9d5e495fea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('course', schema=None) as batch_op:
        batch_op.drop_column('credits')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('course', schema=None) as batch_op:
        batch_op.add_column(sa.Column('credits', sa.INTEGER(), nullable=False))

    # ### end Alembic commands ###
