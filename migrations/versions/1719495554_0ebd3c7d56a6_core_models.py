"""core-models

Revision ID: 0ebd3c7d56a6
Revises: 
Create Date: 2024-06-27 17:09:14.084015

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0ebd3c7d56a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('invoices',
    sa.Column('id', sa.String(length=26), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('receipts',
    sa.Column('id', sa.String(length=26), nullable=False),
    sa.Column('type', mysql.ENUM('Deposit', 'Withdraw'), nullable=False),
    sa.Column('status', mysql.ENUM('Init', 'Pending', 'Accepted', 'Declined', 'Canceled'), nullable=False),
    sa.Column('meta', mysql.JSON(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wallets',
    sa.Column('id', sa.String(length=26), nullable=False),
    sa.Column('type', mysql.ENUM('Business', 'Safe'), nullable=False),
    sa.Column('available_amount', sa.Integer(), nullable=False),
    sa.Column('blocked_amount', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.String(length=26), nullable=False),
    sa.Column('status', mysql.ENUM('Applied', 'Scheduled', 'Canceled'), nullable=False),
    sa.Column('type', mysql.ENUM('Applied', 'Scheduled', 'Canceled'), nullable=False),
    sa.Column('amount', sa.INTEGER(), nullable=False),
    sa.Column('source_id', sa.String(length=26), nullable=False),
    sa.Column('target_id', sa.String(length=26), nullable=False),
    sa.Column('receipt_id', sa.String(length=26), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['receipt_id'], ['receipts.id'], ),
    sa.ForeignKeyConstraint(['source_id'], ['wallets.id'], ),
    sa.ForeignKeyConstraint(['target_id'], ['wallets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('invoice_items',
    sa.Column('id', sa.String(length=26), nullable=False),
    sa.Column('invoice_id', sa.String(length=26), nullable=False),
    sa.Column('transaction_id', sa.String(length=26), nullable=False),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoices.id'], ),
    sa.ForeignKeyConstraint(['transaction_id'], ['transactions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('invoice_items')
    op.drop_table('transactions')
    op.drop_table('wallets')
    op.drop_table('receipts')
    op.drop_table('invoices')
    # ### end Alembic commands ###