"""empty message

Revision ID: 9f7a0ace2a6c
Revises: 3d8f34e83d23
Create Date: 2016-05-29 14:58:00.087740

"""

# revision identifiers, used by Alembic.
revision = '9f7a0ace2a6c'
down_revision = '3d8f34e83d23'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('author', sa.String(length=20), nullable=True),
    sa.Column('coverImage', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('author'),
    sa.UniqueConstraint('name')
    )
    op.create_table('book_chapter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book_chapter')
    op.drop_table('book')
    ### end Alembic commands ###
