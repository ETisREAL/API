"""Add content column to posts table

Revision ID: c3b6f78afd22
Revises: 9904a6fb43af
Create Date: 2022-12-26 12:47:04.038199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3b6f78afd22'
down_revision = '9904a6fb43af'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', 
    sa.Column('content', sa.String, nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
