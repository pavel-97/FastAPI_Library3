"""update book

Revision ID: e77d91ced52c
Revises: 742505d2ab3b
Create Date: 2023-08-27 19:15:54.536573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e77d91ced52c'
down_revision = '742505d2ab3b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Book', sa.Column('author_id', sa.Integer(), nullable=False))
    op.drop_column('Book', 'author')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Book', sa.Column('author', sa.VARCHAR(length=128), autoincrement=False, nullable=False))
    op.drop_column('Book', 'author_id')
    # ### end Alembic commands ###