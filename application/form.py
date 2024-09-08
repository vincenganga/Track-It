from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class UserInputForm(FlaskForm):
    # User to choose the type
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('income', 'income'),
                                ('expense', 'expense')
                                ])
    
    # User to choose the category
    category = SelectField('Category', validators=[DataRequired()],
                           choices=[('salary', 'salary'),
                                    ('rent', 'rent'),
                                    ('investment', 'investment'),
                                    ('side_hustle', 'side_hustle')
                                    ])
    
    # User to enter the amount
    amount = IntegerField("Amount", validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField("Generate")
    
