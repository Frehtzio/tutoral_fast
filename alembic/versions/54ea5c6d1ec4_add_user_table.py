"""add_user_table


Revision ID: 54ea5c6d1ec4
Revises: 66dbef85621f
Create Date: 2023-01-11 16:22:29.403422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54ea5c6d1ec4'
down_revision = '66dbef85621f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id",sa.Integer(),nullable=False),
                    sa.Column("email",sa.String(),nullable=False),
                    sa.Column("password",sa.String(),nullable=False),
                    sa.Column("created_at",sa.TIMESTAMP(timezone=True),
                              server_default = sa.text("now()"),nullable=False),
                    sa.PrimaryKeyConstraint("id"),  #esto hace que id se vuelava una key hay mas de una manera de hacer las cosas
                    sa.UniqueConstraint("email")
    )
    pass


def downgrade() -> None:
    op.drop_column("users")
    pass
