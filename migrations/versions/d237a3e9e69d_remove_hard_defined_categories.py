"""remove hard defined categories

Revision ID: d237a3e9e69d
Revises: 28c6d0d63b38
Create Date: 2019-03-04 21:36:00.683553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd237a3e9e69d'
down_revision = '28c6d0d63b38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('passions')
    op.drop_index('ix_passion_id', table_name='passion')
    op.drop_index('ix_passion_name', table_name='passion')
    op.drop_table('passion')
    op.drop_index('ix_skill_id', table_name='skill')
    op.drop_index('ix_skill_name', table_name='skill')
    op.drop_table('skill')
    op.drop_index('ix_age_group_interest_id', table_name='age_group_interest')
    op.drop_index('ix_age_group_interest_name', table_name='age_group_interest')
    op.drop_table('age_group_interest')
    op.drop_table('skills')
    op.drop_table('age_group_interests')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('age_group_interests',
    sa.Column('opportunity_id', sa.INTEGER(), nullable=True),
    sa.Column('age_group_interests_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['age_group_interests_id'], ['age_group_interest.id'], ),
    sa.ForeignKeyConstraint(['opportunity_id'], ['opportunity.id'], )
    )
    op.create_table('skills',
    sa.Column('opportunity_id', sa.INTEGER(), nullable=True),
    sa.Column('skills_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['opportunity_id'], ['opportunity.id'], ),
    sa.ForeignKeyConstraint(['skills_id'], ['skill.id'], )
    )
    op.create_table('age_group_interest',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_age_group_interest_name', 'age_group_interest', ['name'], unique=1)
    op.create_index('ix_age_group_interest_id', 'age_group_interest', ['id'], unique=False)
    op.create_table('skill',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_skill_name', 'skill', ['name'], unique=1)
    op.create_index('ix_skill_id', 'skill', ['id'], unique=False)
    op.create_table('passion',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_passion_name', 'passion', ['name'], unique=1)
    op.create_index('ix_passion_id', 'passion', ['id'], unique=False)
    op.create_table('passions',
    sa.Column('opportunity_id', sa.INTEGER(), nullable=True),
    sa.Column('passion_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['opportunity_id'], ['opportunity.id'], ),
    sa.ForeignKeyConstraint(['passion_id'], ['passion.id'], )
    )
    # ### end Alembic commands ###