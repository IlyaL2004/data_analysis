"""fix id

Revision ID: 588bf1dbaa4a
Revises: 0ae5b0230029
Create Date: 2025-02-03 14:51:21.911963

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '588bf1dbaa4a'
down_revision: Union[str, None] = '0ae5b0230029'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_visits_id'), 'visits', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_visits_id'), table_name='visits')
    # ### end Alembic commands ###
