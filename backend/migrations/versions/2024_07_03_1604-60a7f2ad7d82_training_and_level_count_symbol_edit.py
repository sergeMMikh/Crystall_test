"""Training and Level count symbol edit

Revision ID: 60a7f2ad7d82
Revises: 65bfd6911a75
Create Date: 2024-07-03 16:04:46.701708

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60a7f2ad7d82'
down_revision: Union[str, None] = '65bfd6911a75'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('TrainingLevels', 'level',
               existing_type=sa.VARCHAR(length=35),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.create_unique_constraint(None, 'TrainingLevels', ['id'])
    op.alter_column('Trainings', 'name',
               existing_type=sa.VARCHAR(length=35),
               type_=sa.String(length=50),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Trainings', 'name',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=35),
               existing_nullable=False)
    op.drop_constraint(None, 'TrainingLevels', type_='unique')
    op.alter_column('TrainingLevels', 'level',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=35),
               existing_nullable=False)
    # ### end Alembic commands ###
