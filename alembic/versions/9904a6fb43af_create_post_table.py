"""create post table

Revision ID: 9904a6fb43af
Revises: 
Create Date: 2022-12-26 12:36:35.189762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9904a6fb43af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', 
    sa.Column('id', sa.Integer, nullable=False, primary_key=True),
    sa.Column('title', sa.String, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('posts')
    pass
