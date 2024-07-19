"""core-models

Revision ID: ab729e5b81e2
Revises: 
Create Date: 2024-07-19 11:48:07.240124

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ab729e5b81e2'
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
    sa.Column('slug', sa.String(length=26), nullable=False),
    sa.Column('type', mysql.ENUM('Safe', 'Business', 'IPG', 'Commission', 'Settlement'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wallets_slug'), 'wallets', ['slug'], unique=False)
    op.create_table('transactions',
    sa.Column('id', sa.String(length=26), nullable=False),
    sa.Column('type', mysql.ENUM('CashIn', 'CashOut', 'Payment', 'PaymentRefund', 'Commission', 'CommissionRefund', 'Unblock'), nullable=False),
    sa.Column('safe', sa.BOOLEAN(), nullable=False),
    sa.Column('amount', sa.INTEGER(), nullable=False),
    sa.Column('source_id', sa.String(length=26), nullable=True),
    sa.Column('safe_source_id', sa.String(length=26), nullable=True),
    sa.Column('target_id', sa.String(length=26), nullable=True),
    sa.Column('safe_target_id', sa.String(length=26), nullable=True),
    sa.Column('receipt_id', sa.String(length=26), nullable=True),
    sa.Column('invoice_id', sa.String(length=26), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoices.id'], ),
    sa.ForeignKeyConstraint(['receipt_id'], ['receipts.id'], ),
    sa.ForeignKeyConstraint(['safe_source_id'], ['wallets.id'], ),
    sa.ForeignKeyConstraint(['safe_target_id'], ['wallets.id'], ),
    sa.ForeignKeyConstraint(['source_id'], ['wallets.id'], ),
    sa.ForeignKeyConstraint(['target_id'], ['wallets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_index(op.f('ix_wallets_slug'), table_name='wallets')
    op.drop_table('wallets')
    op.drop_table('receipts')
    op.drop_table('invoices')
    # ### end Alembic commands ###
