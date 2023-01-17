"""add_foregein_key

Revision ID: 5ec9372c0949
Revises: 54ea5c6d1ec4
Create Date: 2023-01-11 16:41:54.531318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ec9372c0949'
down_revision = '54ea5c6d1ec4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("owner_id",sa.Integer(),nullable=False))
    op.create_foreign_key("post_users_fk",source_table="posts",referent_table="users",
                          local_cols=["owner_id"],remote_cols=["id"],ondelete="CASCADE")

    pass

def downgrade() -> None:
    op.drop_constraint("post_users_fk",table_name="posts")
    op.drop_column("posts","owner_id")
        
    pass
