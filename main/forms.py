from flask_wtf import FlaskForm
from wtforms import SearchField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    # Every form fields are callable.
    # That means, each field returns the method whose name equals to each field name.
    word = SearchField("Enter a search word", validators=[DataRequired()])
    submit = SubmitField('Submit')
