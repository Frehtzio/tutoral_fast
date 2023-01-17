"""create post table

Revision ID: 39b192c854e9
Revises: 
Create Date: 2023-01-09 13:17:29.541744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39b192c854e9'
down_revision = None
branch_labels = None
depends_on = None

# solo se puede upgradear una vez
def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('title',sa.Integer(),nullable=False))
    

def downgrade() -> None:
    op.drop_table('posts')
    pass
