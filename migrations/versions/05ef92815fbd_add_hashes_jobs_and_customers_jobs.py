"""Add jobs per customer and per hashfile

Revision ID: 05ef92815fbd
Revises: d6a54eeeaeb9
Create Date: 2020-12-28 12:29:49.628089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05ef92815fbd'
down_revision = 'd6a54eeeaeb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('customer_id', sa.Integer(), nullable=False))
    op.add_column('jobs', sa.Column('hashfile_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'jobs', 'customers', ['customer_id'], ['id'])
    op.create_foreign_key(None, 'jobs', 'hashfiles', ['hashfile_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'jobs', type_='foreignkey')
    op.drop_constraint(None, 'jobs', type_='foreignkey')
    op.drop_column('jobs', 'hashfile_id')
    op.drop_column('jobs', 'customer_id')
    # ### end Alembic commands ###