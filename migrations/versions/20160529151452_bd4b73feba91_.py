"""empty message

Revision ID: bd4b73feba91
Revises: 9f7a0ace2a6c
Create Date: 2016-05-29 15:14:52.279067

"""

# revision identifiers, used by Alembic.
revision = 'bd4b73feba91'
down_revision = '9f7a0ace2a6c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.drop_index('author', table_name='book')
    op.drop_index('name', table_name='book')
    op.add_column('book_chapter', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.drop_index('name', table_name='book_chapter')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('name', 'book_chapter', ['name'], unique=True)
    op.drop_column('book_chapter', 'updated_at')
    op.create_index('name', 'book', ['name'], unique=True)
    op.create_index('author', 'book', ['author'], unique=True)
    op.drop_column('book', 'updated_at')
    ### end Alembic commands ###
