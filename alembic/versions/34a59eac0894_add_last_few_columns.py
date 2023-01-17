"""add_last_few_columns

Revision ID: 34a59eac0894
Revises: 5ec9372c0949
Create Date: 2023-01-11 17:08:30.297781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34a59eac0894'
down_revision = '5ec9372c0949'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("published",sa.Boolean(),server_default="True",nullable=False))
    op.add_column("posts",sa.Column("created_at",sa.TIMESTAMP(timezone=True),nullable =False,server_default=sa.text('now()')))
    pass
    


def downgrade() -> None:
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    pass
