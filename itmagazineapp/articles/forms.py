from django.forms import ModelForm

from .models import Article


class ArticleForm (ModelForm):
    class Meta:
        model = Article
        fields = "__all__"


# notes
# remember fields are fields, and ALWAYS will appear as fields if it is "__all__"

# read this information 
# 1.https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/ 
# 2.Section "Selecting the fields to use" 
# 3.Note area.
