"""add_contenct_toclumn

Revision ID: 66dbef85621f
Revises: 39b192c854e9
Create Date: 2023-01-09 13:41:44.826530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66dbef85621f'
down_revision = '39b192c854e9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("content",sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_column("posts","content") 
