from django.forms import ModelForm


from admin_app.models import Message
from admin_app.models import Education
from admin_app.models import Skills
from admin_app.models import Expriences


class MessageForm(ModelForm):
    
    class Meta:
        model = Message
        fields = ('sender_name','sender_mail','sender_message')

class EducationForm(ModelForm):
    
    class Meta:
        model = Education
        fields = '__all__'

class SkillsForm(ModelForm):
    
    class Meta:
        model = Skills
        fields = '__all__'

class ExprienceForm(ModelForm):
    
    class Meta:
        model = Expriences
        fields = '__all__'


        


