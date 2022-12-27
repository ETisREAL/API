"""Add user table

Revision ID: 3c338f5493e2
Revises: c3b6f78afd22
Create Date: 2022-12-26 12:51:38.765175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c338f5493e2'
down_revision = 'c3b6f78afd22'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('email', sa.String, nullable=False),
    sa.Column('password', sa.String, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    )


def downgrade() -> None:
    op.drop_table('users')
    pass
