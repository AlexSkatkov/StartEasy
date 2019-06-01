from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','deadline', 'customer','pro','goals','problems','connection','yearly_work_plan','cost_and_prodactivity','Application','General_Architecture_Highlights'
                  ,'Current_situation','System_character','Constraints','Glossary','External_demarcation','Internal_demarcation','User_Interface','Processes','Code_tables','Logical_files','Dictionary_of_information'
                  ,'Reports','Data_Security','Volumes_loads_and_performance','Interfaces_and_links','General_Architecture','Central_hardware','Environmental_infrastructure',
                  'Database','Development_and_maintenance_tools','Shelf_software','Hardware','Local_private_communications','similar_Technologies'
                  ,'Factors_involved','Work_Plan','next_step','Ongoing_operation','Service_and_maintenance','Integration','Robustness_and_reliability',
                  'Configurations','date_posted')

class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','deadline', 'customer','pro','goals','problems','connection','yearly_work_plan','cost_and_prodactivity','Application','General_Architecture_Highlights'
                  ,'Current_situation','System_character','Constraints','Glossary','External_demarcation','Internal_demarcation','User_Interface','Processes','Code_tables','Logical_files','Dictionary_of_information'
                  ,'Reports','Data_Security','Volumes_loads_and_performance','Interfaces_and_links','General_Architecture','Central_hardware','Environmental_infrastructure',
                  'Database','Development_and_maintenance_tools','Shelf_software','Hardware','Local_private_communications','similar_Technologies'
                  ,'Factors_involved','Work_Plan','next_step','Ongoing_operation','Service_and_maintenance','Integration','Robustness_and_reliability',
                  'Configurations','date_posted','user1','user2','user3','user4','client')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)