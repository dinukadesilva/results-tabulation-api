"""empty message

Revision ID: dac224818b28
Revises: dd1c192b77d1
Create Date: 2019-09-23 12:31:07.053321

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dac224818b28'
down_revision = 'dd1c192b77d1'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tallySheetVersionRow_CE_201_ballotBox')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tallySheetVersionRow_CE_201_ballotBox',
    sa.Column('tallySheetVersionRowId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('ballotBoxStationaryItemId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('invoiceStage', mysql.ENUM('Issued', 'Received'), nullable=False),
    sa.ForeignKeyConstraint(['ballotBoxStationaryItemId'], ['ballotBox.stationaryItemId'], name='tallySheetVersionRow_CE_201_ballotBox_ibfk_1'),
    sa.ForeignKeyConstraint(['tallySheetVersionRowId'], ['tallySheetVersionRow_CE_201.tallySheetVersionRowId'], name='tallySheetVersionRow_CE_201_ballotBox_ibfk_2'),
    sa.PrimaryKeyConstraint('tallySheetVersionRowId', 'ballotBoxStationaryItemId'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    ### end Alembic commands ###
